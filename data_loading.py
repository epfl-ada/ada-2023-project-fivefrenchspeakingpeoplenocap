import pandas as pd

# Necessary paths to load the datasets
DATA_PATH = "./data/"
DATA_PATH_MOVIESUMMARIES = DATA_PATH + "MovieSummaries/"
DATA_PATH_TMDB = DATA_PATH + "TMDB/"
DATA_PATH_IMDB = DATA_PATH + "IMDBData/"
DATA_PATH_FINANCIAL = DATA_PATH + "Financial/"

DATASET_PATH = {
    "movie_metadata": DATA_PATH_MOVIESUMMARIES + "movie.metadata.tsv",
    "plot_summaries": DATA_PATH_MOVIESUMMARIES + "plot_summaries.txt",
    "movie_budget": DATA_PATH_TMDB + "movies_metadata.csv",
    "imdb_ratings": DATA_PATH_IMDB + "title.ratings.tsv",
    "imdb_basics": DATA_PATH_IMDB + "title.basics.tsv",
    "cpi_data": DATA_PATH_FINANCIAL + "CPI.csv",
    "gdp_data": DATA_PATH_FINANCIAL + "GDP.csv",
}

# Column names for each dataset
DATASET_COLUMNS = {
    "movie_metadata": [
        "wikipedia_id",
        "freebase_movie_id",
        "title",
        "release_date",
        "revenue",
        "runtime",
        "languages",
        "countries",
        "genres",
    ],
    "plot_summaries": [
        "wikipedia_id",
        "plot",
    ],
    "movie_budget": [
        "budget",
        "imdb_id",
        "original_title",
        "popularity",
        "release_date",
        "revenue",
        "runtime",
        "title",
        "vote_average",
        "vote_count",
    ],
    "imdb_ratings": ["imdb_id", "imdb_rating", "num_votes"],
    "imdb_basics": [
        "imdb_id",
        "title_type",
        "primary_title",
        "title",
        "is_adult",
        "year",
        "end_year",
        "runtime",
        "genres",
    ],
}

# Data types for the datasets
DATASET_TYPES = {
    "movie_metadata": {
        "wikipedia_id": "string",
        "freebase_movie_id": "string",
        "title": "string",
        "release_date": "string",
        "revenue": "float64",
        "runtime": "float64",
        "languages": "object",
        "countries": "object",
        "genres": "object",
    },
    "plot_summaries":{
        "wikipedia_id": "string",
        "plot": "string",
    },
    "movie_budget": {
        "budget": "object",
        "imdb_id": "string",
        "original_title": "object",
        "popularity": "object",
        "release_date": "object",
        "revenue": "float64",
        "runtime": "float64",
        "title": "object",
        "vote_average": "float64",
        "vote_count": "float64",
    },
    "imdb_ratings": {
        "imdb_id": "string",
        "imdb_rating": "float64",
        "num_votes": "int64",
    },
    "imdb_basics": {
        "imdb_id": "string",
        "title_type": "string",
        "primary_title": "string",
        "title": "string",
        "is_adult": "string",
        "year": "string",
        "end_year": "string",
        "runtime": "string",
        "genres": "string",
    },
}


def load_dataset(name):
    """Loads a dataset from the given name

    Args:
        name (string): Name of the dataset to load

    Returns:
        pandas.DataFrame: The loaded dataset
    """
    sep = "\t"
    header = 0
    skiprows = None

    if name == "movie_metadata" or name == "plot_summaries":
        header = None
    elif name == "movie_budget" or name == "cpi_data" or name == "gdp_data":
        sep = ","
        if name != "movie_budget":
            skiprows = 4

    print("Loading dataset: " + name)

    if name in ["movie_metadata", "imdb_ratings", "imdb_basics", "plot_summaries"]:
        return pd.read_csv(
            DATASET_PATH[name],
            sep=sep,
            header=header,
            names=DATASET_COLUMNS[name],
            dtype=DATASET_TYPES[name],
            skiprows=skiprows,
            index_col=False,
        )
    elif name in ["movie_budget", "cpi_data", "gdp_data"]:
        return pd.read_csv(
            DATASET_PATH[name],
            sep=sep,
            header=header,
            dtype=DATASET_TYPES[name] if name == "movie_budget" else None,
            skiprows=skiprows,
            index_col=False,
            usecols=DATASET_COLUMNS[name] if name == "movie_budget" else None,
        )
    else:
        raise ValueError("Dataset name not found")
