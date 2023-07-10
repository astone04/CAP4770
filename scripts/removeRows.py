import pandas as pd

data = pd.read_csv("../data/removed_columns.csv")

data = data[~(data['genres'] == "[]")]
data = data[~(data['revenue'] == 0.0)]
data = data[~(data['revenue'].isnull())]
data = data[~(data['revenue'].isna())]

data.to_csv("../data/removed_rows.csv", index=False)

print("Rows removed successfully!")
