#!/usr/bin/env python3
__Author__ = "limugen"
from urllib import request
import json
from sys import argv

access_token = "xxx"


def send_msg(mobile, item_name):
    """
     钉钉机器人API接口地址:
     https://open-doc.dingtalk.com/docs/doc.htm?spm=a219a.7629140.0.0.karFPe&treeId=257&articleId=105735&docType=1
     :param mobile:
     :param itemName:
     :return:
    """
    url = "https://oapi.dingtalk.com/robot/send?access_token=" + access_token

    data = {
        "msgtype": "text",
        "text": {
            "content": item_name
        },
        "at": {
            "atMobiles": [
                mobile
            ],
            "isAtAll": "false"
        }
    }
    # 设置编码格式
    json_data = json.dumps(data).encode(encoding='utf-8')
    print(json_data)
    header_encoding = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
                       "Content-Type": "application/json"}
    req = request.Request(url=url, data=json_data, headers=header_encoding)
    res = request.urlopen(req)
    res = res.read()
    print(res.decode(encoding='utf-8'))


if __name__ == "__main__":
    mobile = argv[1]
    item_name = argv[2]
    send_msg(mobile, item_name)