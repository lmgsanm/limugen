#!/usr/bin/env python3
__Author__ = "limugen"
import requests
import json

url = "http://10.205.56.119/"

r = requests.get(url,auth=('monitor','WSX@abc321,'))
# print(r.status_code)
# print(r.headers)
# print(r.text)
print(r.text)

data = requests.get(url,)