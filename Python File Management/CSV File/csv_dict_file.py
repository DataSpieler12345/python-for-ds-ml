import csv 

try: 
   with open('./files/nutzers.csv') as file:
      # reader -> list
      # DictReader -> dict
      reader = csv.DictReader(file) # to iterate over 
      
      for row in reader:
         print(
            row.get('name'),
            #row['name'],
            row['email'],
            row['username'])
      

except:
   print("sorry, it was not possible to complete the operation.")