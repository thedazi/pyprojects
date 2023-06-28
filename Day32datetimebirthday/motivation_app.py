import datetime as dt
import smtplib
import ssl
from random import choice

###------ DATETIME
now = dt.datetime.now()
weekday = now.weekday()   # outputs weekday 0=monday, 6=sunday

###------ Random Quote
with open('Day32datetimebirthday/quotes.txt') as quotes:
  quotes_data = quotes.read()
  quotes_list = quotes_data.splitlines()
  rand_quote = choice(quotes_list)

  


###------ SMTP/SSL
my_email = 'Donotreplydazbot@gmail.com'
ps = 'awlyatnjagmrmqql'

receiving_email = 'zak.g.dahl@gmail.com'
message = f'Subject:Monday Quote\n\n{rand_quote}'
smtp_server = "smtp.gmail.com"
smtp_port = 587
connection = smtplib.SMTP(smtp_server,smtp_port)

simple_email_context = ssl.create_default_context()

if weekday == 1:
  with smtplib.SMTP(smtp_server,smtp_port) as connection:
    connection.starttls(context=simple_email_context)
    connection.login(user=my_email,password=ps)
    connection.sendmail(from_addr=my_email,
                        to_addrs=receiving_email,
                        msg=message)

