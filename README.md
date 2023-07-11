

This project uses Pandas and Python 3.11, so to reproduce our results you must:
    1. Clone this repository.
    2. Make sure you have Python downloaded and correctly installed.
    3. Make sure you have Pandas correctly installed by using 'pip install pandas'.

To start with the data preprocessing you must:
    1. Run removeColumns.py
    2. Run emptyRowChecker.py


# CAP4770: Movie Production Recommender

Welcome to the Movie Production Recommender: an application that recommends which type of movie a movie studio should pursue to produce during each time of the year. We will ask questions like time of the year, budget, etc. and provide the user with the genre that will provide them the best profits and ratings.

## Authors

- [Benjamin Mendoza](https://www.github.com/bendoza)
- [Amy Stone](https://github.com/astone04)
- [Erik Mercado](https://www.github.com/)

## Development

#### Dependencies

You need to have [Python 3](https://www.python.org/downloads/),
and [Pandas](https://pandas.pydata.org/).

Verify the tools are installed by running the following commands:

```zsh
python3 --version
print(pd. __version__) [in Python script]
```

Navigate to the `scripts` folder 

```zsh
cd scripts
```

Run removeColumns.py

```zsh
python3 removeColumns.py
```

Run emptyRowChecker.py for stats revolving semi-cleaned data

```zsh
python3 emptyRowChecker.py
``` 
