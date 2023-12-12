import yfinance as yf

def get_past_5day_prices(company_symbol):
  """
  Retrieves past 5 days of closing prices for a company's shares
  registered in NSE.

  Args:
    company_symbol: The symbol of the company on NSE.

  Returns:
    A dictionary containing the closing prices for the past 5 days.
  """
  # Download historical data
  stock_data = yf.download(company_symbol, period="10d", interval="1d")

  # Extract closing prices
  closing_prices = stock_data["Close"].to_dict()

  # Format dates
  dates = list(closing_prices.keys())
  dates = [date.strftime("%Y-%m-%d") for date in dates]

  # Create dictionary with date as key and closing price as value
  past_5day_prices = dict(zip(dates, closing_prices.values()))

  return past_5day_prices

# Example usage
company_symbol = input("Enter the company symbol: ")

past_5day_prices = get_past_5day_prices(company_symbol)

print(f"Past 10 days closing prices for {company_symbol}:")
for date, price in past_5day_prices.items():
  print(f"{date}: {price:.2f}")
