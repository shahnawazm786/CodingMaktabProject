import json

import jsonpath
import requests


url="https://reqres.in/api/users/2"


resp=requests.get(url)

#json_response=json.load(resp.text)

#json_path = jsonpath.jsonpath(json_response,"total_pages")

