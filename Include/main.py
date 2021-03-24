from news_data import News
from sendEmail import Email
from stock_data import Stock

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

stock = Stock()
data = stock.getStockData(STOCK_NAME)
data_list = [value for (key, value) in data.items()]


def getPriceDifference():
    # The absolute value of difference between yesterday_closing_price and  day_before_yesterday_closing_price
    difference = float(data_list[0]["4. close"]) - float(data_list[1]["4. close"])

    # percentage difference in price between closing price yesterday and closing price the day before yesterday.
    diff_percent = round((difference / float(data_list[0]["4. close"])) * 100)
    return abs(diff_percent), difference

def getTopThreeHeadLines(up_down):
    news_data = News()
    three_articles = news_data.getNews(COMPANY_NAME)

    # Create a new list of the first 3 article's headline and description using list comprehension.
    formatted_articles = [
        f"{STOCK_NAME}: {up_down}{priceDifference}%\nHeadline: {article['title']}. \nBrief: {article['description']}"
        for article in three_articles]
    return formatted_articles


def sendEmail(emailAdd, up_down):
    # Sending each article as a separate email.
    email = Email(emailAdd)
    formatted_articles = getTopThreeHeadLines(up_down)
    for article in formatted_articles:
        email.send(article)
        print("sent")

[priceDifference ,difference] = getPriceDifference()

# getting the first 3 news pieces for the COMPANY_NAME.
#If difference percentage is greater than 5 then print("Get News").

# For testing purpouses I set the significant_difference to 0.5
if priceDifference > 0.5:
    # determining wether stock price has surged or declined
    if difference >= 0:
        up_down = "Surged "
    else:
        up_down = "Dropped "

    print(up_down)
	#Enter destination email here
    sendEmail("DestinationEmail", up_down )






