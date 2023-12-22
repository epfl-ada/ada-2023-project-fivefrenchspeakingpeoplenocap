import pandas as pd
import ast
from datetime import datetime
import json


def find_duplicates(df_or_list, subsets):
    """
    Checks for duplicates in the given dataframe(s) based on the provided subsets.

    Parameters:
    df_or_list: A single dataframe or a list of dataframes to check for duplicates.
    subsets (list): List of column subsets for duplicate check. Should correspond to the dataframe(s).
    """
    df_copy = df_or_list.copy(deep=True)
    # convert single dataframe to a list for uniform processing
    if isinstance(df_copy, pd.DataFrame):
        df_copy = [df_copy]
        subsets = [subsets]

    results = []
    for df, subset in zip(df_copy, subsets):
        duplicates = df[df.duplicated(subset=subset, keep=False)].sort_values(by=subset)
        if duplicates.empty:
            results.append(
                "No duplicates found in the specified columns: {}".format(subset)
            )
        else:
            results.append(duplicates)

    # if there's only one dataframe, return the result directly, else return a list of results
    return results[0] if len(results) == 1 else results


def preprocess_release_date(df, date_column):
    # apply the custom function to the 'release_date' column
    df["release_date"] = df[date_column].apply(custom_to_datetime)

    # extract year, month, and day, and calculate days since release
    df["release_year"] = df["release_date"].dt.year
    df["release_month"] = df["release_date"].dt.month
    df["release_day"] = df["release_date"].dt.day

    return df


# function to handle date parsing and extraction
def custom_to_datetime(date_str):
    try:
        return pd.to_datetime(date_str)
    except:
        try:
            # if there's only a year, assume January 1st of that year
            return pd.to_datetime(date_str + "-01-01")
        except:
            # if the date is still not parseable, return NaT
            return pd.NaT


def safe_eval(d):
    try:
        return ast.literal_eval(d)
    except ValueError:
        return {}


def remove_surrogates(d):
    cleaned = {}
    for key, value in d.items():
        try:
            value.encode("utf-8")
            cleaned[key] = value
        except UnicodeEncodeError:
            pass
    return cleaned


def preprocess_json(df, column_name):
    # apply the safe_eval function to parse the strings as dictionaries
    df[column_name + "_dict"] = df[column_name].apply(safe_eval)

    # clean out surrogates from the dictionaries
    df[column_name + "_dict"] = df[column_name + "_dict"].apply(remove_surrogates)

    # extract values into a list
    df[column_name + "_list"] = df[column_name + "_dict"].apply(
        lambda x: list(x.values())
    )

    # one-hot encode the list into a new DataFrame where each category is a column using dummies
    category_dummies = (
        df[column_name + "_list"].apply(lambda x: "|".join(x)).str.get_dummies(sep="|")
    )

    # join the one-hot encoded DataFrame back to the original DataFrame
    df = df.join(category_dummies)

    # drop the original column and the intermediate dictionary column as they are no longer needed
    df.drop(
        [column_name, column_name + "_dict", column_name + "_list"],
        axis=1,
        inplace=True,
    )

    return df


# functions to remove un wanted types and have clean data frame to train the regression model
def remove_unwanted_dtypes(df, keep_types):
    """
    Removes columns from a DataFrame that do not have a specified data type.

    Parameters:
    df (pd.DataFrame): The DataFrame to process.
    keep_types (list): List of data types to keep in the DataFrame.

    Returns:
    pd.DataFrame: A DataFrame with only the columns of specified data types.
    """
    # Filter the columns based on the specified data types
    columns_to_keep = df.select_dtypes(include=keep_types).columns

    # Drop the columns that are not of the specified data types
    df = df[columns_to_keep].copy()

    return df

# one-hot encode the top genres in the DataFrame, unlike the panda dummies this personalized function can include multiple genres
def one_hot_encode_top_genres(df, top_genres):
    for genre in top_genres:
        df['genre_' + genre] = df['filtered_genre_names'].apply(lambda genres: int(genre in genres))
    
    return df