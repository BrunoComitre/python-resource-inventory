import yfinance as yf
import streamlit as st


st.write("""
# Simple Stock Price App
Show are the stock **closing price** and ***volume*** of Google!
""")

# Define the ticker symbol
ticker_symbol = 'GOOGL'

# Get data on thiss ticker
ticker_data = yf.Ticker(ticker_symbol)

# Get the historical prices for this ticker
ticker_dataframe =  ticker_data.history(period='1d', start='2010-5-31', end='2020-7-10')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write("""
## Opening Price
""")
st.line_chart(ticker_dataframe.Open)

st.write("""
## High Price
""")
st.line_chart(ticker_dataframe.High)

st.write("""
## Low Price
""")
st.line_chart(ticker_dataframe.Low)

st.write("""
## Closing Price
""")
st.line_chart(ticker_dataframe.Close)
	
st.write("""
## Volume Price
""")
st.line_chart(ticker_dataframe.Volume)

st.write("""
## Dividends Price
""")
st.line_chart(ticker_dataframe.Dividends)

st.write("""
## Info 
""")
ticker_data.info

st.write("""
## Calendar 
""")
ticker_data.calendar

st.write("""
## Recommendations 
""")
ticker_data.recommendations

# print(ticker_dataframe)
