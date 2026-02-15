import yfinance as yf
import os

os.system('clear')

ticker_symbol = str(input('Enter the ticker symbol (eg. AAPL): ')).upper()

ticker = yf.Ticker(ticker_symbol)

data_1d = ticker.history(period='1d', interval='5m')
data_5d = ticker.history(period='5d', interval='15m')
data_1m = ticker.history(period='1mo')
data_1y = ticker.history(period='1y')

print("===========================")
print(f"{ticker_symbol} Stock Report")
print("===========================")
print()
print(data_1y.sample(10))
print()