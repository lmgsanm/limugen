#!/usr/local/python3/bin/python3

import sys
import os
import datetime
import requests
import urllib
import time

ftp_url = "ftp://10.205.63.94"
sys_code = sys.argv[1]
#sys_code = "uop"
update_version = sys.argv[2]
#update_version = "20180809-25-382"

war_version="1.0.1"
module_name = ["uce-uop-job","uce-uop-main","uce-uop-mq","uce-uop-provider","uce-uop-web"]
download_base_url="/uc/version/updatefiles"

class WarDownload(object):
    def __init__(self,download_url,file_dir,sys_code,war_version,update_version,module_name)
        self.download_url = download_url
        self.file_dir = file_dir
        self.sys_code = sys_code
        self.war_version = war_version
        self.update_version = update_version
        self.module_name = module_name

    def get_war_name(self.module_name,self.war_version):
        war_name = '-'.join([self.module_name,'.'.join([self.war_version,"war"])])
        return war_name

    def get_war_path(self.url,self.sys_code,self.update_version,filename):
        war_download_url = '/'.join([url,sys_code,update_version,filename])
        return war_download_url
       
    def get_update_dir(url,sys_code,update_version):
        update_dir = '/'.join([url,sys_code,update_version])
        return update_dir
        
    os.makedirs(get_update_dir(download_base_url,sys_code,update_version),exist_ok=True)
    war_download_url_list = [] 
    for module in module_name:
        war_name = get_war_name(module,war_version)
        war_download_url = get_war_path(ftp_url,sys_code,update_version,war_name)
        war_update_path= get_war_path(download_base_url,sys_code,update_version,war_name)
        print("now,start to download {}".format(war_name))
        urllib.request.urlretrieve(war_download_url,war_update_path) 
        print("{0} is finished download!! \n".format(war_name))
        print("#####################################################")
