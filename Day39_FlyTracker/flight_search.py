import requests

FLIGHT_ENDPOINT = 'https://api.tequila.kiwi.com'
FLIGHT_API = '7_aT4AF0J7HATRMoJpylyVcS8SW8bnr3'

class FlightSearch:
    def get_destination_code(self, city_name):
        location_endpoint = f'{FLIGHT_ENDPOINT}/locations/query'
        flight_header = {
           'apikey': FLIGHT_API 
        }

        flight_params = {
            'term': city_name,
            'location_types': 'airport',
            'limit': '2'
        }
        
        location_data = requests.get(url=location_endpoint,params=flight_params,headers=flight_header)
        for data in location_data.json()['locations']:
            return data['code']
        