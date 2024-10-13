import yfinance as yf
import pandas as pd

# Specify the stock ticker symbol
ticker_symbol = 'IBM'


stock_data = yf.Ticker(ticker_symbol)

# Get the historical market data (monthly frequency)
data = stock_data.history(period='1mo', interval='1d')

# Fix date column
data = data.reset_index()
data['Date'] = data['Date'].dt.date

# Print the data
print(data.columns)
