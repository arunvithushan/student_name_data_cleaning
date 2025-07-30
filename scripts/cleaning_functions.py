import pandas as pd
import numpy as np

# -----------------------------
# Missing Value Handlers
# -----------------------------

def fill_missing_values(df):
    df['children'].fillna(0, inplace=True)
    df['agent'].fillna(0, inplace=True)
    df['company'].fillna(0, inplace=True)
    df['country'].fillna('Unknown', inplace=True)
    return df

# -----------------------------
# Duplicate Handler
# -----------------------------

def remove_duplicates(df):
    df.drop_duplicates(inplace=True)
    return df

# -----------------------------
# Outlier Detection (IQR Method)
# -----------------------------

def remove_outliers_iqr(df, columns):
    for col in columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]
    return df

# -----------------------------
# Inconsistency Fixes
# -----------------------------

def fix_inconsistencies(df):
    # Remove rows where total guests = 0
    df = df[~((df['adults'] == 0) & (df['children'] == 0) & (df['babies'] == 0))]
    
    # Replace 'Undefined' meals with 'SC'
    df['meal'].replace('Undefined', 'SC', inplace=True)
    
    # Convert reservation date to datetime
    df['reservation_status_date'] = pd.to_datetime(df['reservation_status_date'])
    
    return df

# -----------------------------
# Validate Integrity
# -----------------------------

def validate_data(df):
    assert (df['adults'] + df['children'] + df['babies']).min() > 0, "Invalid guest count"
    return True

# -----------------------------
# Run Full Cleaning Pipeline
# -----------------------------

def clean_hotel_data(df):
    df = fill_missing_values(df)
    df = remove_duplicates(df)
    df = remove_outliers_iqr(df, ['lead_time', 'stays_in_weekend_nights',
                                  'stays_in_week_nights', 'adults',
                                  'children', 'babies', 'adr'])
    df = fix_inconsistencies(df)
    validate_data(df)
    return df
