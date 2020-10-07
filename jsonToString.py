import json
import requests

res = requests.get("http://dummy.restapiexample.com/apio/v1/employess/")
data = json.loads(res.text)
data = json.dumps(data)
print(data)
print(type(data))
input()
