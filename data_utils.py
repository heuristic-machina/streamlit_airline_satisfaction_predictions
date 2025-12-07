import pandas as pd
import streamlit as st

DATA_PATH = "data/airline.csv"

@st.cache_data
def load_airline():
    """Load the Airline dataset from local file, cached by Streamlit."""
    return pd.read_csv(DATA_PATH)