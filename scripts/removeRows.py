import pandas as pd

data = pd.read_csv("../data/removed_columns.csv")

data = data[~(data['genres'] == "[]")]
data = data[~(data['revenue'] == 0.0)]
data = data[~(data['revenue'].isnull())]
data = data[~(data['revenue'].isna())]
data = data[~(data['budget'].isnull())]
data = data[~(data['budget'] == "0")]

num_duplicate_rows = data.duplicated().sum()

print("Number of duplicate rows:", num_duplicate_rows)
print()
print("Dropping duplicates")

data = data.drop_duplicates()
num_duplicate_rows = data.duplicated().sum()

data.to_csv("../data/cleaned_data.csv", index=False)

print("Rows removed successfully!")
