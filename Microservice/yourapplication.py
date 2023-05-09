import requests
import json

c1 = [
        '[ ] Wristband',
        '[ ] Camping Pass',
        '[ ] Sunscreen',
]

json_data = json.dumps(c1)
headers = {'Content-Type': 'application/json'}
#response = requests.post('http://127.0.0.1:5000/data_save', data=json_data, headers=headers).json()
response = requests.get('http://127.0.0.1:5000/data_get', data=json_data, headers=headers).json()

print(response)