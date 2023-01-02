import requests
import json

url="http://ip.jsontest.com/"
response=requests.get(url)
print(response)
assert response.status_code == 200

print(response.headers)
print(response.headers.get("Content-Type"))
content=response.headers.get("Content-Type")
assert  content== 'application/jsons'

