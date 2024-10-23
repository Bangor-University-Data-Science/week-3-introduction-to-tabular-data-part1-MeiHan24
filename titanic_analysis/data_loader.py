import pandas as pd
import numpy as np

def load_titanic_data(filepath: str) -> pd.DataFrame:
       
    """
    Loads the Titanic dataset from the specified file path.
    
    Args:
        filepath (str): Path to the Titanic CSV file.
    
    Returns:
        pd.DataFrame: Loaded Titanic dataset as a DataFrame.
    """


    return pd.read_csv(filepath)

    # df = pd.read_csv(filepath)
    # if df:
    #     return df
    # else: 
    #     return pd.DataFrame() #empty data set
   
    

#df = pd.read_csv('../data/titanic.csv')


# print(df.head())
# print(df.shape)
# print(len(df))
# print(df.index)
# print(df.columns)
# print("Column 0: " + df.columns[0])
# print(df.dtypes)