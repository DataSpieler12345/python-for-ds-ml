#Create a list
names = ['Harry','Tom','Jone','Jane','Teddy']
#We can print the first element
print(names[0])
#And we can add a name
names.append("Emily")
#And another
names.append("Tom")
#But now we have two toms, let's remove one
names = list(set(names))
#We converted to a set then back to a list, to remove any duplicates
print(names)
#But note these are now out of order