import pandas as pdgit

def find_duplicates(df_or_list, subsets):
    """
    Checks for duplicates in the given dataframe(s) based on the provided subsets.

    Parameters:
    df_or_list: A single dataframe or a list of dataframes to check for duplicates.
    subsets (list): List of column subsets for duplicate check. Should correspond to the dataframe(s).
    """
    df_copy = df_or_list.copy(deep=True)
    # Convert single dataframe to a list for uniform processing
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

    # If there's only one dataframe, return the result directly, else return a list of results
    return results[0] if len(results) == 1 else results
