import json
import requests


#API url
url="https://reqres.in/api/users?page=2"
res=requests.get(url)
print(res)
#print headers
print(res.headers)
#print response body or content
print(res.content)
assert res.status_code == 200

