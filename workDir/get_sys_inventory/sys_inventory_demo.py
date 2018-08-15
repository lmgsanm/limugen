#!/usr/bin/env python3
__Author__ = "limugen"
import urllib.request
import urllib
import pymysql.cursors
import sys
import time
import os
import json
import datetime
import csv

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

if __name__ == "__main__":
    sys_code = ["ucb","qk","ucp","wx","omg","uop","ubs","prs","gis","nos","oms"]
    # hostgroup = "ics"
    # for hostgroup in sys_code:
    #     host_info_data_dict = get_host_info(hostgroup)
    # print(host_info_data_dict)
    fieldnames = ['IP地址', '模块名称','主机名']
    csv_dict = {}
    with open('inventory.csv','w') as csvfile:
        writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
        csv_dict = {}
        for hostgroup in sys_code:
            host_info_data_dict = get_host_info(hostgroup)
            for ip in host_info_data_dict:
                writer.writerow({'IP地址': ip, '模块名称': host_info_data_dict.get(ip)[0],'主机名':host_info_data_dict.get(ip)[1]})
