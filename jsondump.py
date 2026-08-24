import json

student = {
    "name": "Rahul",
    "marks": 85
}

json_string = json.dumps(student)

print(json_string)
print(type(json_string))