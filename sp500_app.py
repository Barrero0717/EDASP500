import yfinance as yf
import streamlit as st
import base64
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

st.title('S&P 500 App')

st.markdown(
    """
    This app retrieves the list of the **S&P 500** (from Wikipedia)
    * **Python libraries:** base64, pandas, streamlit, numpy, yfinance, matplotlib, seaborn
    * **Data source:** [Wikipedia](https://wikipedia.org/)
    """
)

st.sidebar.header('User Input Features')

# Web Scraping of S&P 500 data
def load_data():
    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    html = pd.read_html(url, header=0)
    df = html[0]
    return df

df = load_data()

# Sidebar - Sector selection
sector = df.groupby('GICS Sector')
sorted_sector_unique = sorted(df['GICS Sector'].unique())
selected_sector = st.sidebar.multiselect('Sector', sorted_sector_unique)

# Filtering data
df_selected_sector = df[df['GICS Sector'].isin(selected_sector)]

st.header('Display Companies in Selected Sector')
st.write("Data Dimension: " + str(df_selected_sector.shape[0]) + " rows and " + str(df_selected_sector.shape[1]) + " columns")
st.dataframe(df_selected_sector)
