# coding=gbk
#!/usr/bin/env python3

__Author__="limugen"
import json
import urllib.request
import sys
import time
import csv
import os

headers = {"User-Agent" : "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11",
            "Content-Type" : "application/json",
            "Charset" : "utf8"
            }
# """
# csv_head = ["IP地址","模块名称","所属集群","最小内存使用率","平均内存使用率","最大内存使用率","最小CPU使用率","平均CPU使用率","最大CPU使用率","最大磁盘使用率","平均磁盘使用率","最小磁盘使用率","硬件配置","ESTABLISHED","CLOSE_WAIT","TIME_WAIT","LISTEN",]
# csv_dict = {"ip":["ip","module_name_value","culster_numer_value","memery_min_value","memery_avg_value","memery_max_value",
#     "cpu_min_value","cpu_avg_value","cpu_max_value",
#     "disk_min_value","disk_avg_value","disk_max_value",
#      "hardware_value",
#     "tcp_established_value","tcp_close_wait_value","tcp_time_wait_value","tcp_listen_value"]}
# """

#write csv_dict to monitor.csv
# monitor_file = "服务器监控.csv"
# csv_head = ["IP地址","模块名称","所属集群","最小内存使用率","平均内存使用率","最大内存使用率","最小CPU使用率","平均CPU使用率","最大CPU使用率","最大磁盘使用率","平均磁盘使用率","最小磁盘使用率","硬件配置","ESTABLISHED","CLOSE_WAIT","TIME_WAIT","LISTEN",]
# csv_dict_demo = {"ip":["ip","module_name_value","culster_numer_value","memery_min_value","memery_avg_value","memery_max_value",
#     "cpu_min_value","cpu_avg_value","cpu_max_value",
#     "disk_min_value","disk_avg_value","disk_max_value",
#      "hardware_value",
#     "tcp_established_value","tcp_close_wait_value","tcp_time_wait_value","tcp_listen_value"]}
#with open(monitor_file,'w',newline='',encoding='utf-8') as csvfile:
# with open(monitor_file,'w',newline='') as csvfile:
#     csvfile_write = csv.writer(csvfile)
#     csvfile_write.writerow(csv_head)
#     for key in csv_dict_demo:
#         csvfile_write.writerow(csv_dict_demo[key])

def get_host(group):
    host_dict = {}
    api = "http://10.205.56.124/api"
    url = "http://10.205.56.124/api/gethostbygroup/?groupname=ics&grouptype=projectteam"
    req = urllib.request.Request(url=url,headers=headers)
    req_result = urllib.request.urlopen(req)
    return req_result
print(get_host(teest))