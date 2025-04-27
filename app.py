import pandas as pd
import streamlit as st
import re

def clean_csv(df,clear_nulls=False,clean_text=False,remove_duplicates=False):
    clean_df=df.copy()

    if clear_nulls:
        clean_df.dropna(inplace=True)

    if clean_text:
        columns=clean_df.select_dtypes(include=['object']).columns


        protected_cols = ['']
        for col in columns:
            if not any(substring in col for substring in ['ID', 'id', 'Date', 'date']) and clean_df[col].str.contains('[a-zA-Z]').any():
             clean_df[col] = clean_df[col].apply(clean_text_column)
    
    if remove_duplicates:
        clean_df.drop_duplicates(inplace=True)

        
    return clean_df


def clean_text_column(value):
    if isinstance(value, str):
        # Remove unwanted characters but keep spaces and alphanumeric characters
        return re.sub(r'[^a-zA-Z0-9\s]', '', value)
    return value
