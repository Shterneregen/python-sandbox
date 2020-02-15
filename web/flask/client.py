# pip install requests
from pprint import pprint

import requests

response = requests.get('http://127.0.0.1:5000/history')
pprint(response.json())

response = requests.post('http://127.0.0.1:5000/send', json={"username": "Nick", "text": "Hello"})
pprint(response)

response = requests.get('http://127.0.0.1:5000/history')
pprint(response.json())
