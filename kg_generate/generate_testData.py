import os
import random

def generate_test_data(input_file, train_output_file, test_output_file):
    """
    Split input data into train and test datasets with an 80-20 split,
    ensuring train data is never empty for any node.

    Args:
        input_file (str): Path to the input data file.
        train_output_file (str): Path to save the train dataset.
        test_output_file (str): Path to save the test dataset.
    """
    with open(input_file, "r") as f:
        lines = f.readlines()

    train_data, test_data = [], []
    for line in lines:
        if line.strip():
            elements = line.strip().split()
            if len(elements) > 1:
                node = elements[0]
                neighbors = elements[1:]
                random.shuffle(neighbors)

                split_index = int(0.8 * len(neighbors))
                train_neighbors = neighbors[:split_index]
                test_neighbors = neighbors[split_index:]


                if len(train_neighbors) == 0 and len(test_neighbors) > 0:
                    train_neighbors.append(test_neighbors.pop(0))

                train_data.append(f"{node} " + " ".join(train_neighbors))
                test_data.append(f"{node} " + " ".join(test_neighbors))
            else:

                train_data.append(f"{elements[0]}")
                test_data.append(f"{elements[0]}")


    with open(train_output_file, "w") as train_file:
        train_file.write("\n".join(train_data))

    with open(test_output_file, "w") as test_file:
        test_file.write("\n".join(test_data))

    print(f"Train data saved to {train_output_file}")
    print(f"Test data saved to {test_output_file}")

if __name__ == "__main__":
    BASE_PATH = os.path.abspath(os.path.dirname(__file__))
    input_file_path = os.path.join(BASE_PATH, "datasets", "facebook", "intermediate", "facebook_transformed.txt")
    train_output_path = os.path.join(BASE_PATH, "datasets", "facebook", "output", "train.txt")
    test_output_path = os.path.join(BASE_PATH, "datasets", "facebook", "output", "test.txt")
    generate_test_data(input_file_path, train_output_path, test_output_path)
