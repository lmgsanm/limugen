#!/usr/bin/env python3
__Author__ = "limugen"

import csv
import sys
import os

first_line = ["IP地址","模块名称","所属集群","最小内存使用率","平均内存使用率","最大内存使用率","最小CPU使用率","平均CPU使用率","最大CPU使用率","最大磁盘使用率","平均磁盘使用率","最小磁盘使用率","硬件配置","ESTABLISHED","CLOSE_WAIT","TIME_WAIT","LISTEN",]

monitor_dict = {"ip":["ip","module_name_value","culster_numer_value","memery_min_value","memery_avg_value","memery_max_value",
                        "cpu_min_value","cpu_avg_value","cpu_max_value",
                        "disk_min_value","disk_avg_value","disk_max_value",
                        "hardware_value",
                        "tcp_established_value","tcp_close_wait_value","tcp_time_wait_value","tcp_listen_value"],
                    "ip2":["ip2","module_name_value","memery_min_value","memery_avg_value","memery_max_value",
                        "cpu_min_value","cpu_avg_value","cpu_max_value",
                        "disk_min_value","disk_avg_value","disk_max_value",
                        "hardware_value",
                        "tcp_established_value","tcp_close_wait_value","tcp_time_wait_value","tcp_listen_value"]}



with open('some.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(first_line)
    for ip in monitor_dict:
        writer.writerow(monitor_dict[ip])



