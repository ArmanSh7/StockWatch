import requests
class Stock:
    def __init__(self):
        self.api_key = "API_KEY"
        self.request_endpoint = "https://www.alphavantage.co/query"

    def getStockData(self, STOCK_NAME):
        # yesterday's closing stock price
        stock_params = {
            "function": "TIME_SERIES_DAILY",
            "symbol": STOCK_NAME,
            "apikey": self.api_key,
        }
        response = requests.get(self.request_endpoint, params=stock_params)
        return response.json()["Time Series (Daily)"]
