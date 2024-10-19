import pandas as pd

def create_summary_table(df):
    """
    Creates a summary DataFrame with feature name, data type, number of unique values, and if it has missing values.
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
    
    Returns:
        pd.DataFrame: A summary DataFrame.
    """
    
    sum_dict = {'Feature Name': df.columns.to_list(), 
            'Data Type': df.dtypes,
            'Has Missing Values?': df.nunique(),
            'Number of Unique Values': df.isnull()
            }
    
    return pd.DataFrame(sum_dict)
