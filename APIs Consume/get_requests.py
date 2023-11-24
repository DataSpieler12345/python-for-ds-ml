import requests

url = 'https://httpbin.org/get'

response = requests.get(url) # GET
print(response) # code 200 = Success
print(response.status_code) # code 200 = Success
print(response.text) # answer text / info / string
print(type(response.text)) #string type
# print(response.json()) # json object
payload = response.json() # store response as a json object
print(payload.get('origin')) # Dictionary

print(response.url) # to get the route from