import json

import requests

ur="https://reqres.in/api/users"

# Read input from json file
file=open("C:\\json_files\\employee.json","r")
json_input=file.read()
print(json_input)
requests_json=json.load(json_input)
print(requests_json)
