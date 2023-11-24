import requests

url = 'https://httpbin.org/get?name=boing&password=123&email=boing@io.com' # the query is everything after the question mark (3 variables)
# query 

response = requests.get(url) # GET


if response.status_code == 200:
   payload = response.json()
   params = payload['args']
   
   print(params['name'])
   print(params['password'])
   print(params['email'])





