#!/usr/local/python3/bin/python3
import sys
import os
import subprocess
import shlex



nameserver = 'qk.rocketmq.rocketmq.01.poc:9876;qk.rocketmq.rocketmq.02.poc:9876'
command = '/uc/alibaba-rocketmq/bin/mqadmin'

def get_consumerProgress_data(command,namerver):
	data = subprocess.Popen(['/bin/sh',command,"consumerProgress","-n",nameserver],stdout=subprocess.PIPE)
	out=data.stdout.readlines()
	line_list = []
	for line in out:
		lines = line.strip().decode('utf-8')
		arg=shlex.split(lines)
		line_list.append(arg)
	line_list = line_list[1:-1]
	group_name_list_dict = {}
	group_name_list = []
	for group in line_list:
		group_name_list_dict[group[0]] = [group[-2],group[-1]]
	return group_name_list_dict

consumer_data = get_consumerProgress_data(command,nameserver)
consumer_group_list = []
for k in consumer_data:
	consumer_group_list.append(k)
print(consumer_group_list)	
