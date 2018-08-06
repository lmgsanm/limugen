#!/usr/bin/env python3
__Author__ = "limugen"

from pyzabbix import ZabbixAPI
from datetime import datetime
import time

url = "http://zabbix.uce.local"
username = "monitor"
password = "WSX@abc321,"

zapi = ZabbixAPI(url)
zapi.login(username, password)
# print("Connected to Zabbix API Version %s" % zapi.api_version())

item_id = '155413'
host_id = "10260"
graph_id = "12079"

# Create a time range
time_till = time.mktime(datetime.now().timetuple())
time_from = time_till - 60 * 60 * 24 * 7  # 4 hours

# Query item's history (integer) data
history = zapi.history.get(
                           # itemids=[item_id],
                           hostids=[host_id],
                           # graphids=[graph_id],
                           time_from=time_from,
                           time_till=time_till,
                           output='extend',
                           limit='5000',
                           )

# If nothing was found, try getting it from history (float) data
if not len(history):
    history = zapi.history.get(
                               # itemids=[item_id],
                               hostids=[host_id],
                               # graphids=[graph_id],
                               time_from=time_from,
                               time_till=time_till,
                               output='extend',
                               limit='5000',
                               history=0,
                               )

# Print out each datapoint
for point in history:
    print("{0}: {1}".format(datetime.fromtimestamp(int(point['clock']))
.strftime("%x %X"), point['value']))
