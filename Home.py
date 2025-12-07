import streamlit as st

#set page title and icon
st.set_page_config(page_title='Coronary Artery Disease Dataset Explorer', page_icon='✈️')


st.title('✈️ Airline Satisfaction Dataset Explorer')
st.subheader('Welcome to the Airline Satisfaction dataset explorer app')
st.write('This app provides an interactive platform to explore traveler satisfaction.')
st.write('You can visualize the distribution of data in Data Overview and Dictionary pages, explore relationships between features on Exploratory Analysis page, and even make your own confusion matrix model on Make Your Own Matrix page!')
st.write('When your done exploring, fly over to the Prediction Insights page for experimental results performed on this dataset using Machine Learning Classifying Models.')
st.image('imgs/airline.jpg', caption="Airline")