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
    return data_text
def data_image(data_image):
    data_image = {
        "msgtype": "image",
        "image": {
            "media_id": data_image
        }
    }

data_voice = {
    "msgtype": "voice",
    "voice": {
       "media_id": "MEDIA_ID",
       "duration": "10"
    }
}

def data_file(data_file):
    data_file = {
        "msgtype": "file",
        "file": {
           "media_id": data_file
        }
    }
def data_link(messageUrl,picUrl,title,text):
    data_link = {
        "msgtype": "link",
        "link": {
            "messageUrl": messageUrl,
            "picUrl":picUrl,
            "title": title,
            "text": text
        }
    }

data_oa = {
     "msgtype": "oa",
     "oa": {
        "message_url": "http://dingtalk.com",
        "head": {
            "bgcolor": "FFBBBBBB",
            "text": "头部标题"
        },
        "body": {
            "title": "正文标题",
            "form": [
                {
                    "key": "姓名:",
                    "value": "张三"
                },
                {
                    "key": "年龄:",
                    "value": "20"
                },
                {
                    "key": "身高:",
                    "value": "1.8米"
                },
                {
                    "key": "体重:",
                    "value": "130斤"
                },
                {
                    "key": "学历:",
                    "value": "本科"
                },
                {
                    "key": "爱好:",
                    "value": "打球、听音乐"
                }
            ],
            "rich": {
                "num": "15.6",
                "unit": "元"
            },
            "content": "大段文本大段文本大段文本大段文本大段文本大段文本大段文本大段文本大段文本大段文本大段文本大段文本",
            "image": "@lADOADmaWMzazQKA",
            "file_count": "3",
            "author": "李四 "
        }
    }
}

data_markdown = {
    "msgtype": "markdown",
    "markdown": {
        "title": "首屏会话透出的展示内容",
        "text": "# 这是支持markdown的文本 \n## 标题2  \n* 列表1 \n![alt 啊](https://img.alicdn.com/tps/TB1XLjqNVXXXXc4XVXXXXXXXXXX-170-64.png)"
    }
}
data_ActionCard_all = {
    "msgtype": "action_card",
    "action_card": {
        "title": "是透出到会话列表和通知的文案",
        "markdown": "支持markdown格式的正文内容",
        "single_title": "查看详情",
        "single_url": "https://open.dingtalk.com"
    }
}

data_ActionCard_simple = {
    "msgtype": "action_card",
    "action_card": {
        "title": "是透出到会话列表和通知的文案",
        "markdown": "支持markdown格式的正文内容",
        "btn_orientation": "1",
        "btn_json_list": [
            {
                "title": "一个按钮",
                "action_url": "https://www.taobao.com"
            },
            {
                "title": "两个按钮",
                "action_url": "https://www.tmall.com"
            }
        ]
    }
}


ding_hook = "https://oapi.dingtalk.com/robot/send?access_token=2ee5e76cbb22d8ba52d61d69b2379f139789f74b999dd9caebee1aa5f68d12ad"
message = "for a test"
send_data = json.dumps(data_text(message)).encode("utf-8")  #发送文字
# send_data = json.dumps(data_file("./demo.py")).encode("utf-8")  #发送文件
# messageUrl = "http://s.dingtalk.com/market/dingtalk/error_code.php"
# picUrl = "@lALOACZwe2Rk"
# title = "测试"
# text = "测试"
#send_data = json.dumps(data_link(messageUrl,picUrl,title,text)).encode("utf-8")  ##link
req = request.Request(ding_hook,send_data,header)
request.urlopen(req)
# request.urlopen(req).read().decode('utf-8')
# html = request.urlopen(req).read().decode('utf-8')
# print(json.loads(html))