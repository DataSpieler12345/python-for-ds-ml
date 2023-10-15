# list
list = ["football","PC",18.6,18,[6,7,10.4],True,False]
#insert 88 after football
list.insert(1,88)
# add new data to the end of the list
list.extend([True,100])                                      
# number of elements in the list
print(len(list))
# print the array 
print(list)
# Create a new list2
list2 = [200,250,"hi"]
# Concatenate the both list  
final = list + list2
# print the final list
print(final)
# number of elements in the list
print(len(final))
# print the pc element in the list | True or false 
print("PC" in list) # True
# print the football element in the list | True or false 
print("football" in list) #True
# print out the PC index of the list
print(list.index("PC")) # 2
# print out the number of PC elements in the list 
print(list.count("PC")) #1
#insert PC after PC
list.insert(1,"PC")
# print out the number of PC elements in the list 
print(list.count("PC")) #2
# print the length of the list 
print(len(list))
# print the list
print(list)
# remove 1 pc element from the list 
list.remove("PC")
#print out the list again 
print(list)
# use reverse to change the order of the elements
list.reverse()
#print out the list again 
print(list)
# order the elements ASCENDING
list3 = [1,8,2,-11,5]
print(list3.sort())
#print out the list again 
print(list3)
# order the elements descending
list3.sort(reverse=True)
#print out the list again 
print(list3)