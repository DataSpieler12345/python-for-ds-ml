import json

# principal functions
# dumps = allows the generation of a json object from a dictionary
# loads = allows the generation of a dictionary from a json object

user = {
   'name': 'Cody',
   'email': 'info@io.com',
   'courses': [
      {'id': 1, 'title': 'Python'},
      {'id': 2, 'title': 'Django'},
      {'id': 3, 'title': 'Flask'}
   ]
}

# Convert JSON object to a string
json_string = json.dumps(user)

print(json_string)
print(type(json_string))
