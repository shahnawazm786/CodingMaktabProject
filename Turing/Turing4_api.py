import json

import requests
import jsonpath

url="https://reqres.in/api/users?page=2"
res=requests.get(url)
print(res.content)

#parse response to json path

json_response=json.loads(res.text)
print(json_response)

#find the pages
pages=jsonpath.jsonpath(json_response,"total_pages")
print(pages[0])

assert pages[0] == 2