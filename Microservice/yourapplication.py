import requests
import json

c1 = [
        '[ ] Wristband',
        '[ ] Camping Pass',
        '[ ] Sunscreen',
        '[ ] Standard clothes',
        '[ ] Warm clothes',
]

json_data = json.dumps(c1)
headers = {'Content-Type': 'application/json'}
response = requests.get('http://127.0.0.1:5000/data', data=json_data, headers=headers).json()
#response = requests.get('http://127.0.0.1:5000/data_load', data=json_data, headers=headers).json()

print(response)