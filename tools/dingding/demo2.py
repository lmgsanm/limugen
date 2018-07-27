#!/usr/bin/env python3
__Author__ = "limugen"

from urllib import parse
from urllib import request
import json

url = 'https://oapi.dingtalk.com/robot/send?access_token=a6fb88903bfd7c1c42ba8a0b2c9418bbd423dfedb89bae64e3fe1858a9e1051d'

pagram = {
    "msgtype" : "text" ,
        "text" : {
            "content" : "there is a error"
        },
}

header = {
    "Content-Type" : 'application/json'
}

#f = requests.post(url,data=json.dumps(pagram),headers = header)
req = request.Request(url,data=json.dumps(pagram),headers = header)
res = request.urlopen(req)
ret = res.read()
print(ret)