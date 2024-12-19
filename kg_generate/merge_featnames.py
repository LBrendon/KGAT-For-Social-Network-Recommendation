import collections
import re
import os

def merge_featnames_with_nodes(input_files, output_file):
    """
    Merge multiple featnames files into one, ensuring all featnames and their associated nodes are included.
    """
    feature_dict = collections.defaultdict(set)

    for file_path in input_files:
        with open(file_path, 'r') as f:
            for line in f:
                # Match feature name and nodes using regex
                match = re.match(r"^(.*?)(\d+)\s+(.*)$", line.strip())
                if match:
                    featname_base = match.group(1).strip()  # Feature name base
                    featname_number = match.group(2).strip()  # Feature number
                    nodes_part = match.group(3).strip()  # Nodes part

                    # Format feature name with underscore
                    feature_name = f"{featname_base}_{featname_number}"

                    # Convert nodes to integers
                    nodes = set(map(int, nodes_part.split()))
                    feature_dict[feature_name].update(nodes)

    # Write the combined results to the output file
    with open(output_file, 'w') as f:
        for feature_name, nodes in sorted(feature_dict.items()):
            # Sort nodes in ascending order and format as a string
            nodes_str = " ".join(map(str, sorted(nodes)))
            f.write(f"{feature_name} {nodes_str}\n")

if __name__ == "__main__":
    BASE_PATH = os.path.abspath(os.path.dirname(__file__))
    input_files = [
        os.path.join(BASE_PATH, f"datasets/facebook/intermediate/featnames{i:02d}.txt") for i in range(1, 11)
    ]
    output_file = os.path.join(BASE_PATH, "datasets/facebook/intermediate/merged_featname.txt")
    merge_featnames_with_nodes(input_files, output_file)
    print(f"Merged featnames saved to {output_file}")
