import json

try:
   with open('./files/users.json') as file:
      payload = json.load(file)
      users = payload['users'] # to iterate over users
      
      for user in users:
         print(user['name'], '-', user['age'])
      
except:
   print("we are sorry we are unable to complete the operation")