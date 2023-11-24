import requests

url = 'https://httpbin.org/get' # the query is everything after the question mark (3 variables)
# query 

params = {
   'name':'boing',
   'password':'123',
   'email':'boing@io.com'
}

response = requests.get(url,params=params) # GET + params

if response.status_code == 200:
   payload = response.json()
   params = payload['args']
   
   print(params['name'])
   print(params['password'])
   print(params['email'])
   
   print(response.url)
