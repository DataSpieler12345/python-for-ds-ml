import csv

columns = [
   "username", "password", "email", "creation_date", "name"
]

try:
   with open('./files/courses.csv', 'w', newline='') as file:
      writer = csv.DictWriter(file, fieldnames=columns)
      writer.writeheader()
      
      writer.writerows(
         [
            {'username': 'pythondev', 'password': '12345_6589lak', 'email': 'pythondevs@pormi.io', 'creation_date': '2023', 'name': 'bond'},  
            {'username': 'pythonent', 'password': '12345_654789k', 'email': 'pythondevs@porma.io', 'creation_date': '2023', 'name': 'james'},
            {'username': 'pythonfront', 'password': '145_654789lak', 'email': 'pythondevs@pormes.io', 'creation_date': '2023', 'name': 'boo'}, 
            {'username': 'pythonweb', 'password': '12654789lak', 'email': 'pythondevs@pormil.io', 'creation_date': '2023', 'name': 'boni'}, 
         ]
      )
   
except Exception as err:
   print(err)
   print("Sorry, it was not possible to complete the operation.")