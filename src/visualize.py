import pandas as pd
import matplotlib.pyplot as plt

# Load processed data
prices = pd.read_csv(
    "data/processed/prices.csv",
    index_col=0,
    parse_dates=True
)

returns = pd.read_csv(
    "data/processed/returns.csv",
    index_col=0,
    parse_dates=True
)

print("Prices head:")
print(prices.head())

print("\nReturns head:")
print(returns.head())

# Plot price history
plt.figure(figsize=(10, 6))
for column in prices.columns:
    plt.plot(prices.index, prices[column], label=column)

plt.title("Asset prices over time")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.tight_layout()
plt.show()

# Plot daily returns
plt.figure(figsize=(10, 6))
for column in returns.columns:
    plt.plot(returns.index, returns[column], label=column)

plt.title("Daily returns")
plt.xlabel("Date")
plt.ylabel("Return")
plt.legend()
plt.tight_layout()
plt.show()

# Cumulative returns
cumulative = (1 + returns).cumprod()

plt.figure(figsize=(10, 6))
for column in cumulative.columns:
    plt.plot(cumulative.index, cumulative[column], label=column)

plt.title("Cumulative returns (growth of 1 unit)")
plt.xlabel("Date")
plt.ylabel("Growth factor")
plt.legend()
plt.tight_layout()
plt.show()

