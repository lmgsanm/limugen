#!/usr/bin/env python3

from pyzabbix import ZabbixAPI

zapi = ZabbixAPI("http://zabbix.uce.local")
zapi.login("monitor", "WSX@abc321,")
#print("Connected to Zabbix API Version %s" % zapi.api_version())

#for h in zapi.hostgroup.get(output="extend",hostids="10263",itemids='29459'):
for h in zapi.graph.get(output="extend",itemids='29459'):
        print(h['graphid'])
