#!/usr/bin/env python3
__Author__ = "limugen"

import sys
import datetime
import http.cookiejar, urllib.request, urllib
from xml import etree
import requests

class ZabbixChart(object):
    def __init__(self, name, password):
        url="http://zabbix.uce.local/index.php";
        self.url = url
        self.name = name
        self.password = password
        cookiejar = http.cookiejar.CookieJar()
        urlOpener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookiejar))
        values = {"name": self.name, 'password': self.password, 'autologin': 1, "enter": 'Sign in'}
        data = urllib.parse.urlencode(values).encode(encoding='UTF8')
        request = urllib.request.Request(url, data)
        try:
            urlOpener.open(request, timeout=10)
            self.urlOpener = urlOpener
        except urllib.request.HTTPError as e:
            print(e)

    def download_chart(self, image_dir, itemids, stime, etime):
        # 此url是获取图片是的，请注意饼图的URL 和此URL不一样，请仔细观察！
        url = "http://company.monitor.com/chart.php";
        # 折线图的大小
        url_par = {}
        url_par = {"width": 1778, "height": 300, "itemids": itemids}
        # 开始日期、结束日期从str转换为datetime
        stime = datetime.datetime.strptime(stime, "%Y-%m-%d")
        etime = datetime.datetime.strptime(etime, "%Y-%m-%d")
        # 计算period
        diff_sec = etime - stime
        period = diff_sec.days * 24 * 3600 + diff_sec.seconds
        url_par["period"] = period
        # stime转换str
        stime = stime.strftime('%Y%m%d%H%M%S')
        url_par["stime"] = stime
        key = url_par.keys()
        data = urllib.parse.urlencode(url_par).encode(encoding='UTF8')
        request = urllib.request.Request(url, data)
        url = self.urlOpener.open(request)
        image = url.read()
        html = requests.get('http://zabbix.uce.local/history.php?action=showgraph&itemids[]={}'.format(itemids)).text
        page = etree.HTML(html)
        hostname_itemname = page.xpath('//div[@class="header-title"]/h1/text()')[0].split(':')
        hostname = hostname_itemname[0]
        hostname_itemname.pop(0)
        itemname = '_'.join(hostname_itemname).replace('/', '_')
        imagename = "{}\{}_{}_{}_({}).png".format(image_dir, hostname, stime, etime.strftime('%Y%m%d%H%M%S'), itemname)
        f = open(imagename, 'wb')
        f.write(image)

username = "monitor"
password = "WSX@abc321,"
stime = "2018-07-01"
etime = "2018-07-02"
image_dir = "20180726"

b = ZabbixChart(username, password)
item_list = ["28903"]

for i in item_list:
    itemids = i
    b.download_chart(image_dir,itemids,stime,etime)

