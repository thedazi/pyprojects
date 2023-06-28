import datetime as dt
import smtplib
import ssl
import pandas


###------ DATETIME
now = dt.datetime.now()
today = (now.month, now.day)   # outputs weekday 0=monday, 6=sunday
current_year = now.year

data = pandas.read_csv('Day32datetimebirthday/birthdaylist.csv')
birthday_dict = {(data_row.month, data_row.day):data_row for (index, data_row) in data.iterrows()}

if today in birthday_dict:
  birthday_person = birthday_dict[today]
  receiver = birthday_person['name']
  age = now.year - birthday_person['year']
  receiving_email = birthday_person['email']


  ###------ SMTP/SSL
  my_email = 'Donotreplydazbot@gmail.com'
  ps = 'awlyatnjagmrmqql'
  message = f"Subject:Happy Birthday {receiver}!\n\nHappy Birthday, you are {age} now and you/'ve done it again making it another year. Well done!"
  smtp_server = "smtp.gmail.com"
  smtp_port = 587
  connection = smtplib.SMTP(smtp_server,smtp_port)
  simple_email_context = ssl.create_default_context()

  ###------ Email Script
  with smtplib.SMTP(smtp_server,smtp_port) as connection:
    connection.starttls(context=simple_email_context)
    connection.login(user=my_email,password=ps)
    connection.sendmail(from_addr=my_email,
                        to_addrs=receiving_email,
                        msg=message)
