import pandas as pd
import ast
from datetime import datetime
import json
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
nltk.download('punkt')

# functions to process the realease date

# function to handle date parsing and extraction
def custom_to_datetime(date_str):
    try:
        return pd.to_datetime(date_str)
    except:
        try:
            # if there's only a year, assume January 1st of that year
            return pd.to_datetime(date_str + '-01-01')
        except:
            # if the date is still not parseable, return NaT
            return pd.NaT

def process_release_date(df, date_column):
    
    # apply the custom function to the 'release_date' column
    df['release_date'] = df[date_column].apply(custom_to_datetime)

    # extract year, month, and day, and calculate days since release
    df['release_year'] = df['release_date'].dt.year
    df['release_month'] = df['release_date'].dt.month
    df['release_day'] = df['release_date'].dt.day

    # calculate the number of days since release
    current_date = datetime.now()
    df['days_since_release'] = df['release_date'].apply(lambda x: (current_date - x).days if not pd.isna(x) else None)

    return df

#_____________________________________________


# functions to process 'languages' and 'countries' Json columns

def safe_eval(d):
    try:
        return ast.literal_eval(d)
    except ValueError:
        return {}

def remove_surrogates(d):
    cleaned = {}
    for key, value in d.items():
        try:
            value.encode('utf-8')
            cleaned[key] = value
        except UnicodeEncodeError:
            pass  # Skip any values that cause encoding errors
    return cleaned

def process_column(df, column_name):
    
    # apply the safe_eval function to parse the strings as dictionaries
    df[column_name + '_dict'] = df[column_name].apply(safe_eval)

    # clean out surrogates from the dictionaries
    df[column_name + '_dict'] = df[column_name + '_dict'].apply(remove_surrogates)

    # extract values into a list
    df[column_name + '_list'] = df[column_name + '_dict'].apply(lambda x: list(x.values()))

    # one-hot encode the list into a new DataFrame where each category is a column using dummies
    category_dummies = df[column_name + '_list'].apply(lambda x: '|'.join(x)).str.get_dummies(sep='|')

    # join the one-hot encoded DataFrame back to the original DataFrame
    df = df.join(category_dummies)

    # drop the original column and the intermediate dictionary column as they are no longer needed
    df.drop([column_name, column_name + '_dict', column_name + '_list'], axis=1, inplace=True)

    return df

def preprocess_movie_data(df, column_name):
    return process_column(df, column_name)

#_____________________________________________

#functions to process the genre column



#_____________________________________________



# functions to remove un wanted types and have clean data frame to train the regression model on
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
