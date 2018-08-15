#!/usr/bin/env python3

import sys
import os
import shlex
import datetime
import time

vip = "172.16.2.99/24"
eth = "eth0"
redis_home = "/usr/local/redis"
redis_passwd = "test"
redis_status_flag = "PONG"
redis_role_flag = "master"
redis_keepalived_log_path = '/'.join([redis_home,"var","logs","Redis_keepalived_status.log"])

def get_cmd_data_result(cmd):
    data = cmd.readlines()
    if data == None:
        result = []
    else:
        result = shlex.split(data[0])
    return result

def get_vip_addr_info(ip):
    cmd_data = os.popen("/sbin/ip addr list | grep " + ip)
    result_list = get_cmd_data_result(cmd_data)
    return result_list

def set_vip_addr(ip):
    os.popen("/sbin/ip addr add " + ip + " dev " + eth)


def del_vip_addr(ip):
    os.popen("/sbin/ip addr del " + ip + " dev " + eth)

def get_redis_status(cmd):
    cmd_data = os.popen(redis_home + "/bin/redis-cli " + "-a " + redis_passwd + " " + cmd )
    result_list = get_cmd_data_result(cmd_data)
    return result_list

def get_redis_role(cmd):
    cmd_data = os.popen(redis_home + "/bin/redis-cli " + "-a " + redis_passwd + " " + cmd  + "|" + "grep " + "role" )
    result_list = get_cmd_data_result(cmd_data)
    return result_list

def file_write(data,file):
    with open(file,'a+') as f:
        f.write(data + "\n")

current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
redis_status = get_redis_status("PING")
redis_role = get_redis_role("INFO")[0].split(":")[1]
redis_info = ["Redis server is avaliable!","Redis server is not running!",
            "there is a virtual ip address(172.16.2.99) on Redis server!","there is not virtual ip address(172.16.2.99) on Redis server!",
            "Redis server is on master mode!","Redis server is on slave mode!"]

if redis_status_flag in redis_status:
    file_write(' '.join([current_time,redis_info[0]]),redis_keepalived_log_path)
    if redis_role == redis_role_flag:
        file_write(' '.join([current_time,redis_info[4]]),redis_keepalived_log_path)
        if vip in get_vip_addr_info(vip):
            file_write(' '.join([current_time,redis_info[2]]),redis_keepalived_log_path)
        else:
            file_write(' '.join([current_time,redis_info[3]]),redis_keepalived_log_path)
            set_vip_addr(vip)
    else:
        file_write(' '.join([current_time,redis_info[5]]),redis_keepalived_log_path)
        if vip in get_vip_addr_info(vip):
            file_write(' '.join([current_time,redis_info[2]]),redis_keepalived_log_path)
        else:
            file_write(' '.join([current_time,redis_info[3]]),redis_keepalived_log_path)
            del_vip_addr(vip)

else:
    file_write(' '.join([current_time,redis_info[1]]),redis_keepalived_log_path)
    if vip in get_vip_addr_info(vip):
        file_write(' '.join([current_time,redis_info[2]]),redis_keepalived_log_path)
    else:
        file_write(' '.join([current_time,redis_info[3]]),redis_keepalived_log_path)
        del_vip_addr(vip)
