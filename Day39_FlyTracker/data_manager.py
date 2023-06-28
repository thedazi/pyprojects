import requests
from flight_search import FlightSearch

class DataManager(FlightSearch):
    def __init__(self):
        super().__init__()
        self.get_destination_code
        self.data_endpoint = 'https://api.sheety.co/3a4c293e1580a57f2e8181fdd270c71c/flightData/priceData'
        
    def edit_iapa(self):
        requested_data = requests.get(url=self.data_endpoint)
        json_data = requested_data.json()
        self.destination_info = json_data['priceData']
        for city in self.destination_info:
            if city['iapaCode'] == '':
                edited_row = city['id']
                if str(self.get_destination_code(city['location'])) == 'None':
                    error_input = {
                'pricedatum': {
                    'iapaCode': 'NAMING ERROR'
                        }
                    }
                    requests.put(url=f'{self.data_endpoint}/{edited_row}',json=error_input)
                
                else:
                    iapa_input = {
                    'pricedatum': {
                        'iapaCode': self.get_destination_code(city['location'])
                        }
                    }
                    requests.put(url=f'{self.data_endpoint}/{edited_row}',json=iapa_input)
        