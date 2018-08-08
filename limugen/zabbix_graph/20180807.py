#!/usr/bin/env python3
__Author__ = "limugen"
#
# import pymysql
#
# def get_mysql_data(sql):
#     host = "10.205.34.251"
#     user = "readonly"
#     password = "!@1234read"
#     db = "zabbix"
#     charset='utf8mb4'
#     connection = pymysql.connect(host=host,user=user,password=password,db=db,charset=charset,cursorclass=pymysql.cursors.DictCursor)
#     try:
#         with connection.cursor() as cursor:
#             sql = sql
#             cursor.execute(sql)
#             result = cursor.fetchall()
#             return result
#     finally:
#         connection.close()
#
# def get_item_data(ip,zabbix_key):
#     sql = "select itemid from items where hostid in ( select hostid from hosts where host = \'" + ip + "\' ) AND key_ = \'" + zabbix_key + "\'"
#     item_id = get_mysql_data(sql)
#     return item_id
#     # sql = "SELECT i.hostid,itemid,i. NAME,key_,i.description FROM items i JOIN HOSTS h ON i.hostid = h.hostid WHERE h. HOST =" + "\'" + ip + "\'"
#     # return sql
#
# # print(get_mysql_data(get_item_data('10.205.53.228')))
# # print(get_item_data('10.205.53.228'))
# # mysql_data = get_mysql_data(get_item_data('10.205.53.228'))
# itemid = get_item_data("10.205.53.228","cpu.usage")
# print(itemid[0].get("itemid"))


#!/usr/bin/env python3
# coding=gbk
__Author__="limugen"
__data__ = "2018/8/7"

import sys
import datetime
import http.cookiejar
import urllib
import urllib.request
from lxml import etree
import requests

class ZabbixChart(object):
    def __init__(self,name,password):
        url = "http://10.205.56.119/index.php"
        self.url = url
        self.name = name
        self.password = password
        cookiejar = http.cookiejar.CookieJar()
        urlOpener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookiejar))
        values = {"name":self.name,"password":self.password,"authlogin":1,"enter":"Sign in"}
        data = urllib.parse.urlencode(values).encode(encoding='UTF8')
        request = urllib.request.Request(url,data)
        try:
            urlOpener.open(request,timeout=10)
            self.urlOpener = urlOpener
        except urllib.request.HTTPError as e:
            print(e)

    def download_chart(self,image_dir,itemids,stime,etime):
        url = "http://10.205.56.119/chart.php";
        url_par = {}
        url_par = {"width": 1778, "height": 300, "itemids": itemids}
        stime = datetime.datetime.strptime(stime, "%Y-%m-%d")
        etime = datetime.datetime.strptime(etime, "%Y-%m-%d")
        diff_sec = etime - stime
        period = diff_sec.days * 24 * 3600 + diff_sec.seconds
        url_par["period"] = period
        time = stime.strftime('%Y%m%d%H%M%S')
        url_par["stime"] = stime
        key = url_par.keys()
        data = urllib.parse.urlencode(url_par).encode(encoding='UTF8')
        request = urllib.request.Request(url, data)
        url = self.urlOpener.open(request)
        image = url.read()
        html = requests.get('http://10.205.56.119/history.php?action=showgraph&itemids[]={}'.format(itemids)).text
        page = etree.HTML(html)
        hostname_itemname = page.xpath('//div[@class="header-title"]/h1/text()')[0].split(':')
        hostname = hostname_itemname[0]
        hostname_itemname.pop(0)
        itemname = '_'.join(hostname_itemname).replace('/', '_')
        imagename = "{}\{}_{}_{}_({}).png".format(image_dir, hostname, stime, etime.strftime('%Y%m%d%H%M%S'), itemname)
        f = open(imagename, 'wb')
        f.write(image)

if __name__ == "__main__":
    username = "xinysu"
    password = "passwd"

    stime = "2017-09-01"
    etime = "2017-10-01"
    image_dir = "./"
    b = ZabbixChart(username, password)
    # item_list = (
    # 35295, 35328, 38080, 37992, 38102, 38014, 35059, 35022, 42765, 35024, 35028, 35035, 35036, 35044, 35045, 35046,
    # 35047, 38248, 36369, 36370, 36371, 36372)
    item_list = (29459,29484,29485,29490)
    for i in item_list:
        itemids = i
        b.download_chart(image_dir, itemids, stime, etime)



