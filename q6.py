import pandas as pd
import ast

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
    # Apply the safe_eval function to parse the strings as dictionaries
    df[column_name + '_dict'] = df[column_name].apply(safe_eval)

    # Clean out surrogates from the dictionaries
    df[column_name + '_dict'] = df[column_name + '_dict'].apply(remove_surrogates)

    # Extract values into a list
    df[column_name + '_list'] = df[column_name + '_dict'].apply(lambda x: list(x.values()))

    # One-hot encode the list into a new DataFrame where each category is a column
    category_dummies = df[column_name + '_list'].apply(lambda x: '|'.join(x)).str.get_dummies(sep='|')

    # Join the one-hot encoded DataFrame back to the original DataFrame
    df = df.join(category_dummies)

    # Drop the original column and the intermediate dictionary column as they are no longer needed
    df.drop([column_name, column_name + '_dict', column_name + '_list'], axis=1, inplace=True)

    return df

def preprocess_movie_data(df, column_name):
    return process_column(df, column_name)

