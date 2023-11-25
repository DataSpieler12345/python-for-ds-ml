import requests
from setting import *

url = 'https://github.com/login/oauth/access_token'

params = {
   'client_id': client_id,
   'client_secret': secret_id,
   'code': code,
}

headers = {
   'Accept': 'application/json'
}

response = requests.post(url, params=params, headers=headers)

if response.status_code == 200:
   print(response.json())