#!/usr/bin/env python3
__Author__ = "limugen"

import yaml
import sys
#
with open('../conf/system.yaml') as f:
    data = yaml.load(f)
    print(data)

# document = """
#   a: 1
#   b:
#     c: 3
#     d: 4
# """
# #print(yaml.dump(yaml.load(document)))
# print(yaml.load(document))

    modules = data.get('modules').keys()
    print(modules)
    # for key,value in modules:
    #     print(key,value)
    for module in modules:
        ips = data.get('modules').get(module)
        print(module,ips)
    sys_code = data.get('syscode')
    print(sys_code)
    # apps_home, tomcat_home, backup_home, version_home = data.get('dest_path')
    # print(data.get('dest_path'))
    # print(apps_home)
    # print(apps_home.split(':')[-1])
    # for home in data.get('dest_path'):
    #     apps_home = home.split(':')[-1]
    #     tomcat_home

    apps_home = data.get('dest_path')[0].split(':')[-1]
    tomcat_home = data.get('dest_path')[1].split(':')[-1]
    backup_home = data.get('dest_path')[2].split(':')[-1]
    version_home = data.get('dest_path')[3].split(':')[-1]
    print(apps_home, tomcat_home, backup_home, version_home)

    wars_home = data.get('local_path')[0].split(':')[-1]
    operation_home = data.get('local_path')[1].split(':')[-1]
    staic_home = data.get('local_path')[2].split(':')[-1]
    print(wars_home, operation_home, staic_home)


# sys_code,deploy_version,sys_operation = sys.argv[1:4]
# print(sys_code,deploy_version,sys_operation)

# import urllib.request
from urllib import request
#
# urllib.request.urlretrieve()

request.urlretrieve("http://10.205.63.94/wars/ics/20180706-101-127/ics-srv-1.0.0.war")
import shutil
shutil.make_archive()

import zipfile
zipfile.ZipFile
