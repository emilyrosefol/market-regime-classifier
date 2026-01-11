​You​
import yfinance as yf
import pandas as pd

symbol = "BTC-USD"
interval = "1h"   # if this errors later, change to "1d"
period = "2y"

df = yf.download(symbol, interval=interval, period=period, auto_adjust=False)
df.reset_index(inplace=True)
df.columns = [c.lower() for c in df.columns]

df.to_csv("raw_prices.csv", index=False)

print("✅ Saved raw_prices.csv")
print(df.head())
