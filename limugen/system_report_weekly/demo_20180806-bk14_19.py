#!/usr/bin/env python3
# coding=gbk
__Author__="limugen"
import urllib.request
import pymysql.cursors
import sys
import time
#import csv
import os
import json
from pyzabbix import ZabbixAPI
from datetime import datetime

django_headers = {"User-Agent" : "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11",
            "Content-Type" : "application/json",
            "Charset" : "utf8"
            }
"""
csv_head = ["IP��ַ","ģ������","������Ⱥ","��С�ڴ�ʹ����","ƽ���ڴ�ʹ����","����ڴ�ʹ����","��СCPUʹ����","ƽ��CPUʹ����","���CPUʹ����","������ʹ����","ƽ������ʹ����","��С����ʹ����","Ӳ������","ESTABLISHED","CLOSE_WAIT","TIME_WAIT","LISTEN",]
csv_dict = {"ip":["ip","module_name_value","culster_numer_value","memery_min_value","memery_avg_value","memery_max_value",
    "cpu_min_value","cpu_avg_value","cpu_max_value",
    "disk_min_value","disk_avg_value","disk_max_value",
     "hardware_value",
    "tcp_established_value","tcp_close_wait_value","tcp_time_wait_value","tcp_listen_value"]}
"""

#write csv_dict to monitor.csv
monitor_file = "���������.csv"
csv_head = ["IP��ַ","ģ������","������Ⱥ","��С�ڴ�ʹ����","ƽ���ڴ�ʹ����","����ڴ�ʹ����","��СCPUʹ����","ƽ��CPUʹ����","���CPUʹ����","������ʹ����","ƽ������ʹ����","��С����ʹ����","Ӳ������","ESTABLISHED","CLOSE_WAIT","TIME_WAIT","LISTEN",]
csv_dict_demo = {"ip":["ip","module_name_value","culster_numer_value","memery_min_value","memery_avg_value","memery_max_value",
    "cpu_min_value","cpu_avg_value","cpu_max_value",
    "disk_min_value","disk_avg_value","disk_max_value",
     "hardware_value",
    "tcp_established_value","tcp_close_wait_value","tcp_time_wait_value","tcp_listen_value"]}


def get_json_data(url):
    headers = {"User-Agent" : "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11",
                "Content-Type" : "application/json",
                "Charset" : "utf8"
                }
    req = urllib.request.Request(url=url,headers=headers)
    req_result = urllib.request.urlopen(req).read().decode('utf-8')
    req_data = json.loads(req_result)
    return req_data

#with open(monitor_file,'w',newline='') as csvfile:
#    csvfile_write = csv.writer(csvfile)
#    csvfile_write.writerow(csv_head)
#    for key in csv_dict_demo:
#        csvfile_write.writerow(csv_dict_demo[key])
#
def get_group_info(group):
    host_dict = {}
    api = "http://10.205.56.124/api"
    api_url = '/'.join(["gethostbygroup",'='.join(["?groupname",'&'.join([])])])
    parament_last = '&'.join(['='.join(["?groupname",group]),"grouptype=projectteam"])
    parament_url = '/'.join(["gethostbygroup",parament_last])
    api_url = '/'.join([api,parament_url])
    host_info = []
    json_data = get_json_data(api_url)
    return json_data

