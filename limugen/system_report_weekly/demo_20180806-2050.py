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
import docx

django_headers = {"User-Agent" : "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11",
            "Content-Type" : "application/json",
            "Charset" : "utf8"
            }
"""
csv_head = ["IP地址","模块名称","所属集群","最小内存使用率","平均内存使用率","最大内存使用率","最小CPU使用率","平均CPU使用率","最大CPU使用率","最大磁盘使用率","平均磁盘使用率","最小磁盘使用率","硬件配置","ESTABLISHED","CLOSE_WAIT","TIME_WAIT","LISTEN",]
csv_dict = {"ip":["ip","module_name_value","culster_numer_value","memery_min_value","memery_avg_value","memery_max_value",
    "cpu_min_value","cpu_avg_value","cpu_max_value",
    "disk_min_value","disk_avg_value","disk_max_value",
     "hardware_value",
    "tcp_established_value","tcp_close_wait_value","tcp_time_wait_value","tcp_listen_value"]}
"""

#write csv_dict to monitor.csv
monitor_file = "服务器监控.csv"
csv_head = ["IP地址","模块名称","所属集群","最小内存使用率","平均内存使用率","最大内存使用率","最小CPU使用率","平均CPU使用率","最大CPU使用率","最大磁盘使用率","平均磁盘使用率","最小磁盘使用率","硬件配置","ESTABLISHED","CLOSE_WAIT","TIME_WAIT","LISTEN",]
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
    #time_from = time_till - 60 * 60 * 24 * 7
    time_from = time_till - 60 * 60 * 24
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
    value_temp = []
    for point in history:
        value_temp.append(point["value"])
    num = len(value_temp)
    sum = 0
    for i in value_temp:
        sum = sum + float(i)
    value_temp_max = max(value_temp)
    value_temp_average = float(round(float(sum)/float(num),3))
    value_list = [value_temp_max,value_temp_average]
    return value_list

def get_host_monitor_data(host_info_dict,monitor_keys):
    host_monitor_data_dict = {}
    for ip in host_info_dict:
        zabbix_data_list = []
        for monitor_key in monitor_keys:
            item_id = get_item_data(ip,monitor_key)
            itemid = item_id[0].get("itemid")
            zabbix_data = get_zabbix_data(itemid)
            zabbix_data_list.extend(zabbix_data)
        host_monitor_data_dict[ip] = zabbix_data_list
    return host_monitor_data_dict

def get_item_data(ip,zabbix_key):
    sql = "select itemid from items where hostid in ( select hostid from hosts where host = \'" + ip + "\' ) AND key_ = \'" + zabbix_key + "\'"
    item_id = get_mysql_data(sql)
    return item_id

if __name__ == "__main__":
    hostgroup = sys.argv[1]
    monitor_keys = [ 'cpu.usage','vm.memory.usage','tcp.status["CLOSE_WAIT"]','tcp.status["ESTABLISHED"]','tcp.status["TIME_WAIT"]']
    host_info_head_list = ["序号","IP地址","模块名称","主机名","CPU","内存","磁盘"]
    host_monitor_head_list = ["序号","IP地址","CPU平均使用率","CPU最大使用率","内存平均使用率","内存最大使用率","TCP-CLOSE_WAIT连接数","TCP-ESTABLISHED连接数","TCP-TIME_WAIT连接数"]
    host_info_data_dict = get_host_info(hostgroup)
    host_monitor_data_dict = get_host_monitor_data(host_info_data_dict,monitor_keys)
    
    doc = docx.Document()

    host_info_data_list = []
    for seq,ip in enumerate(host_info_data_dict,start=1):
        host_info_data_list.append([seq,ip,host_info_data_dict.get(ip)])
    host_info_rows = len(host_info_data_list) + int(1)
    host_info_columns = len(host_info_head_list)
    host_info_table = doc.add_table(rows=host_info_rows, cols=host_info_columns, style='Table Grid')
    for row in range(host_info_rows):
        if row == 0:
            host_info_cells = host_info_table.rows[0].cells
            host_info_cells[0].text = host_info_head_list[0]
            host_info_cells[1].text = host_info_head_list[1]
            host_info_cells[2].text = host_info_head_list[2]
            host_info_cells[3].text = host_info_head_list[3]
            host_info_cells[4].text = host_info_head_list[4]
            host_info_cells[5].text = host_info_head_list[5]
            host_info_cells[6].text = host_info_head_list[6]
        elif row == 1:
    
    doc.save('temp.docx')
