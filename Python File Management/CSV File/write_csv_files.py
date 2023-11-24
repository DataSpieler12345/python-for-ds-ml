import csv 

columns = [
   "username","password","email","creation_date","name"
]

try: 
   with open('./files/nutzers.csv', 'a') as file:
      
      
      writer = csv.DictWriter(file, fieldnames=columns)
      # writer.writerows # add multiple lines at the end of the file
      writer.writerow( #add a new line at the end of the file
         {
            'username':'mitrozone', 'password':'_.NoData', 'email':'mitrozone@io.com', 'creation_date':2023-11-24, 'name':'bond'
         }
      )
      

except:
   print("sorry, it was not possible to complete the operation.")