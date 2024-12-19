import os

def read_entity_list(entity_file):
    """
    Read entity_list.txt and return a dictionary mapping org_id to remap_id.
    """
    entity_mapping = {}
    with open(entity_file, 'r') as f:
        for line in f.readlines()[1:]:
            parts = line.strip().rsplit(maxsplit=1)
            if len(parts) == 2:
                org_id, remap_id = parts
                entity_mapping[org_id] = remap_id
    return entity_mapping

def read_merged_featname(merged_featname_file):
    """
    Read merged_featname.txt and return a dictionary mapping featname to a list of nodes.
    """
    featname_to_nodes = {}
    with open(merged_featname_file, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            # Split line by space to separate featname and nodes
            parts = line.split()
            featname = parts[0] + " " + parts[1]  # First two parts form the featname
            nodes = parts[2:]  # Remaining parts are nodes
            featname_to_nodes[featname] = nodes
    return featname_to_nodes


def read_relation_list(relation_file):
    """
    Read relation_list.txt and return a dictionary mapping org_id to remap_id.
    """
    relations = {}
    with open(relation_file, 'r') as f:
        for line in f.readlines()[1:]:
            parts = line.strip().rsplit(maxsplit=1)
            if len(parts) == 2:
                org_id, remap_id = parts
                relations[org_id] = remap_id
    return relations

def generate_kg(entity_mapping, featname_to_nodes, relations, output_file):
    """
    Generate kg_final.txt using entity mappings, featname to nodes, and relation mappings.
    """
    unique_triples = set()

    with open(output_file, 'w') as f:
        for featname, nodes in featname_to_nodes.items():
            # Debug: Print featname and nodes
            print(f"Processing featname: {featname}, nodes: {nodes}")

            relation_key = featname.split(';anonymized')[0]
            relation_remap_id = relations.get(relation_key)
            if relation_remap_id is None:
                print(f"Relation key '{relation_key}' not found in relations.")
                continue

            featname_remap_id = entity_mapping.get(featname)
            if featname_remap_id is None:
                print(f"Featname '{featname}' not found in entity mapping.")
                continue

            for node in nodes:
                node_remap_id = entity_mapping.get(node)
                if node_remap_id is None:
                    print(f"Node '{node}' not found in entity mapping.")
                    continue

                triple = (node_remap_id, relation_remap_id, featname_remap_id)
                if triple not in unique_triples:
                    unique_triples.add(triple)
                    f.write(f"{node_remap_id}\t{relation_remap_id}\t{featname_remap_id}\n")

    print(f"KG file saved to {output_file}")

if __name__ == "__main__":
    BASE_PATH = os.path.abspath(os.path.dirname(__file__))
    entity_file_path = os.path.join(BASE_PATH, "datasets/facebook/output/entity_list.txt")
    merged_featname_file_path = os.path.join(BASE_PATH, "datasets/facebook/intermediate/merged_featname.txt")
    relation_file_path = os.path.join(BASE_PATH, "datasets/facebook/output/relation_list.txt")
    output_file_path = os.path.join(BASE_PATH, "datasets/facebook/output/kg_final.txt")

    entity_mapping = read_entity_list(entity_file_path)
    featname_to_nodes = read_merged_featname(merged_featname_file_path)
    relations = read_relation_list(relation_file_path)
    generate_kg(entity_mapping, featname_to_nodes, relations, output_file_path)


