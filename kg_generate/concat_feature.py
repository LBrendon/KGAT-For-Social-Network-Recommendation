import pandas as pd
import os

def map_features_to_nodes(feat_file, featnames_file, output_file):
    """
    Map features to nodes and generate the output file.
    """
    feat_df = pd.read_csv(feat_file, header=None, delim_whitespace=True)
    node_ids = feat_df.iloc[:, 0].tolist()
    features = feat_df.iloc[:, 1:]

    with open(featnames_file, 'r') as f:
        featnames = [line.strip().split(' ', 1) for line in f.readlines()]

    feature_to_nodes = {}
    for feat_id, feat_name in featnames:
        feat_id = int(feat_id)
        nodes_with_feat = [node_ids[i] for i in range(len(node_ids)) if features.iloc[i, feat_id] == 1]
        feature_to_nodes[feat_name] = nodes_with_feat

    with open(output_file, 'w') as f:
        for feat_name, nodes in feature_to_nodes.items():
            node_list = " ".join(map(str, nodes))
            f.write(f"{feat_name} {node_list}\n")

    print(f"Feature mapping saved to {output_file}")

if __name__ == "__main__":
    BASE_PATH = os.path.abspath(os.path.dirname(__file__))
    input_files = [
        ("0.feat", "0.featnames", "featnames01.txt"),
        ("107.feat", "107.featnames", "featnames02.txt"),
        ("348.feat", "348.featnames", "featnames03.txt"),
        ("414.feat", "414.featnames", "featnames04.txt"),
        ("686.feat", "686.featnames", "featnames05.txt"),
        ("698.feat", "698.featnames", "featnames06.txt"),
        ("1684.feat", "1684.featnames", "featnames07.txt"),
        ("1912.feat", "1912.featnames", "featnames08.txt"),
        ("3437.feat", "3437.featnames", "featnames09.txt"),
        ("3980.feat", "3980.featnames", "featnames10.txt"),
    ]

    for feat_file, featnames_file, output_file in input_files:
        feat_file_path = os.path.join(BASE_PATH, "datasets/facebook/input", feat_file)
        featnames_file_path = os.path.join(BASE_PATH, "datasets/facebook/input", featnames_file)
        output_file_path = os.path.join(BASE_PATH, "datasets/facebook/intermediate", output_file)

        map_features_to_nodes(feat_file_path, featnames_file_path, output_file_path)
