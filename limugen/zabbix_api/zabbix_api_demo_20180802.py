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

item_id = '29459'
host_id = '10263'
time_till = time.mktime(datetime.now().timetuple())
time_from = time_till - 60 * 60 * 4

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
for point in history:
    print(point['value'])
