import json

import requests

url="https://reqres.in/api/users"

# Read input from json file
file=open("C:\\json_files\\employee.json","r")
json_input=file.read()
print(json_input)
requests_json=json.loads(json_input)
print(requests_json)

#hit the post api url
resp=requests.post(url,requests_json)
print(resp.status_code)

assert resp.status_code==201

print(resp.content)

#print form response header
print(resp.headers)

# Content type
print(resp.headers.get('Content-Type'))

# Content length
print(resp.headers.get('Content-Length'))

#Connection

print(resp.headers.get('Connection'))

#NEL
print(resp.headers.get('NEL'))
