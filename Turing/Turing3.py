import json
import requests


#API url
url="https://reqres.in/api/users?page=2"
res=requests.get(url)
print(res)

