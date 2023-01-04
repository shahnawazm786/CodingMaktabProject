import requests
import json
url="https://reqres.in/api/users?page=2"
res=requests.get(url)
print(res)