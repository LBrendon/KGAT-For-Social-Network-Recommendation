import pandas as pd
import os

def generate_item_list(input_file, output_file):
    """
    Generate an item_list.txt file from the facebook_combined.txt file.
    """
    df = pd.read_csv(input_file, sep=" ", header=None, names=["user1", "user2"])
    unique_users = pd.concat([df['user1'], df['user2']]).unique()
    user_list_df = pd.DataFrame({
        'org_id': unique_users,
        'remap_id': range(len(unique_users)),
        'freebase_id': ['null'] * len(unique_users)
    })
    user_list_df.to_csv(output_file, sep="\t", index=False, header=["org_id", "remap_id", "freebase_id"])
    print(f"Item list saved to {output_file}")

if __name__ == "__main__":
    BASE_PATH = os.path.abspath(os.path.dirname(__file__))
    input_file_path = os.path.join(BASE_PATH, "datasets", "facebook", "input", "facebook_combined.txt")
    output_file_path = os.path.join(BASE_PATH, "datasets", "facebook", "output", "item_list.txt")
    generate_item_list(input_file_path, output_file_path)
