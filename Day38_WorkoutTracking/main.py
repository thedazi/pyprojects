import requests
import datetime 

# https://www.geeksforgeeks.org/python-os-environ-object/

# CONSTANTS
GENDER = 'male'
AGE = 27
WEIGHT = 78
HEIGHT = 183

nutritionix_id = 'b82e6e89'
nutritionix_key = '3fd33db7c0e2b1b8c7e7ec6947e09253'

sheets_endpoint = 'https://api.sheety.co/3a4c293e1580a57f2e8181fdd270c71c/myWorkouts/workouts'
sheets_token = 'ri34qhr430qwerkhqjwer10934857'
nutritionix_endpoint = f'https://trackapi.nutritionix.com/v2/'


nutritionix_header = {
  'x-app-id': nutritionix_id,
  'x-app-key': nutritionix_key,
  'x-remote-user-id': '0'
}

sheets_header = {
  'Authorization': f'Bearer {sheets_token}'
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

nutrition_response = requests.post(url=exercise_endpoint,json=exercise_params,headers=nutritionix_header)
print(nutrition_response.text)
nutrition_results = nutrition_response.json()

today = datetime.date.today().strftime('%d/%m/%Y')
current_time = datetime.datetime.now().strftime('%X')


for exercise in nutrition_results['exercises']:
  sheets_params = {
    'workout': {
      'date': today,
      'time': current_time,
      'exercise': exercise['name'].title(),
      'duration': exercise['duration_min'],
      'calories': exercise['nf_calories']
    }
  }

  post_workout_request = requests.post(url=sheets_endpoint, json=sheets_params, headers=sheets_header)

  print(post_workout_request.text)