# STONKS 📈💹

## 1. Stock Watch

The Stock Watch program, implemented in Python, allows users to retrieve and view the past 5 days' closing prices for a company's shares in either the Indian (NSE) or US (NASDAQ) stock market. The program uses the `yfinance` library for fetching historical stock data and Pandas for data manipulation and display.

### Usage

1. **Menu-driven Interface:**
   - When you run the program, it presents a menu-driven interface to choose the stock market:
      - Enter `1` for the Indian Stock Market (NSE).
      - Enter `2` for the US Stock Market (NASDAQ).

2. **Input Company Information:**
   - After selecting the stock market, the program prompts the user to enter the company symbol.

3. **View Closing Prices:**
   - The program retrieves and displays the past 5 days' closing prices for the chosen company in a tabular format using Pandas.

4. **Save to CSV:**
   - The closing prices are saved to a CSV file named `{company_symbol}_{exchange}_closing_prices.csv`.

5. **Display Information:**
   - The chosen company name, symbol, and the table of closing prices are displayed.

6. **CSV File Location:**
   - The program informs the user about the location of the saved CSV file.


## 2. LIVE STOCK PRICE 

### Get Live Stock Price

This Python script retrieves the live stock price using the Alpha Vantage API. It fetches the global quote for a specified stock symbol and prints the live price.

### Usage

1. **Alpha Vantage API Key:**
   - Replace `'YOUR_API_KEY'` in the script with your actual Alpha Vantage API key.

2. **Stock Symbol:**
   - Replace `'AAPL'` in the script with the stock symbol for which you want to get the live price.

3. **Run the Script:**
   - Execute the script to see the live price of the specified stock.


### Requirements

- Python 3.x
- `yfinance` library: Install with `!pip install yfinance`
- `pandas` library: Install with `!pip install pandas`

