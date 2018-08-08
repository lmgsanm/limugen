#!/usr/bin/env python3
# coding=gbk
__Author__ = "limugen"
from pyzabbix import ZabbixAPI
from datetime import datetime
import time

zabbix_server = "http://10.205.56.119"
zabbix_user = "monitor"
zabbix_password = "WSX@abc321,"
zapi = ZabbixAPI(zabbix_server)
zapi.login(zabbix_user,zabbix_password)

item_id = '29459'
host_id = '10280'
time_till = time.mktime(datetime.now().timetuple())
time_from = time_till - 60 * 60
#
# history = zapi.graph.get(hostids = [host_id],
#                             # time_from = time_from,
#                             # time_till = time_till,
#                             # output = 'extend',
#                             # limit = '5000',
#                             )
# history = zapi.graphitem.get(itemids = [item_id],
#                             # time_from = time_from,
#                             # time_till = time_till,
#                             output = 'extend',
#                             limit = '5000',
#                             )
history = zapi.history.get(hostids = [host_id],
                            itemids = [item_id],
                            time_from = time_from,
                            time_till = time_till,
                            output = 'extend',
                            limit = '5000',
                            )

# print(history[0].get("graphid"))
#
print(history)


# print(history)
# for dict in history:
#     for k in dict:
#         if "Disk space usage" in dict.get(k):
#             # print(dict.get('graphid'))
#             print(dict.get('itemid'))