import requests

url = 'https://httpbin.org/post' # authentication


data = {
   'username': 'Cobra', # body requests
   'password': 'password123'
}

response = requests.post(url, data=data) # send info to the server


if response.status_code == 200:
   payload = response.json()
   print(response.text)
   
   print(response.url)   

