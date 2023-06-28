import requests
from datetime import datetime, date

pixela_endpoints = 'https://pixe.la/v1/users'
USERNAME = 'dazi'
TOKEN = 'v13489vhnyf879234bh189fkjsefh810'
ID = 'studygraph1'

today = date.today()
today_date_formatted = str(today.strftime('%Y%m%d'))


# https://pixe.la/v1/users/dazi/graphs/studygraph1.html

# user_params = {
#   'token': TOKEN,
#   'username': USERNAME,
#   'agreeTermsOfService': 'yes',
#   'notMinor': 'yes'
# }




# my page
# https://pixe.la/@dazi

pixela_graph_create_endpoint = f'{pixela_endpoints}/{USERNAME}/graphs'

headers = {
  'X-USER-TOKEN': TOKEN
}

graph_params = {
  'id': ID,
  'name': 'Japanese Study Tracker',
  'unit': 'minutes',
  'type': 'int',
  'color': 'momiji'
}


pixela_graph_createpoint_endpoint = f'{pixela_endpoints}/{USERNAME}/graphs/{ID}'

graph_edit_params = {
  'date': today_date_formatted,
  'quantity': '120'
}

editdate = today_date_formatted

pixela_graph_editpoint_endpoint = f'{pixela_endpoints}/{USERNAME}/graphs/{ID}/20230506'

graph_editpoint_params = {
  'quantity': '120'
}

        #!!!! be sure to differentiate commands, post is for new content and put is for editing and delete is for deleting#
response = requests.put(url=pixela_graph_editpoint_endpoint,json=graph_editpoint_params,headers=headers)
print(response.text)

deletedate = '20230507'

pixela_graph_editpoint_endpoint = f'{pixela_endpoints}/{USERNAME}/graphs/{ID}/{deletedate}'

# delete_response = requests.delete(url=pixela_graph_editpoint_endpoint,headers=headers)
# print(delete_response.text)