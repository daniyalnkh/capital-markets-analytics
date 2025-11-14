import yfinance as yf
import pandas as pd

tickers = ["SPY", "BTC-CAD", "ETH-CAD"]

data = yf.download(tickers, start="2018-01-01")
print(data.head())

data.to_csv("data/raw/market_data.csv")
