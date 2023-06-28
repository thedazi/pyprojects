import requests

class FlightData:
    def __init__(self) -> None:
        self.data_endpoint = 'https://api.sheety.co/3a4c293e1580a57f2e8181fdd270c71c/flightData/priceData'
        self.data_output()
        
    def data_output(self):
        requested_data = requests.get(url=self.data_endpoint)
        json_data = requested_data.json()
        completed_data = json_data['priceData']
        for data in completed_data:
            self.location = data['location']
            self.iapa = data['iapaCode']
            self.price = data['price']