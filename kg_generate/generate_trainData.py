import os
def transform_facebook_combined(input_file, output_file):
    """
    Transform the facebook_combined.txt file into the format:
    0 1 2 3 4 5 6 7 8 9
    """
    from collections import defaultdict

    connections = defaultdict(list)
    with open(input_file, 'r') as file:
        for line in file:
            node1, node2 = map(int, line.strip().split())
            connections[node1].append(node2)

    with open(output_file, 'w') as file:
        for node, connected_nodes in sorted(connections.items()):
            file.write(f"{node} {' '.join(map(str, sorted(connected_nodes)))}\n")

if __name__ == "__main__":
    BASE_PATH = os.path.abspath(os.path.dirname(__file__))
    input_file_path = os.path.join(BASE_PATH, "datasets", "facebook", "input", "facebook_combined.txt")
    output_file_path = os.path.join(BASE_PATH, "datasets", "facebook", "intermediate", "facebook_transformed.txt")
    transform_facebook_combined(input_file_path, output_file_path)
