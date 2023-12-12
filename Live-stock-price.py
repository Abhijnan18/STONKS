import requests
import json

def get_stock_price(api_key, symbol):
    base_url = "https://www.alphavantage.co/query"
    function = "GLOBAL_QUOTE"
    datatype = "json"

    params = {
        "function": function,
        "symbol": symbol,
        "apikey": api_key,
        "datatype": datatype,
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        if "Global Quote" in data:
            stock_data = data["Global Quote"]
            return stock_data["05. price"]
        else:
            print("Error: Unable to retrieve stock data.")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def main():
    # Replace 'YOUR_API_KEY' with your actual Alpha Vantage API key
    api_key = "QS6J3T7CPCIKDMMR"

    # Replace 'AAPL' with the stock symbol you want to get the live price for
    stock_symbol = "TSLA"

    price = get_stock_price(api_key, stock_symbol)
    
    if price is not None:
        print(f"The live price of {stock_symbol} is ${price}")

if __name__ == "__main__":
    main()
