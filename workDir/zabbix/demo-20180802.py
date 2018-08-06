#!/usr/bin/env python3
__Author__ = "limugen"
from urllib import request
from urllib import parse
import json
#
#
# zabbix_url = "http://zabbix.uce.local/api_jsonrpc.php"
# # zabbix_url = "http://10.205.56.119/api_jsonrpc.php"
# headers = {"User-Agent" : "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11",
#           "Content-Type" : "application/application/json-rpc",
#           "Charset" : "utf8"
#           }
#
# data = {"jsonrpc":"2.0",
#         "method":"user.login",
#         "params":{
#             "user": "monitor",
#             "password": "WSX@abc321,"
#                 },
#         "id": 1,
#         "auth": 'null'
#         }
# # data = {"jsonrpc":"2.0","method":"apiinfo.version"," ":1,"auth":'null',"params":{}}
#
# def getUrlData(url,data,hearders):
#     data = parse.urlencode(data).encode('utf-8')
#     req = request.Request(url,headers=headers,data=data)
#     html = request.urlopen(req).read().decode('utf-8')
#     return html
#
# print(getUrlData(zabbix_url,data,headers))
#
# # send_data = json.dumps(data).encode("utf-8")
# # req = request.Request(zabbix_url,send_data,headers)
# # print(request.urlopen(req))


from pyzabbix import ZabbixAPI
from datetime import datetime
import time


zabbix_server = "http://10.205.56.119"
zabbix_user = "monitor"
zabbix_password = "WSX@abc321,"

zabbix_api = ZabbixAPI(zabbix_server)
zabbix_api.login(zabbix_user,zabbix_password)

item_id = '29459'
time_till = time.mktime(datetime.now().timetuple())
time_from = time_till - 60 * 60 * 24 * 7

history = zabbix_api.history.get(itemids=[item_id],
                                 time_till = time_till,
                                 time_from = time_from,
                                 output = 'extend',
                                 limit = '5000',
                                 )

if not len(history):
    history = zabbix_api.history.get(itemids=[item_id],
                                     time_till=time_till,
                                     time_from=time_from,
                                     output='extend',
                                     limit='5000',
                                     history = 0
                                     )
for point in history:
#     print("{0}: {1}".format(datetime.fromtimestamp(int(point['clock']))
# .strftime("%x %X"), point['value']))
    print(point['value'])

