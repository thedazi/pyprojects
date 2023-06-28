import requests
import datetime 

# CONSTANTS
GENDER = 'male'
AGE = 27
WEIGHT = 78
HEIGHT = 183

nutritionix_id = 'b82e6e89'
nutritionix_key = '3fd33db7c0e2b1b8c7e7ec6947e09253'
nutritionix_endpoint = f'https://trackapi.nutritionix.com/v2/'

sheets_endpoint = 'https://api.sheety.co/3a4c293e1580a57f2e8181fdd270c71c/weightliftingRecord/chestTri'


exercise_response = requests.get(url=sheets_endpoint)
json_exercise_response = exercise_response.json()
for exercises in json_exercise_response['chestTri']:
  print(exercises)

nutritionix_header = {
  'x-app-id': nutritionix_id,
  'x-app-key': nutritionix_key,
  'x-remote-user-id': '0'
}

exercise_text = input('What exercise did you do? ')

exercise_endpoint = f'{nutritionix_endpoint}natural/exercise'

exercise_params = {
  'query': exercise_text,
  'gender': GENDER,
  'weight_kg': WEIGHT,
  'height_cm': HEIGHT,
  'age': AGE
}
