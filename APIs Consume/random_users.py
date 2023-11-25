import requests

url = 'https://randomuser.me/api/'

count = int(input('enter the number of users: '))
response = requests.get(url, params = {'results': count})


if response.status_code == 200:
   
   payload = response.json()
   results = payload.get('results')
   
   for user in results:
      name = user.get('name') #dictionary
      
      print("{title} {first} {last}".format(**name))
      
      