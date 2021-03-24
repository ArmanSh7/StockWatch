import requests

class News:
    def __init__(self):
        self.api_key = "NEWS_API_KEY"
        self.request_endpoint = "https://newsapi.org/v2/everything"

    def getNews(self, COMPANY_NAME):
        news_params = {
                "apiKey": self.api_key,
                "qInTitle": COMPANY_NAME,
            }
        news_response = requests.get(self.request_endpoint, params=news_params)
        articles = news_response.json()["articles"]

        #returning a list that contains the first 3 articles
        return articles[:3]


