#!/usr/bin/env python3
# coding=gbk
from pyzabbix import ZabbixAPI
from datetime import datetime
import time

zabbix_server = "http://10.205.56.119"
zabbix_user = "monitor"
zabbix_password = "WSX@abc321,"
zapi = ZabbixAPI(zabbix_server)
zapi.login(zabbix_user,zabbix_password)

item_id = '34454'
time_till = time.mktime(datetime.now().timetuple())
time_from = time_till - 60 * 60 * 24 * 7

history = zapi.history.get(itemids = [item_id],
                            time_from = time_from,
                            time_till = time_till,
                            output = 'extend',
                            limit = '5000',
                            )

if not len(history):
    history = zapi.history.get(itemids = [item_id],
                                time_from = time_from,
                                time_till = time_till,
                                output = 'extend',
                                limit = '5000',
                                history = '0',
                                )
value_temp = []
for point in history:
    value_temp.append(int(point["value"]))
    num = len(value_temp)
    sum = 0
    for i in value_temp:
        sum = sum + float(i)
    value_temp_max = float(max(value_temp))
    value_temp_average = float(round(float(sum) / float(num), 3))
    value_list = [value_temp_average, value_temp_max]
# print(value_list)
print(value_temp)
print(max(value_temp))
print(min(value_temp))
