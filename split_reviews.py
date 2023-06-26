import json
"""
This file contains the code necessary to split the review file in three files, one containig the training data, one containig the validation data and one containing the testing data.

The split is done to better operate on them when using online learning
"""

def split_data_file(input_file, train_file, val_file, test_file, train_ratio=0.70, val_ratio=0.15, test_ratio=0.15):
    total_lines = 6990280 # from https://www.yelp.com/dataset

    train_lines = int(train_ratio * total_lines)
    val_lines = int(val_ratio * total_lines)
    test_lines = int(test_ratio * total_lines)

    with open(input_file, 'r') as input_f:
        with open(train_file, 'w') as train_f:
            for _ in range(train_lines):
                line = json.loads(input_f.readline())
                json.dump(line, train_f, indent=2)
        print("[+] Done with training split.")

        with open(val_file, 'w') as val_f:
            for _ in range(val_lines):
                line = json.loads(input_f.readline())
                json.dump(line, val_f, indent=2)
        print("[+] Done with validation split.")

        with open(test_file, 'w') as test_f:
            for _ in range(test_lines):
                line = json.loads(input_f.readline())
                json.dump(line, test_f, indent=2)
        print("[+] Done with test split.")

    print("[+] Splitting complete!")


data_dir = "yelp-data/" 
review_file = "yelp_academic_dataset_review.json"
# Example usage
split_data_file(
    data_dir + review_file,
    data_dir + "train_" + review_file, 
    data_dir + "val_" + review_file, 
    data_dir + "test_" + review_file, 
    train_ratio=0.70, val_ratio=0.15, test_ratio=0.15)
