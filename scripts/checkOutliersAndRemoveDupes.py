import pandas as pd

data = pd.read_csv("../data/cleaned_data.csv")

revenue_less_than_100 = data[data['revenue'] < 100].shape[0]
revenue_less_than_1000 = data[data['revenue'] < 1000].shape[0]
revenue_less_than_10000 = data[data['revenue'] < 10000].shape[0]
revenue_less_than_100000 = data[data['revenue'] < 100000].shape[0]
revenue_less_than_1000000 = data[data['revenue'] < 1000000].shape[0]
budget_less_than_1 = data[data['budget'] < 1].shape[0]
budget_less_than_1000 = data[data['budget'] < 1000].shape[0]
budget_less_than_10000 = data[data['budget'] < 10000].shape[0]
budget_less_than_100000 = data[data['budget'] < 100000].shape[0]
budget_less_than_1000000 = data[data['budget'] < 1000000].shape[0]
num_duplicate_rows = data.duplicated().sum()

print("Number of duplicate rows:", num_duplicate_rows)
print("Count of rows with revenue less than 100: ", revenue_less_than_100)
print("Count of rows with revenue less than 1,000: ", revenue_less_than_1000)
print("Count of rows with revenue less than 10,000: ", revenue_less_than_10000)
print("Count of rows with revenue less than 100,000: ", revenue_less_than_100000)
print("Count of rows with revenue less than 1,000,000: ", revenue_less_than_1000000)
print()
print("Count of rows with budget less than 1: ", budget_less_than_1)
print("Count of rows with budget less than 1,000: ", budget_less_than_1000)
print("Count of rows with budget less than 10,000: ", budget_less_than_10000)
print("Count of rows with budget less than 100,000: ", budget_less_than_100000)
print("Count of rows with budget less than 1,000,000: ", budget_less_than_1000000)
print()
print("Dropping duplicates")

data = data.drop_duplicates()
num_duplicate_rows = data.duplicated().sum()

data.to_csv("../data/cleaned_data.csv", index=False)

print("Dataset successfully cleaned!")


