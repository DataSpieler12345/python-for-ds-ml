# Create a Dictionary

dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
phone_numbers = {'jefe': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}
 
print(dictionary)
print(phone_numbers)
print(empty_dictionary)



#The following code safely searches for French words:

dictionary = {"cat": "cat", "dog": "chien", "horse": "cheval"}
words = ['cat', 'lion', 'horse']
 
for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "is not in the dictionary")
        
        
# Key Methods

dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
for key in dictionary.keys():
    print(key, "->", dictionary[key])
    
    
# Key Methods / second way  

dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
for spanish, french in dictionary.items():
    print(spanish, "->", french)
    
    
# Modifying, adding and deleting values Assigning a new value to an existing key is straightforward - because dictionaries are fully mutable, there are no obstacles to modifying them.

# We are going to replace the value "chat" with "minou", which is not very appropriate, but will work for our example.

dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
dictionary['gato'] = 'minou'
print(dictionary)

# Adding new keys to dictionary
dictionary['cisne'] = 'cygne'
print(dictionary)

#deleting a key from dictionary
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
del dictionary['perro']
print(dictionary)

#deleting the last element of the dictionary
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
dictionary.popitem()
print(dictionary)
