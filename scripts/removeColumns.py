import pandas as pd

data = pd.read_csv("../data/original_data.csv")

data = data[["budget", "genres", "revenue", "release_date", "vote_average"]]

data.to_csv("../data/removed_columns.csv", index=False)

print("Columns removed successfully!")