import streamlit as st
from data_utils import load_airline


st.title('Overview')
#load dataset


df=load_airline()
# Data Overview

st.title("🔢 Data Overview")

st.subheader("About the Data")
st.write("""
        
    """)

st.image('imgs/business.jpg', caption="Business Class")

    # Dataset Display
st.subheader("Quick Glance at the Data")
if st.checkbox("Show DataFrame"):
        st.dataframe(df)

    # Shape of Dataset
if st.checkbox("Show Shape of Data"):
        st.write(f"The dataset contains {df.shape[0]} rows and {df.shape[1]} columns.")

