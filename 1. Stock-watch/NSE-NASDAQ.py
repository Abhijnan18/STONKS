import yfinance as yf
import pandas as pd

def get_past_5day_prices(company_symbol, exchange):
    """
    Retrieves past 5 days of closing prices for a company's shares
    registered in the specified stock exchange.

    Args:
      company_symbol: The symbol of the company on the stock exchange.
      exchange: The stock exchange code ("NSE" for Indian, "US" for US).

    Returns:
      A DataFrame containing the closing prices for the past 5 days.
    """
    # Define the appropriate interval and period based on the stock exchange
    if exchange == "NSE" or exchange == "US":
        interval = "1d"
        period = "10d"
    else:
        raise ValueError("Invalid exchange code. Use 'NSE' for Indian or 'US' for US.")

    # Download historical data
    stock_data = yf.download(company_symbol, period=period, interval=interval)

    # Extract closing prices
    closing_prices = stock_data["Close"]

    return closing_prices

# Menu-driven interface
print("Welcome to the Stock Price Viewer!")
print("1. Indian Stock Market (NSE)")
print("2. US Stock Market")
choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    exchange = "NSE"
elif choice == "2":
    exchange = "US"
else:
    print("Invalid choice. Exiting.")
    exit()

# Example usage
company_symbol = input("Enter the company symbol: ")

# Get past 5 days closing prices
past_5day_prices = get_past_5day_prices(company_symbol, exchange)

# Display output in a table using Pandas
df = pd.DataFrame({"Date": past_5day_prices.index, "Closing Price(in USD)": past_5day_prices.values})
df["Date"] = df["Date"].dt.strftime("%Y-%m-%d")

# Save the DataFrame to a CSV file
output_csv_filename = f"{company_symbol}_{exchange}_closing_prices.csv"
df.to_csv(output_csv_filename, index=False)

# Display the chosen company name and symbol
print(f"\nChosen Company: {company_symbol} ({exchange})")

# Display the table with labels and without the index
styled_df = df.style.set_table_styles([{'selector': 'thead', 'props': [('display', 'none')]}])
styled_df.set_caption("Past 5 days closing prices")

# Display the company information
styled_df

# Inform the user about the CSV file
print(f"\nThe output has been saved to {output_csv_filename}")
