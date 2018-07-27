
__Author__ = "limugen"

import sys
import subprocess
import os
from urllib import parse

class Url_Operation:
    def __init__(self,download_url,deploy_version,sys_module):
        self.download_url = download_url
        self.deploy_version = deploy_version
        self.sys_module = sys_module

    def url_get(self):
        return parse.urljoin(self.download_url,self.deploy_version,self.sys_module)

    def file_download(self):
        pass

class Deploy_Prerequisites:
    pass
    def war_backup(self):
        pass

    def version_prepare(self):
        pass
    def softlink_check(self):
        pass
class Deploy_runner:
    passs
    def nginx_operation(self):
        pass
    def tomcat_stop(self):
        pass
    def version_relace(self):
        pass

    def tomcat_start(self):

class Class Nginx_Operaton:
    pass


if "__name__" == "__main__":
    pass