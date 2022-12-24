import json

import jsonpath
import requests


url="https://reqres.in/api/users/2"


resp=requests.delete(url)

# fetch the response code

print(resp.status_code)

assert

