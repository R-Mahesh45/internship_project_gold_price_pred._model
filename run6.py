# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 12:50:09 2024

@author: Care
"""

import streamlit as st
import pandas as pd
import pickle
from datetime import timedelta
import time
import matplotlib.pyplot as plt

# Function to create the page layout
def create_page():
    st.title('Gold Price Prediction')

    # Sidebar for inputs
    with st.sidebar:
        st.header('Input Parameters')
        # Dropdown for selecting year, month, and day
        year = st.selectbox('Choose prediction year', range(2022, 2030))
        month = st.selectbox('Choose prediction month', range(1, 13))
        day = st.selectbox('Choose prediction day', range(1, 32))

    # Converted selected date to DataFrame
    pred_date = pd.DataFrame({'year': [year], 'month': [month], 'day': [day]})
    features_timestamp = pd.to_datetime(pred_date)

    return features_timestamp

# Load the model
@st.cache_data
def load_model():
    with open('pred.pkl', 'rb') as f:
        loaded_model = pickle.load(f)
    return loaded_model

# Get features and make prediction
features_timestamp = create_page()
loaded_model = load_model()

if st.button('Submit'):
    try:
        # Add a progress bar
        with st.spinner('doing this guys wait...'):
            progress_bar = st.progress(0)
            for i in range(100):
                # Update the progress bar with each iteration.
                time.sleep(0.01)
                progress_bar.progress(i + 1)

            res = loaded_model.predict(start=features_timestamp.iloc[0], end=features_timestamp.iloc[0])
            st.subheader('Predicted Result')
            st.write(f"Price of gold for {features_timestamp.iloc[0].strftime('%Y-%m-%d')} is {round(res[0],2)}")

            # Generate monthly report
            start_date = features_timestamp.iloc[0].replace(day=1)
            end_date = start_date + pd.DateOffset(months=1) - timedelta(days=1)
            monthly_res = loaded_model.predict(start=start_date, end=end_date)
            st.subheader('Monthly Report')
            st.line_chart(monthly_res)

            # Trend Analysis
            st.subheader('Trend Analysis')
            plt.figure(figsize=(10,5))
            plt.plot(monthly_res)
            plt.title('Trend Analysis')
            st.pyplot(plt)
    except Exception as e:
        st.error(f"An error occurred: {e}")
