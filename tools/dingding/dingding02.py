#!/usr/bin/env python3
__Author__ = "limugen"

from urllib import request
import json


header = {"User-Agent" : "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11",
          "Content-Type" : "application/json",
          "Charset" : "utf8"
          }

def data_text (content):
    data_text = {
        "msgtype": "text",
        "text": {
            "content": content
        }
    }
    return data_tex


ding_hook = "https://oapi.dingtalk.com/robot/send?access_token=2ee5e76cbb22d8ba52d61d69b2379f139789f74b999dd9caebee1aa5f68d12ad"
message = "for a test"
send_data = json.dumps(data_text(message)).encode("utf-8")

req = request.Request(ding_hook,send_data,header)
request.urlopen(req)
