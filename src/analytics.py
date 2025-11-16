import pandas as pd

# Load daily returns
returns = pd.read_csv(
    "data/processed/returns.csv",
    index_col=0,        # first column is the date index
    parse_dates=True    # turn that index into real datetime
)

print("First rows of returns:")
print(returns.head())

# Mean and standard deviation of daily returns
mean_daily = returns.mean()
std_daily = returns.std()

print("\nMean daily returns:")
print(mean_daily)

print("\nDaily volatility (standard deviation):")
print(std_daily)

TRADING_DAYS = 252

annual_return = mean_daily * TRADING_DAYS
annual_vol = std_daily * (TRADING_DAYS ** 0.5)

print("\nAnnualised return:")
print(annual_return)

print("\nAnnualised volatility:")
print(annual_vol)

sharpe = annual_return / annual_vol

print("\nSharpe ratio (approx, rf = 0):")
print(sharpe)

corr = returns.corr()

print("\nCorrelation matrix of daily returns:")
print(corr)
