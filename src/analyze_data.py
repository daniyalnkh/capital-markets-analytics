import pandas as pd

# Read the CSV with:
# - first column as the index (dates)
# - first two rows as column headers (for multi-index: field + ticker)
df = pd.read_csv(
    "data/raw/market_data.csv",
    header=[0, 1],     # two header rows
    index_col=0,       # first column = index (Date)
    parse_dates=True   # parse index as datetime
)

print("Columns:")
print(df.columns)
print("\nFirst rows:")
print(df.head())

# Extract Adjusted Close prices
adj_close = df["Close"]

print("\nAdjusted Close:")
print(adj_close.head())

returns = adj_close.pct_change().dropna()
adj_close.to_csv("data/processed/prices.csv")
returns.to_csv("data/processed/returns.csv")

