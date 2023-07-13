import pandas as pd
import numpy as np


# the following function determines possible outliers in the 'cleaned_data.csv' file
def check_for_outliers(file):

    df = pd.read_csv(file)
    outliers = {}
    for col in df.columns:
        # skip the 'genres' and 'release_date' columns
        if col == "genres" or col == "release_date":
            continue

        # calculate the mean and standard deviation for the column
        mean = df[col].mean()
        std_dev = df[col].std()


        # identify the outliers that are > 3 std dev away from mean (in both directions), this can be changed if needed
        outliers[col] = df[col][abs(df[col] - mean) >= 3 * std_dev]

        print("number of outliers in the", col, "column:", outliers[col].size)


    return outliers

# the following function prints the outliers listing each category and writes it to a new .csv file
def print_no_outlier_file(outliers):

    for category, values in outliers.items():
        print(f"* {category}: {values}")


print_no_outlier_file(check_for_outliers("../data/removed_rows.csv"))