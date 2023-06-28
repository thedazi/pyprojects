#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from pprint import pprint
import requests
import pygsheets


data_endpoint = 'https://api.sheety.co/3a4c293e1580a57f2e8181fdd270c71c/flightData/priceData'

requested_data = requests.get(url=data_endpoint)
json_data = requested_data.json()
print(json_data)

# flight_params = {
#   'term': 'Oslo',
#   'location_types': 'airport',
#   'limit': '2'
# }


# test = requests.get(url=flight_location,params=flight_params,headers=flight_header)
# for data in test.json()['locations']:
#   print(data['code'])

# data_manager = DataManager()
# data_manager.edit_iapa()


# flight_data = FlightData()
# print(f"{flight_data.location}: ${flight_data.price}")
# searcher = FlightSearch()
# print(str(searcher.get_destination_code('Miyako-jima')))