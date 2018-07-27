#!/usr/bin/env python3
__Author__ = "limugen"

from urllib import request
from urllib import parse
import json

url = 'http://fanyi.baidu.com/v2transapi'
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
}
values = {
    'from': 'zh',
    'to': 'en',
    'query': '死肥猪',
    'transtype': 'translang',
    'simple_means_flag': '3'
}

# data = parse.urlencode(values).encode('utf-8')
# request = request.Request(url, data, headers)
# html = request.urlopen(request).read().decode('utf-8')
# print(json.loads(html)['trans_result']['data'][0]['dst'])

data = parse.urlencode(values).encode('utf-8')
reqt = request.Request(url,data,headers)
html = request.urlopen(reqt).read().decode('utf-8')
# print(json.loads(html)['trans_result']['data'][0]['dst'])
print(json.loads(html))