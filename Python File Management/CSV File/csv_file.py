import csv 

try: 
   with open('./files/nutzers.csv') as file:
      
      reader = csv.reader(file) # to iterate over 
      
      next(reader) # jumping from the first line
      
      for row in reader:
         name = row[4] #column name
         user_name = row[0]
         email = row[2]
         # print(row) # List
         # print(type(row))
         print(name, user_name, email)

except:
   print("sorry, it was not possible to complete the operation.")