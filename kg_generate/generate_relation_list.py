import os

def generate_relation_list_with_unique_org_id(featnames_file, output_file):
    """
    Generate a relation_list file using unique org_id extracted from featnames.
    """
    unique_org_ids = set()

    with open(featnames_file, 'r') as feat_file:
        for line in feat_file:
            line = line.strip()
            if not line:
                continue  # Skip empty lines
            # Extract the part before "anonymized"
            org_id = line.split(";anonymized")[0].strip()
            unique_org_ids.add(org_id)

    # Write unique org_ids to the output file with remap_id
    with open(output_file, 'w') as rel_file:
        rel_file.write("org_id remap_id\n")
        for remap_id, org_id in enumerate(sorted(unique_org_ids)):
            rel_file.write(f"{org_id} {remap_id}\n")

if __name__ == "__main__":
    BASE_PATH = os.path.abspath(os.path.dirname(__file__))
    featnames_file = os.path.join(BASE_PATH, "datasets/facebook/intermediate/merged_featname.txt")
    output_file = os.path.join(BASE_PATH, "datasets/facebook/output/relation_list.txt")
    generate_relation_list_with_unique_org_id(featnames_file, output_file)
    print(f"Relation list saved to {output_file}")
