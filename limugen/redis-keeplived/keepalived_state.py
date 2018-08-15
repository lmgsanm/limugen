#!/usr/bin/env python3
"""
该脚本需要配置到定时任务中，执行间隔视sentinel.conf 配置文件中sentinel failover-timeout而定，如sentinel.conf
中配置是10000，即10s，则定时任务最好每10秒执行一次，配置如下
* * * * * /usr/local/python3/bin/python3 /uc/bin/keepalived_state.py 2>&1 /dev/null
* * * * * sleep 10 && /usr/local/python3/bin/python3 /uc/bin/keepalived_state.py 2>&1 /dev/null
* * * * * sleep 20 && /usr/local/python3/bin/python3 /uc/bin/keepalived_state.py 2>&1 /dev/null
* * * * * sleep 30 && /usr/local/python3/bin/python3 /uc/bin/keepalived_state.py 2>&1 /dev/null
* * * * * sleep 40 && /usr/local/python3/bin/python3 /uc/bin/keepalived_state.py 2>&1 /dev/null
* * * * * sleep 50 && /usr/local/python3/bin/python3 /uc/bin/keepalived_state.py 2>&1 /dev/null
"""
import sys
import os
import shlex
import datetime
import time

vip = "172.16.2.99/24"  ##keealived 的虚拟ip地址，从keepalived.conf中配置项virtual_ipaddress中配置
eth = "eth0"    ##服务器配置该vip的以太网卡名称
redis_home = "/usr/local/redis"  ##redis安装路径
redis_passwd = "test" ## redis密码
redis_status_flag = "PONG" ##用于判断redis存活状态
redis_role_flag = "master" ##用于判断redis的角色是master还是slave
redis_keepalived_log_path = '/'.join([redis_home,"var","logs","Redis_keepalived_status.log"])  ##日志输出路径

#通过传入执行命令，获取执行结果
def get_cmd_data_result(cmd):
    data = cmd.readlines()
    if len(data) == 0:
        result = data
    if len(data) == 1:
        result = shlex.split(data[0])
    return result

#通过输入虚拟IP（vip）地址，判断该IP是否已经配置在服务器上
def get_vip_addr_info(ip):
    cmd_data = os.popen("/sbin/ip addr list | grep " + ip)
    result_list = get_cmd_data_result(cmd_data)
    return result_list

#设置虚拟IP（vip）地址到该服务器上
def set_vip_addr(ip):
    os.popen("/sbin/ip addr add " + ip + " dev " + eth)

#删除该服务器上已经配置了的虚拟IP（vip）地址
def del_vip_addr(ip):
    os.popen("/sbin/ip addr del " + ip + " dev " + eth)

#通过执行shell命令获取redis存活状态
def get_redis_status(cmd):
    cmd_data = os.popen(redis_home + "/bin/redis-cli " + "-a " + redis_passwd + " " + cmd )
    result = get_cmd_data_result(cmd_data)
    if len(result) == 0:
        result_list = []
    if len(result) == 1:
        result_list = result
    return result_list

#通过执行shell命令获取redis服务器的角色名称
def get_redis_role(cmd):
    cmd_data = os.popen(redis_home + "/bin/redis-cli " + "-a " + redis_passwd + " " + cmd  + "|" + "grep " + "role" )
    result = get_cmd_data_result(cmd_data)
    if len(result) == 0:
        result_list = []
    if len(result) == 1:
        result_list = result[0].split(":")[1]
    return result_list

#写入日志
def file_write(data,file):
    with open(file,'a+') as f:
        f.write(data + "\n")

current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
redis_status = get_redis_status("PING")
redis_role = get_redis_role("INFO")
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
