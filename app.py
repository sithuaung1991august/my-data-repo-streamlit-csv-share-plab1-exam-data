import streamlit as st
import pandas as pd

# Replace with the raw URL of your CSV file from GitHub
CSV_URL = "https://raw.githubusercontent.com/sithuaung1991august/my-data-repo-streamlit-csv-share-plab1-exam-data/refs/heads/main/Sample%20data%20PLAB%20-%20FInal%20revision.csv"

st.title("CSV Data Viewer from GitHub")

@st.cache_data
def load_data(url):
    try:
        df = pd.read_csv(url)
        return df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None

df = load_data(CSV_URL)

if df is not None:
    st.write("Here's a preview of your data:")
    st.dataframe(df)

    st.write(f"Shape of the data: {df.shape[0]} rows, {df.shape[1]} columns")

    if st.checkbox("Show column information"):
        st.write(df.info())

    if st.checkbox("Show descriptive statistics"):
        st.write(df.describe())
else:
    st.warning("Please ensure the CSV_URL is correct and accessible.")
