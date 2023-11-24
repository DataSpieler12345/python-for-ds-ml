# read 

try:
   with open('./files/frankenstein.txt') as file:
      # print(file.read(32)) #bytes of data
      # for line in file.readlines(): # list of lines
      # for line in file.readlines()[::-1][:10][::-1]: #iterating lines
         # print(line, end ='')
         
      print(file.readline()) # 1 line by line / string
      print(file.readline()) # 2 line by line / string
      print(file.readline()) # 3 line by line / string
      print(file.readline()) # 4 line by line / string
      print(file.readline()) # 5 line by line / string
      print(file.readline()) # 6 line by line / string 
      print(file.readline()) # 7 line by line / string
      print(file.readline()) # 8 line by line / string
      print(file.readline()) # 9 line by line / string
      print(file.readline()) # 10 line by line / string
      
   
except:
   print("sorry, it was not possible to read the file.")