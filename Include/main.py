import requests
import smtplib

# from tkinter import *
#
# window = Tk()
# window.title("StockWatch")
# window.minsize(width=300, height=300)
# window.config(padx=20, pady=20)
#
#
# #StockWatch Label
# StockWatch_label = Label(text="StockWatch", font=("Arial", 12, "bold"), bg="light green")
# StockWatch_label.grid(column=1, row=0)
# StockWatch_label.config(padx=10, pady=10)
#
# #StockName label
# StockName_label = Label(text="Which Stock do you want?", font=("Arial", 12, "bold"))
# StockName_label.grid(column=1, row=1)
# StockName_label.config(padx=10, pady=10)
#
# #stockName
# stockName = Entry(width=20)
# print(stockName.get())
# stockName.grid(column=1, row=2)
#
# #SurgeOrDropLabel Label
# num_label = Label(text="What would be significant surge or drop?", font=("Arial", 12, "bold"))
# num_label.grid(column=1, row=3)
# num_label.config(padx=10, pady=10)
#
# #SurgeNumber
# surgeNum = Entry(width=20)
# surgeNum.grid(column=1, row=4)
# high_dif =-55
#
# def submit():
#     compareIt()
#
# #Button
# exitButton = Button(text="Submit", command=submit)
# exitButton.grid(column=1, row=5)

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stockApi_key="KT4W1L6X22ZEAWL3"
newsApi_key ="bbdcfe37116b4bb3adc8f71bf5ebaa7b"
TWILIO_SID = "YOUR TWILIO ACCOUNT SID"
TWILIO_AUTH_TOKEN = "YOUR TWILIO AUTH TOKEN"

#yesterday's closing stock price
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": stockApi_key,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

#The day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

#The absolute value of difference between float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None


#percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent = round((difference / float(yesterday_closing_price)) * 100)
print(diff_percent)
if diff_percent > 5 :
    print(difference)
    up_down = "Surged"
else:
    up_down = "Dropped"
print(up_down)

# getting the first 3 news pieces for the COMPANY_NAME.
#If difference percentage is greater than 5 then print("Get News").
if abs(diff_percent) > 1:
    news_params = {
        "apiKey": newsApi_key,
        "qInTitle": COMPANY_NAME,
    }

news_response = requests.get(NEWS_ENDPOINT, params=news_params)
articles = news_response.json()["articles"]

#Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
three_articles = articles[:3]
print(three_articles)
#
# STEP 3: Use Twilio to send a seperate message with each article's title and description to your phone number.

#Create a new list of the first 3 article's headline and description using list comprehension.
formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
print(formatted_articles)

#TODO 8. - Sending each article as a separate message via email.

for article in formatted_articles:
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login("moshiripedram9@gmail.com", "Esteghlal1")
    connection.sendmail(
        from_addr="moshiripedram9@gmail.com",
        to_addrs="arman.shahriari95@gmail.com",
        msg=f"Subject:StockWash News \n\n {article}"
    )




# window.mainloop()