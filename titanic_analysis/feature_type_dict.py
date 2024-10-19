import pandas as pd

def create_feature_type_dict(df):
    
    """
    Classifies features into numerical (continuous or discrete) and categorical (nominal or ordinal).   
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.   
    Returns:
        dict: A dictionary classifying features into numerical and categorical types.
    """

    feature_types = {
        'numerical': { #['PassengerId', 'Survived', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare']
            'continuous': [],  # Fill with continuous numerical features
            'discrete': []  # Fill with discrete numerical features
        },
        'categorical': { #['Name', 'Sex', 'Ticket', 'Cabin', 'Embarked']
            'nominal': [],  # Fill with nominal categorical features
            'ordinal': []  # Fill with ordinal categorical features
        }
    }



    # 4 features = data types
    continuous_col = []
    discrete_col = []
    nominal_col = []
    ordinal_col = []

    numerical_col = df.select_dtypes(include = ['int64', 'float64']).columns.to_list() 
    for n_col in numerical_col:  
        if df[n_col].nunique() > 20:
            continuous_col.append(n_col)
        else:
            discrete_col.append(n_col)


    nominal_col = df.select_dtypes(include=['object',]).columns.to_list()
    ordinal_col = df.select_dtypes(include=['category', 'bool']).columns.to_list()


    feature_types['numerical']['continuous'] = continuous_col
    feature_types['numerical']['discrete'] = discrete_col
    feature_types['categorical']['nominal'] = nominal_col
    feature_types['categorical']['ordinal'] = ordinal_col

    print (f"nominal_col: {nominal_col}")
    print (ordinal_col)


    return feature_types