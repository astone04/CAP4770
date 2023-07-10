import pandas as pd

data = pd.read_csv("data/removed_columns.csv")

count_empty_genres = data[data['genres'] == "[]"].shape[0]
count_empty_release_date = data['release_date'].isnull().sum()
count_zero_popularity = data[data['vote_average'] == 0.0].shape[0]
count_zero_revenue = data[data['revenue'] == 0.0].shape[0]

print("Number of rows where the 'genres' column is an empty list: ", count_empty_genres)
print("Number of rows where the 'release_date' column is empty or null: ", count_empty_release_date)
print("Number of rows where the 'vote_average' column is 0.0: ", count_zero_popularity)
print("Number of rows where the 'revenue' column is 0: ", count_zero_revenue)