def get_mysql_data(sql):
    host = "10.205.34.251"
    user = "readonly"
    password = "!@1234read"
    db = "zabbix"
    charset='utf8mb4'
    connection = pymysql.connect(host=host,user=user,password=password,db=db,charset=charset,cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            sql = sql
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    finally:
        connection.close()

#def get_graph(graphid,hostid,itemid):
#def get_graph():
#    url = "http://zabbix.uce.local/api_jsonrpc.php"
#    headers = {"User-Agent" : "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11",
#                "Content-Type" : "application/json-rpc",
#                "Charset" : "utf8"
#                }
#    parameter = {"jsonrpc":"2.0","method":"graph.get","id":1,"auth":"06b8fc69d4b665d2c5aca7cf8d8a480d",
#                "params":{ "output": "extend", "hostids":"10.205.71.55","sortfield": "name"
#                    }
#                 }
#
#    req = urllib.request.Request(url=url,data=parameter,headers=headers)
#    req_result = urllib.request.urlopen(req).read().decode('utf-8')
#    req_data = json.loads(req_result)
#    

def get_host_info(group_name):
    group_list = get_group_info(group_name)
    host_info_dict = {}
    for host in group_list:
        ip = host["ipaddr"]
        hostname = host["hostname"]
        cpu = host["cpu"]
        memory = host["memory"]
        disk = host["disk"]
        host_api_url = '='.join(["http://10.205.56.124/api/getgroupbyhost/?ipaddr",str(ip)])
        addr_json = get_json_data(host_api_url)
        module_name = addr_json[0]["groupname"]
        host_info_list = [module_name,hostname,cpu,memory,disk]
        host_info_dict[ip] = host_info_list
    return host_info_dict

def get_zabbix_data(item_id):
    zabbix_server = "http://10.205.56.119"
    zabbix_user = "monitor"
    zabbix_password = "WSX@abc321,"
    item_id = item_id
    zabbix_api = ZabbixAPI(zabbix_server)
    zabbix_api.login(zabbix_user,zabbix_password)
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
                time_till = time_till,
                time_from = time_from,
                output = 'extend',
                limit = '5000',
                history = 0
                )
    value = []
    for point in history:
        value.append(point["value"])
#    return value
    num = len(value)
    sum = 0
    for i in value:
        sum = sum + float(i)
    value_max = max(value)
    value_average = float(round(float(sum)/float(num)))
    return value_average,value_max

def get_item_data(ip,zabbix_key):
    #item_id = get_mysql_data("select itemid from items where hostid in ( select hostid from hosts where host='10.205.53.228')  AND key_ = 'cpu.usage'")
    #sql = "select itemid from items where hostid in ( select hostid from hosts where host = \'" + ip + "\') AND key_ = " + '\zabbix_key\'"
    sql = "select itemid from items where hostid in ( select hostid from hosts where host = \'" + ip + "\' ) AND key_ = \'" + zabbix_key + "\'"
    #print(sql)
    #sys.exit()
    item_id = get_mysql_data(sql)
    return item_id

if __name__ == "__main__":
    hostgroup = sys.argv[1]
    zabbix_server = "http://10.205.56.119"
    zabbix_user = "monitor"
    zabbix_password = "WSX@abc321,"
    host_info_dict = get_host_info(hostgroup)
    #monitor_keys = [ 'cpu.usage','vm.memory.usage','vfs.fs.size[{#FSNAME},used]','tcp.status["CLOSE_WAIT"]','tcp.status["ESTABLISHED"]','tcp.status["TIME_WAIT"]']
    #monitor_keys = [ 'cpu.usage','vm.memory.usage','vfs.fs.size[{#FSNAME},total]','tcp.status["CLOSE_WAIT"]','tcp.status["ESTABLISHED"]','tcp.status["TIME_WAIT"]']
    #monitor_keys = [ 'cpu.usage','vm.memory.usage','vfs.fs.size[{#FSNAME},pfree]','tcp.status["CLOSE_WAIT"]','tcp.status["ESTABLISHED"]','tcp.status["TIME_WAIT"]']
    monitor_keys = [ 'cpu.usage','vm.memory.usage','tcp.status["CLOSE_WAIT"]','tcp.status["ESTABLISHED"]','tcp.status["TIME_WAIT"]']
    #print(host_info_dict)
    #print(len(host_info_dict))
    #print(host_info_dict.get("10.205.71.71"))
    #for ip in host_info_dict.keys():
    for ip in host_info_dict:
        for monitor_key in monitor_keys:

            item_id = get_item_data(ip,monitor_key)
            itemid = item_id[0].get("itemid")
            zabbix_data = get_zabbix_data(itemid)
            print(itemid,zabbix_data)
           # sys.exit()
            #print(get_item_data(item_id))
        #    print(ip,item_id)
#            print(ip,get_item_data(ip,monitor_key))
#        print(ip,get_item_data(ip,"cpu.usage"))

