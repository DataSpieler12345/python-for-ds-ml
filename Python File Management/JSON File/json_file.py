import json

data = {
    "name": "John Doe",
    "age": 25,
    "average": 8.5,
    "active": True,
    "email": "johndoe@example.com",
    "courses": ["python", "mongodb", "flask"],
    "address": {
        "code": "12345",
        "country": "USA"
    }
}


# Convert JSON object to a string
json_string = json.dumps(data)

# Print JSON string with single quotes
# print(json_string)

user = json.loads(json_string) # Dict

print(user['email'])
print(user['courses'])