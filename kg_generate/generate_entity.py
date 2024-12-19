import os

def generate_entity_list(item_list_file, merged_featname_file, output_file):
    """
    Generate an entity_list.txt file by combining org_id from item_list.txt and full featname from merged_featname.txt.
    """
    # Collect org_ids from item_list.txt
    item_org_ids = set()
    with open(item_list_file, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) >= 2:
                item_org_ids.add(parts[1])  # Add org_id from item_list

    # Collect featname org_ids from merged_featname.txt
    featname_org_ids = set()
    with open(merged_featname_file, 'r') as f:
        for line in f:
            # Extract the entire featname (stop at the first number in the line)
            parts = line.strip().split(" ", 1)  # Split once
            if len(parts) > 1:
                featname = parts[0] + " " + parts[1].split()[0]  # Combine the first two parts
                featname_org_ids.add(featname.strip())

    # Combine all unique org_ids
    all_org_ids = sorted(item_org_ids.union(featname_org_ids))

    # Write to entity_list.txt
    with open(output_file, 'w') as f:
        f.write("org_id\tremap_id\n")  # Header
        for remap_id, org_id in enumerate(all_org_ids):
            f.write(f"{org_id}\t{remap_id}\n")

if __name__ == "__main__":
    BASE_PATH = os.path.abspath(os.path.dirname(__file__))
    item_list_path = os.path.join(BASE_PATH, "datasets/facebook/output/item_list.txt")
    merged_featname_path = os.path.join(BASE_PATH, "datasets/facebook/intermediate/merged_featname.txt")
    output_path = os.path.join(BASE_PATH, "datasets/facebook/output/entity_list.txt")
    generate_entity_list(item_list_path, merged_featname_path, output_path)
    print(f"Entity list saved to {output_path}")
