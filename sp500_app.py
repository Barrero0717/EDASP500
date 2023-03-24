import yfinance as yf
import streamlit as st
import base64
import pandas as pd
import numpy as np

st.title('S&P 500 App')

st.markdown(
    """
    This app retrieves the list of the **S&P 500** (from Wikipedia)
    * **Python libraries:** base64, pandas, streamlit, numpy, yfinance
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
st.write("Data Dimension: " + str(df_selected_sector.shape[0]) + " rows and " + str(df_selected_sector.shape[1]) + " columns.")
st.dataframe(df_selected_sector)

# Get Finance Data
if(selected_sector != []):
    finance_data = yf.download(
        tickers = list(df_selected_sector[:50].Symbol),
        period = "ytd",
        interval = "1d",
        group_by = "ticker",    
        auto_adjust = True,
        prepost = True,
        threads = True,
        proxy = None
        )

#Download S&P 500 data
def filedownload(df):
    csv = df.to_csv(index = False)
    b64 = base64.b64encode(csv.encode()).decode() # strings <-> bytes conversions
    href = f'<a href="data:file/csv;base64,{b64}" download="SP500.csv">Download CSV File</a>'
    return href
st.markdown(filedownload(df_selected_sector), unsafe_allow_html=True)

# Add silder into the sidebar
num_company = st.sidebar.slider('Number of Companies', 1, 50)

# Plot Closing Price of Query Symbol with area_chart
if st.button('Show Plots'):
    st.header('Stock Closing Price')
    for i in list(df_selected_sector.Symbol)[:num_company]:
        st.write(i)
        st.area_chart(pd.DataFrame(finance_data[i].Close))