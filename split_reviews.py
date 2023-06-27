"""
This file contains the code necessary to split the review file in three files, one containig the training data, one containig the validation data and one containing the testing data.

The split is done to better operate on them when using online learning
"""
import random

def split_file(input_file_path, train_output_path, val_output_path, test_output_path, train_ratio=0.7, val_ratio=0.15, seed=None):
    if seed is not None:
        random.seed(seed)

    with open(input_file_path, 'r') as input_file:
        train_file = open(train_output_path, 'w')
        val_file = open(val_output_path, 'w')
        test_file = open(test_output_path, 'w')

        for line in input_file:
            # determine which file to write to based on the random ratio
            rand_value = random.random()
            if rand_value < train_ratio:
                output_file = train_file
            elif rand_value < train_ratio + val_ratio:
                output_file = val_file
            else:
                output_file = test_file

            output_file.write(line)

        train_file.close()
        val_file.close()
        test_file.close()

        print("[+] Splitting complete.")


if __name__ == "__main__":
    data_dir = "yelp-data/" 
    review_file = "yelp_academic_dataset_review.json"

    print("[+] Commencing splitting...")
    split_file(
        data_dir + review_file,
        data_dir + "train_" + review_file, 
        data_dir + "val_" + review_file, 
        data_dir + "test_" + review_file, 
        train_ratio=0.70, val_ratio=0.15)
