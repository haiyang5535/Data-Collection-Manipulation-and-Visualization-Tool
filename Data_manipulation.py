import pandas as pd

def company_data_manipulation(df):
    if 'Unnamed: 0' in df.columns:
        df.drop(['Unnamed: 0'], axis=1, inplace=True)

    if 'company_location' in df.columns:
        df[["City", "State"]] = df['company_location'].str.split(',', expand=True)
        df.drop(["company_location"], axis=1, inplace=True)
    
    if 'revenue_range' in df.columns:
        df[["min_revenue", "max_revenue"]] = df['revenue_range'].str.split('-', expand=True)

    string_columns = df.select_dtypes(include=['object']).columns
    for col in string_columns:
        df[col] = df[col].str.strip()
    
    df.fillna("N/A", inplace=True)
    
    return df
