import pandas as pd
import os

def generate_user_list(input_file, output_file):
    """
    Generate a user_list.txt file from the facebook_combined.txt file.

    Args:
        input_file (str): Path to the input facebook_combined.txt file.
        output_file (str): Path to save the user_list.txt file.
    """
    data = pd.read_csv(input_file, sep=" ", header=None, names=["user1", "user2"])
    unique_users = pd.unique(pd.concat([data["user1"], data["user2"]]))
    user_list = pd.DataFrame({
        "org_id": unique_users,
        "remap_id": range(len(unique_users))
    })
    user_list.to_csv(output_file, sep="\t", index=False)
    print(f"User list file saved to {output_file}")

if __name__ == "__main__":
    BASE_PATH = os.path.abspath(os.path.dirname(__file__))
    input_file_path = os.path.join(BASE_PATH, "datasets", "facebook", "input", "facebook_combined.txt")
    output_file_path = os.path.join(BASE_PATH, "datasets", "facebook", "output", "user_list.txt")
    generate_user_list(input_file_path, output_file_path)
