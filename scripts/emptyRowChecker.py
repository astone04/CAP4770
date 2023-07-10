import pandas as pd

data = pd.read_csv("../data/removed_rows.csv")

count_empty_genres = data[data['genres'] == "[]"].shape[0]
count_empty_release_date = data['release_date'].isnull().sum()
count_zero_popularity = data[data['vote_average'] == 0.0].shape[0]
count_zero_revenue = data[data['revenue'] == 0.0].shape[0]
count_null_revenue = data['revenue'].isnull().sum()
count_zero_budget = data[data['budget'] == "0"].shape[0]
total_rows = data.shape[0]

print("Number of rows where the 'genres' column is an empty list:", count_empty_genres)
print("Number of rows where the 'release_date' column is empty:", count_empty_release_date)
print("Number of rows where the 'vote_average' column is 0.0:", count_zero_popularity)
print("Number of rows where the 'revenue' column is 0:", count_zero_revenue)
print("Number of rows where the 'revenue' column is null:", count_null_revenue)
print("Number of rows where the 'budget' column is 0:", count_zero_budget)
print("Total number of rows: ", total_rows)