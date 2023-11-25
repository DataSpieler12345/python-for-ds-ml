import requests

url = 'https://httpbin.org/post' # authentication

# Query to send info to the server -> GET
# Body request to send info to the server -> POST
# Headers to send info to the server

headers = {
   'course':'Python Course',
   'version':'2.0',
   'author':'El papa'
}

params = {
   'name':'Codes'
}

data = {
   'username':'Jason',
   'password':'password123456'
}

response = requests.post(url, headers=headers, params=params, data=data)

if response.status_code == 200:
   print(response.text)