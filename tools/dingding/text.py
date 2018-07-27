#!/usr/bin/env python3
__Author__ = "limugen"

import json
from urllib import request
from urllib import parse

url = 'https://oapi.dingtalk.com/robot/send?access_token=a6fb88903bfd7c1c42ba8a0b2c9418bbd423dfedb89bae64e3fe1858a9e1051d'

print = {
     "msgtype": "text",
     "text": {
         "content": "我就是我,  @1825718XXXX 是不一样的烟火"
     },
     "at": {
         "atMobiles": [
             "1825718XXXX"
         ],
         "isAtAll": false
     }
 }