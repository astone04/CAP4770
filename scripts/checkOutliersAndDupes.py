import pandas as pd

data = pd.read_csv("../data/removed_rows.csv")

count_less_than_100 = data[data['revenue'] < 100].shape[0]
count_less_than_1000 = data[data['revenue'] < 1000].shape[0]
count_less_than_10000 = data[data['revenue'] < 10000].shape[0]
count_less_than_100000 = data[data['revenue'] < 100000].shape[0]
count_less_than_1000000 = data[data['revenue'] < 1000000].shape[0]
num_duplicate_rows = data.duplicated().sum()

print("Number of duplicate rows:", num_duplicate_rows)
print("Count of rows with revenue less than 100: ", count_less_than_100)
print("Count of rows with revenue less than 1,000: ", count_less_than_1000)
print("Count of rows with revenue less than 10,000: ", count_less_than_10000)
print("Count of rows with revenue less than 100,000: ", count_less_than_100000)
print("Count of rows with revenue less than 1,000,000: ", count_less_than_1000000)

print("Dropping duplicates")

data = data.drop_duplicates()
num_duplicate_rows = data.duplicated().sum()

data.to_csv("../data/cleaned_data.csv", index=False)

print("Dataset successfully cleaned!")


