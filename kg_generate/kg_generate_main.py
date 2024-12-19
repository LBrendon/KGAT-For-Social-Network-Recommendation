import os
import logging
import argparse
from kg_generate.generate_userList import generate_user_list
from kg_generate.generate_itemList import generate_item_list
from kg_generate.concat_feature import map_features_to_nodes
from kg_generate.merge_featnames import merge_featnames_with_nodes
from kg_generate.generate_relation_list import generate_relation_list_with_unique_org_id
from kg_generate.generate_entity import generate_entity_list
from kg_generate.generate_kg import generate_kg, read_entity_list, read_merged_featname, read_relation_list
from kg_generate.generate_testData import generate_test_data
from kg_generate.generate_trainData import transform_facebook_combined

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define paths
BASE_PATH = os.path.abspath(os.path.dirname(__file__))
INPUT_PATH = os.path.join(BASE_PATH, "datasets", "facebook", "input")
INTERMEDIATE_PATH = os.path.join(BASE_PATH, "datasets", "facebook", "intermediate")
OUTPUT_PATH = os.path.join(BASE_PATH, "datasets", "facebook", "output")

# File paths
INPUT_FILES = {
    "facebook_combined": os.path.join(INPUT_PATH, "facebook_combined.txt"),
    "feat_files": [(os.path.join(INPUT_PATH, f"{name}.feat"), os.path.join(INPUT_PATH, f"{name}.featnames"))
                   for name in ["0", "107", "348", "414", "686", "698", "1684", "1912", "3437", "3980"]]
}
INTERMEDIATE_FILES = {
    "facebook_transformed": os.path.join(INTERMEDIATE_PATH, "facebook_transformed.txt"),
    "user_list": os.path.join(OUTPUT_PATH, "user_list.txt"),
    "item_list": os.path.join(OUTPUT_PATH, "item_list.txt"),
    "mapped_features": os.path.join(INTERMEDIATE_PATH, "mapped_features.txt"),
    "merged_featname": os.path.join(INTERMEDIATE_PATH, "merged_featname.txt"),
    "relation_list": os.path.join(OUTPUT_PATH, "relation_list.txt"),
    "entity_list": os.path.join(OUTPUT_PATH, "entity_list.txt"),
}
OUTPUT_FILES = {
    "kg_final": os.path.join(OUTPUT_PATH, "kg_final.txt"),
    "train_data": os.path.join(OUTPUT_PATH, "facebook_train.txt"),
    "test_data": os.path.join(OUTPUT_PATH, "facebook_test.txt"),
}

# Main pipeline
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="KGAT Data Processing Pipeline")
    parser.add_argument("--step", type=str, choices=[
        "all", "user", "item", "concat", "merge", "relation", "entity", "kg", "train_test", "transform"
    ], default="all", help="Specify which step to run. Default is 'all'.")
    args = parser.parse_args()

    try:
        # Step 1: Generate user list
        if args.step in ["all", "user"]:
            logging.info("Generating user list...")
            generate_user_list(INPUT_FILES["facebook_combined"], INTERMEDIATE_FILES["user_list"])
            logging.info("User list generated.")

        # Step 2: Generate item list
        if args.step in ["all", "item"]:
            logging.info("Generating item list...")
            generate_item_list(INPUT_FILES["facebook_combined"], INTERMEDIATE_FILES["item_list"])
            logging.info("Item list generated.")

        # Step 3: Concatenate features
        if args.step in ["all", "concat"]:
            logging.info("Mapping features to nodes...")
            for idx, (feat_file, featnames_file) in enumerate(INPUT_FILES["feat_files"], start=1):
                output_file = os.path.join(INTERMEDIATE_PATH, f"featnames{idx:02d}.txt")
                map_features_to_nodes(feat_file, featnames_file, output_file)
            logging.info("Feature mapping completed.")

        # Step 4: Merge featnames
        if args.step in ["all", "merge"]:
            logging.info("Merging featnames files...")
            featnames_files = [os.path.join(INTERMEDIATE_PATH, f"featnames{i:02d}.txt") for i in range(1, 11)]
            merge_featnames_with_nodes(featnames_files, INTERMEDIATE_FILES["merged_featname"])
            logging.info("Featnames merged successfully.")

        # Step 5: Generate relation list
        if args.step in ["all", "relation"]:
            logging.info("Generating relation list...")
            generate_relation_list_with_unique_org_id(
                INTERMEDIATE_FILES["merged_featname"], INTERMEDIATE_FILES["relation_list"]
            )
            logging.info("Relation list generated.")

        # Step 6: Generate entity list
        if args.step in ["all", "entity"]:
            logging.info("Generating entity list...")
            generate_entity_list(
                INTERMEDIATE_FILES["item_list"], INTERMEDIATE_FILES["merged_featname"], INTERMEDIATE_FILES["entity_list"]
            )
            logging.info("Entity list generated.")

        # Step 7: Generate knowledge graph
        if args.step in ["all", "kg"]:
            logging.info("Generating knowledge graph (kg_final.txt)...")
            entity_mapping = read_entity_list(INTERMEDIATE_FILES["entity_list"])
            featname_to_nodes = read_merged_featname(INTERMEDIATE_FILES["merged_featname"])
            relations = read_relation_list(INTERMEDIATE_FILES["relation_list"])
            generate_kg(entity_mapping, featname_to_nodes, relations, OUTPUT_FILES["kg_final"])
            logging.info("Knowledge graph generated.")

        # Step 8: Transform facebook_combined.txt
        if args.step in ["all", "transform"]:
            logging.info("Transforming facebook_combined.txt...")
            transform_facebook_combined(INPUT_FILES["facebook_combined"], INTERMEDIATE_FILES["facebook_transformed"])
            logging.info("Transformation completed.")

        # Step 9: Generate train and test data
        if args.step in ["all", "train_test"]:
            logging.info("Generating train and test datasets...")
            generate_test_data(
                INTERMEDIATE_FILES["facebook_transformed"],
                OUTPUT_FILES["train_data"],
                OUTPUT_FILES["test_data"]
            )
            logging.info("Train and test datasets generated.")

        logging.info("Pipeline execution completed.")

    except Exception as e:
        logging.error(f"Pipeline execution failed: {e}")
