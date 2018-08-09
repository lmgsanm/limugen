#!/usr/local/python3/bin/python3

import sys
import os
import datetime
import requests
import urllib
import time
import json
import threading
import zipfile
import shutil


ftp_url = "ftp://10.205.63.94"
# sys_code = sys.argv[1]
# update_version = sys.argv[2]
# war_version= sys.argv[3]
sys_code = 'uop'
update_version = '20180809-26-383'
war_version= '1.0.1'
updatefiles_base_dir = "/uc/updatefiles"
versions_base_dir = "/uc/versions"
module_name = ["uce-uop-job","uce-uop-main","uce-uop-mq","uce-uop-provider","uce-uop-web"]
ignorefiles_base_dir = "/uc/ignorefiles"
ignore_files_dict = {"WEB-INF/classes":["disconf.properties","logback.xml","spring-conf.xml"]
                     }

#step download wars and prepare update version

def get_war_name(module_name,war_version):
    war_name = '-'.join([module_name,'.'.join([war_version,"war"])])
    return war_name

def get_war_path(url,sys_code,update_version,filename):
    war_download_url = '/'.join([url,sys_code,update_version,filename])
    return war_download_url
   
def get_update_dir(url,sys_code,update_version):
    update_dir = '/'.join([url,sys_code,update_version])
    return update_dir
   
def get_update_moudle_dir(url,sys_code,update_version,module_name):
    update_dir = '/'.join([url,sys_code,update_version,module_name])
    return update_module_dir

updatefiles_dir = '/'.join([updatefiles_base_dir,sys_code,update_version])
ignorefiles_dir = '/'.join([ignorefiles_base_dir,sys_code])

os.makedirs(updatefiles_dir,exist_ok=True)
os.makedirs(ignorefiles_dir,exist_ok=True)

for module in module_name:
    print("开始准备#################################模块 （{0}） 升级包#################################+++start".format(module))
    war_name = get_war_name(module,war_version)
    war_download_url = '/'.join([ftp_url,sys_code,update_version,war_name])
    war_path= '/'.join([updatefiles_base_dir,sys_code,update_version,war_name])
    war_version_path= '/'.join([versions_base_dir,sys_code,update_version,module])
    os.makedirs(war_version_path,exist_ok=True)
    try:
        print("开始下载 ########################### {0} ############################ ".format(war_name))
        urllib.request.urlretrieve(war_download_url,war_path)
        print("下载########################### {0} ###########################完毕".format(war_name))
    except urllib.error.ContentTooShortError as error:
        print(error)
    print("开始解压 ########################### {0} ############################ ".format(war_name))
    war_zip = zipfile.ZipFile(war_path)
    war_zip.extractall(war_version_path)
    print("解压########################### {0} ############################完毕".format(war_name))
    print("开始替换###################### {0} ################################# 配置文件".format(war_name))
    for key in ignore_files_dict:
            for file_name in ignore_files_dict.get(key)[:]:
                war_file_name_path = '/'.join([war_version_path,key,file_name])
                ignore_file_name_path = '/'.join([ignorefiles_dir,file_name])
                shutil.copyfile(ignore_file_name_path,war_file_name_path)
    print("替换###################### {0} ################################# 配置文件完毕".format(war_name))
    shutil.make_archive('_'.join([war_version_path,update_version]),"gztar",war_version_path)
    print("准备#################################模块 （{0}） 升级包#################################完毕+++stop\n".format(module))



