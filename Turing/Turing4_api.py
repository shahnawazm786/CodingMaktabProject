import json

import requests
import jsonpath

url="https://reqres.in/api/users?page=2"
res=requests.get(url)
print(res.content)

#parse response to json path

json_response=json.loads(res.text)
print(json_response)
