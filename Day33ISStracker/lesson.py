import requests

responses = requests.get(url='http://api.open-notify.org/iss-now.json')

print(responses) ### returns a response code (tells us if it succeeded or failed)
# #### the responses can be summarized as 
# 1xx = hold on 
# 2xx = success
# 3xx = go away
# 4xx = you messed up
# 5xx = server messed up
#https://www.webfx.com/web-development/glossary/http-status-codes/

print(responses.status_code)
responses.raise_for_status()  ### raises exception based on the response from the API

data = responses.json()
latitude = data['iss_position']['latitude']
longitude = data['iss_position']['longitude']
coords = (latitude,longitude)
print(coords)

sunrise_sunsetrequest = requests.get(url='https://api.sunrise-sunset.org/json?lat=35.689487&lng=139.691711&formatted=0')

sunrise_sunset_data = sunrise_sunsetrequest.json()
sunset = sunrise_sunset_data['results']['sunset'].split('T')[1].split(':')[0]
print(sunset)