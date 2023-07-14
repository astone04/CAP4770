# CAP4770: Movie Production Recommender

Welcome to the Movie Production Recommender: an application that recommends which type of movie a movie studio should pursue to produce during each time of the year. We will ask questions like time of the year, budget, etc. and provide the user with the genre that will provide them the best profits and ratings.

## Authors

- [Benjamin Mendoza](https://www.github.com/bendoza)
- [Amy Stone](https://github.com/astone04)
- [Erik Mercado](https://github.com/TheLittleChosenOne)

## Development

#### Dependencies

You need to have [Python 3](https://www.python.org/downloads/),
and [Pandas](https://pandas.pydata.org/).

Verify the tools are installed by running the following commands:

```zsh
python3 --version
print(pd. __version__) [in Python script]
```

#### Data Cleaning Process

Navigate to the `scripts` folder 

```zsh
cd scripts
```

Run emptyRowChecker.py (with original_data.csv, which must be inputted manually) for stats revolving un-cleaned data

```zsh
python3 emptyRowChecker.py
``` 

Run removeColumns.py, which removes unnecessary attributes from each row in the original dataset

```zsh
python3 removeColumns.py
```

Run removeRows.py, which removes rows where the values are not accurate or complete, and also removes duplicate rows

```zsh
python3 removeRows.py
```

Run emptyRowChecker.py (with removed_rows.csv, which must be inputted manually) for stats revolving semi-cleaned data

```zsh
python3 emptyRowChecker.py
```

Run identifyOutliers.py to view outliers, and stats revolving around the attributes susceptible to outliers: revenue/budget/vote_average.
```zsh
python3 identifyOutliers.py
```

The prior step identifies outliers from only vote_average, because after inspection we found the outliers in revenue/budget play to the strengths of the problem we are trying to solve.

Run emptyRowChecker.py (with cleaned_data.csv, which must be inputted manually) for stats revolving fully cleaned data

```zsh
python3 emptyRowChecker.py
```
