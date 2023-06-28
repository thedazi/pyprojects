import requests
from datetime import date, timedelta
from twilio.rest import Client

# Constants
STOCK = "IBM"
COMPANY_NAME = "IBM"
ALPHAVANTAGE_API = 'VTH1TWEBEABBLQER'
NEWS_API = '685fb42bd2024d7180dd3171a08b48aa'
REQUIRED_DIFF = 3
twilo_account_sid = 'AC3afb5ef7afdce4a87bdcbbb7e2cc6c62'
twilo_auth_token= '445b5b766e1143da5ad31c19a5e7cb0e'
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#datetime functions
today = date.today()
today_date = str(today)
yesterday_date = str(today - timedelta(1))
yesteryesterday_date = str(today - timedelta(2))
print(today_date)



def two_day_stock_comparison(stock):
  # API pulls
  alphavantage_url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={stock}&apikey={ALPHAVANTAGE_API}'
  AV_get = requests.get(alphavantage_url)
  AV_data = AV_get.json()

  yester_data = float(AV_data['Time Series (Daily)'][yesterday_date]['5. adjusted close'])
  two_day_ago_data = float(AV_data['Time Series (Daily)'][yesteryesterday_date]['1. open'])

  two_day_actual_diff = round(yester_data - two_day_ago_data,2)

  if round(abs(yester_data - two_day_ago_data),2) > REQUIRED_DIFF:
    news_url = f'https://newsapi.org/v2/everything?q={COMPANY_NAME}&from={yesterday_date}&sortBy=publishedAt&apiKey={NEWS_API}'
    news_get = requests.get(news_url)
    news_data = news_get.json()
    top_3_articles = news_data['articles'][:3]
    message_content = f'{STOCK}: {two_day_actual_diff}% change'
    if two_day_actual_diff > 0:
      message_content += ' 🔺\n'
    else:
      message_content += ' 🔻\n'
    message_content += f"Source: {top_3_articles[0]['source']['name']}\nHeadline: {top_3_articles[0]['title']}\nURL: {top_3_articles[0]['url']}"
    # for article in range(len(top_3_articles)):
    #   message_content += f"Source: {top_3_articles[article]['source']['name']}\nHeadline: {top_3_articles[article]['title']}\nURL: {top_3_articles[article]['url']}"
    return message_content
  else:
    return False

full_notification = two_day_stock_comparison(STOCK)
print(full_notification)

def send_news(input=full_notification):
  if input == True:
    client = Client(twilo_account_sid, twilo_auth_token)
    message = client.messages.create(
    body=input,
    from_='+13203628468',
    to='+818053030666'
  )
    print(message.status)
  else:
    return False
    


send_news()
  
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

