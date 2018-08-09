#!/usr/local/python3/bin/python3

import sys
import os
import datetime
import requests
import urllib
import time
import json

ftp_url = "ftp://10.205.63.94"
sys_code = sys.argv[1]
update_version = sys.argv[2]
war_version= sys.argv[3]

download_base_url="/uc/version/updatefiles"

module_name = ["uce-uop-job","uce-uop-main","uce-uop-mq","uce-uop-provider","uce-uop-web"]



#step download wars
#def get_module_name(sys_code):
#    headers = {"User-Agent" : "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11", 
#                "Content-Type" : "application/json",
#                "Charset" : "utf8"
#                }
#    url = '='.join(["http://10.205.56.124/api/getgnbypt/?projectteam",sys_code])
#    req = urllib.request.Request(url=url,headers=headers)
#    req_result = urllib.request.urlopen(req).read().decode('utf-8')
#    req_data = json.loads(req_result)
#    return req_data

def get_war_name(module_name,war_version):
    war_name = '-'.join([module_name,'.'.join([war_version,"war"])])
    return war_name

def get_war_path(url,sys_code,update_version,filename):
    war_download_url = '/'.join([url,sys_code,update_version,filename])
    return war_download_url
   
def get_update_dir(url,sys_code,update_version):
    update_dir = '/'.join([url,sys_code,update_version])
    return update_dir
    
os.makedirs(get_update_dir(download_base_url,sys_code,update_version),exist_ok=True)

for module in module_name:
    war_name = get_war_name(module,war_version)
    war_download_url = get_war_path(ftp_url,sys_code,update_version,war_name)
    war_update_path= get_war_path(download_base_url,sys_code,update_version,war_name)
    try:
        print("now,start to download {}".format(war_name))
        urllib.request.urlretrieve(war_download_url,war_update_path) 
        print("{0} is finished download!!".format(war_name))
        print("#####################################################")
    except urllib.error.ContentTooShortError as error:
        print(error)

#prepare update version
update_version_base_dir = "/uc/version"
os.makedirs(get_update_dir(update_version_base_dir,sys_code,update_version),exist_ok=True)


