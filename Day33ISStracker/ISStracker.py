import requests
from datetime import datetime
import smtplib
import ssl
from time import sleep

MY_LAT = 35.689487 # Your latitude
MY_LONG = 139.691711 # Your longitude
format = 0
jp_time = 9

def iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if (MY_LAT-5 <= iss_latitude <= MY_LAT+5) and (MY_LONG-5 <= iss_longitude <= MY_LONG+5):
        return True

time_now = datetime.now()
hour_now = time_now.hour
minute_now = time_now.minute
day_now = time_now.day
month_now = time_now.month
date_now = f'{month_now}/{day_now}' 

response = requests.get(f'https://api.sunrise-sunset.org/json?lat={MY_LAT}&lng={MY_LONG}&formatted={format}')
response.raise_for_status()
data = response.json()
print(data)

def is_night():
    response = requests.get(f'https://api.sunrise-sunset.org/json?lat={MY_LAT}&lng={MY_LONG}&formatted={format}')
    response.raise_for_status()
    data = response.json()
    print(data)
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    jp_sunset = sunset + jp_time
    jp_sunrise = sunrise + jp_time

    if int(hour_now) >= jp_sunset or int(hour_now) <= jp_sunrise:
        return True
    


# while True:
#     sleep(60)
#     if is_night() and iss_overhead() == True:
         
#         ###------ Email Info  
#         my_email = 'Donotreplydazbot@gmail.com'
#         ps = 'awlyatnjagmrmqql'
#         receiving_email = 'zak.g.dahl@gmail.com'
#         message = f"Subject:THE ISS IS ABOVE YOU NOW! {date_now}\n\nGo outside and look now! Sent at {hour_now}:{minute_now} - {date_now}."
#         smtp_server = "smtp.gmail.com"
#         smtp_port = 587
#         connection = smtplib.SMTP(smtp_server,smtp_port)
#         simple_email_context = ssl.create_default_context()
#         ###------ Email Script   
#         with smtplib.SMTP(smtp_server,smtp_port) as connection:
#             connection.starttls(context=simple_email_context)
#             connection.login(user=my_email,password=ps)
#             connection.sendmail(from_addr=my_email,
#                                 to_addrs=receiving_email,
#                                 msg=message)
    


# BONUS: run the code every 60 seconds.



