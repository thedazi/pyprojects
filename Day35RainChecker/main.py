import requests
import os
import math
from datetime import datetime as dt
from twilio.rest import Client

#CONSTANTS
#tokyo_arakawa lat lon
home_lat = 35.7359
home_long = 139.7835
school_lat = 35.631112
school_long = 139.784414
# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC3afb5ef7afdce4a87bdcbbb7e2cc6c62'
auth_token= '445b5b766e1143da5ad31c19a5e7cb0e'

#current time
now = dt.now()
current_time = now.strftime("%H")
current_time.replace('0','')

def get_daily_rain_info(lat,long):
  # api for weather information
  weather_request = requests.get(url=f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&hourly=precipitation_probability,is_day&current_weather=true&timezone=Asia%2FTokyo')
  weatherdata  = weather_request.json()

  # takes api info and singles out the precipitation probability
  hourly_precipitation_list = weatherdata['hourly']['precipitation_probability']

  # api nfo for LATER
  # hourly_unit = weatherdata['hourly_units']
  # current_weather = weatherdata['current_weather']
  # is_day_list = weatherdata['hourly']['is_day']


  # iterates through the first 24 hours from todays date
  
  todays_precipitation_data = [time for time in hourly_precipitation_list[7:20]]
  # test_list = [10,34,14,25,62,100,14,52,3,62,56,55,23,0,9,0,0,0,0,0,16,0,0,0]
  # todays_precipitation_data = [time for time in test_list[7:20]]

  # puts the rain times and chances into seperate list and then takes the average chance of the whole day
  will_rain_times = []
  will_rain_chance = []
  avrge_rain_chance = math.floor(sum(todays_precipitation_data[7:20])/13)
  for (index, data) in (enumerate(todays_precipitation_data)):
    if data >= 10:
      will_rain_chance.append(data)
      will_rain_times.append(index)

# dictionary conver
  will_rain_dict = {will_rain_times[x]:will_rain_chance[x] for x in range(len(will_rain_times))}
  return will_rain_dict, avrge_rain_chance
      
  

home_rain_info = get_daily_rain_info(home_lat,home_long)
school_rain_info = get_daily_rain_info(school_lat,school_long)
rain_avrge = school_rain_info[1]
specific_info = ''
for key, value in school_rain_info[0].items():
  specific_info += f"At {key+7} o'clock, there is a {value}% chance of rain.\n"
# print(specific_info,rain_avrge)


  

if rain_avrge >= 5:
  client = Client(account_sid, auth_token)
  message = client.messages.create(
    body=f'''
    With a {rain_avrge}% chance of I love you, looks like you should pack an umbrella!\n
    {specific_info}''',
    from_='+13203628468',
    to='+818053030666'
  )
  print(message.status)

    
