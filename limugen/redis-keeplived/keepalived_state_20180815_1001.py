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
    if len(data) == 0:
        result = data
    if len(data) == 1:
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
redis_vip_info = get_vip_addr_info(vip)
#print(redis_status)
#print(redis_role)
#print(redis_vip_info)
redis_info = ["Redis server is avaliable!","Redis server is not running!",
            "there is a virtual ip address(172.16.2.99) on Redis server!","there is not virtual ip address(172.16.2.99) on Redis server!",
            "Redis server is on master mode!","Redis server is on slave mode!"]

if redis_status_flag in redis_status: ##判断redis是否存活，如果存活，再判断redis的角色是master还是slave
    file_write(' '.join([current_time,redis_info[0]]),redis_keepalived_log_path) ## 如果存活，打印存活信息
    if redis_role == redis_role_flag: ##判断redis角色为master
        file_write(' '.join([current_time,redis_info[4]]),redis_keepalived_log_path) ##打印当前redis角色名称：master
        if vip in redis_vip_info: ##判断该服务器是否配置了VIP
            file_write(' '.join([current_time,redis_info[2]]),redis_keepalived_log_path) ##如果配置了VIP,打印存在vip信息
        else:
            file_write(' '.join([current_time,redis_info[3]]),redis_keepalived_log_path) ##没有配置vip，打印不存在vip的信息
            set_vip_addr(vip)  #给该服务器配置vip(因为该redis的角色是master，所以必须配置vip映射到该master服务器上)
    else: ##该服务器的redis角色为slave
        file_write(' '.join([current_time,redis_info[5]]),redis_keepalived_log_path) ##打印slave角色信息到指定文件
        if vip in redis_vip_info:##redis角色为slave但是已经配置了vip
            file_write(' '.join([current_time,redis_info[2]]),redis_keepalived_log_path) ## 打印vip信息到指定文件
            del_vip_addr(vip)
        else: ##redis角色为slave，没有配置vip
            file_write(' '.join([current_time,redis_info[3]]),redis_keepalived_log_path) ## 打印vip信息到指定文件

else: ##redis服务处于宕机状态
    file_write(' '.join([current_time,redis_info[1]]),redis_keepalived_log_path) ##打印宕机状态到指定文件
    if vip in get_vip_addr_info(vip):##判断该服务器配置了vip
        file_write(' '.join([current_time,redis_info[2]]),redis_keepalived_log_path) ## 打印vip信息到指定文件
        del_vip_addr(vip)
    else:##该服务没有配置vip
        file_write(' '.join([current_time,redis_info[3]]),redis_keepalived_log_path) ## 打印vip信息到指定文件
