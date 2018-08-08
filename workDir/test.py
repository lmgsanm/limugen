#!/usr/bin/env python3
__Author__ = "limugen"

__Author__="limugen"
import urllib.request
import urllib
import pymysql.cursors
import sys
import time
import os
import json
import datetime
import docx
from pyzabbix import ZabbixAPI

# def get_host_graph_url(graphid,period,stime):
#     zabbix_graph_url = 'http://10.205.56.119/chart2.php'
#     zabbix_graph__request_url = zabbix_graph_url + "?graphid=" + graphid + "&period=" + period + "&isNow=0&stime=" + stime
#     return zabbix_graph__request_url
#
# graph_url = get_host_graph_url("8849","8849","20180711113356")
# name = "test.png"
# urllib.request.urlretrieve(graph_url,name)

nowtime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
print(nowtime)