# Gold Price Prediction Model

This project involves the development of a **gold price prediction model** using a combination of **Random Forest** and **ARIMA models**. The model was trained on historical gold price data and is capable of forecasting day-wise gold prices with **97% accuracy**, significantly improving from an initial accuracy of **76%**.

## Project Overview

We developed a **gold price prediction model** using time series analysis, focusing on improving forecasting accuracy. The model leverages advanced techniques like **Random Forest** and **ARIMA** to predict gold prices on a daily basis. The project aims to provide accurate predictions for investors, traders, and analysts in the precious metals market.

## Key Features

- **Improved Prediction Accuracy**: Achieved an impressive **97% accuracy** after applying Random Forest and ARIMA models, up from **76%** in initial experiments.
- **Data Preprocessing**: Performed extensive data cleaning, manipulation, and exploratory data analysis (EDA) on time series data spanning from **2016 to 2021**.
- **Forecasting**: Deployed the prediction model using **Streamlit**, making it accessible for real-time day-wise gold price forecasting.

## Technical Details

- **Data Source**: Time series data (2016-2021) on historical gold prices.
- **Tools Used**: 
  - **Python** for data processing, modeling, and analysis
  - **Random Forest** for machine learning-based predictions
  - **ARIMA** for time series forecasting
  - **Streamlit** for model deployment

## Steps Taken

1. **Data Cleaning**: Cleaned the raw data to handle missing values, outliers, and inconsistencies.
2. **Exploratory Data Analysis (EDA)**: Visualized and understood the data trends, patterns, and seasonal variations.
3. **Modeling**: 
   - Built **Random Forest** model for price prediction.
   - Applied **ARIMA** model for capturing time-dependent patterns.
4. **Model Improvement**: Enhanced accuracy from 76% to 97% through hyperparameter tuning and model refinement.
5. **Deployment**: Used **Streamlit** to deploy the final model, making it accessible for real-time predictions.

## Installation

To run the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/gold-price-prediction.git
   cd gold-price-prediction
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app to interact with the model:
   ```bash
   streamlit run app.py
   ```

## Project Structure

```
gold-price-prediction/
│
├── data/                   # Contains raw and processed data
│   └── gold_prices.csv     # Gold price data from 2016 to 2021
│
├── models/                 # Contains model scripts
│   ├── random_forest.py    # Random Forest model code
│   ├── arima_model.py      # ARIMA model code
│
├── app.py                 # Streamlit app for deployment
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
```

## Future Improvements

- Incorporate additional features such as geopolitical events, market trends, and currency fluctuations.
- Experiment with other models like LSTM for deep learning-based time series forecasting.
