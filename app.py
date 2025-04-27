import streamlit as st
import pandas as pd
from cleaning import clean_csv


st.set_page_config(page_title="CSV Cleaner", layout="wide")


st.title("🛠️CleanSheet: Get your data cleaned ASAP!")


file = st.file_uploader("Upload your CSV file", type=["csv"])

if file:
    df = pd.read_csv(file)
    st.subheader("📄 Preview of Uploaded CSV")
    st.dataframe(df.head(5))

    remove_nulls = st.checkbox("Remove Null values")
    clean_text = st.checkbox("Remove special characters and spaces")
    missing_vals = st.checkbox("Handle missing values")
    remove_duplicates = st.checkbox("Remove duplicate rows")

    if missing_vals:
        st.subheader("Select one method to handle missing values:")
        action = st.selectbox(
            "Choose how to handle missing values:",
            ("Do nothing", "Drop rows with missing values", "Fill missing with 0", "Fill missing with 'Unknown'")
        )

        if action == "Drop rows with missing values":
            df.dropna(inplace=True)

        elif action == "Fill missing with 0":
            df.fillna(0, inplace=True)

        elif action == "Fill missing with 'Unknown'":
            df.fillna("Unknown", inplace=True)

    if st.button("🚀 Clean Data"):
        cleaned_df = clean_csv(df, clear_nulls=remove_nulls, clean_text=clean_text,remove_duplicates=remove_duplicates)

        st.success("✅ Data cleaned successfully!")
        st.subheader("🔍 Cleaned Data Preview")
        st.dataframe(cleaned_df.head(5))
        csv = cleaned_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download Cleaned CSV",
            data=csv,
            file_name="cleaned_data.csv",
            mime="text/csv"
        )
    
    
