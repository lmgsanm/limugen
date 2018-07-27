#!/usr/bin/env python3
__Author__ = "limugen"

from bs4 import BeautifulSoup
from urllib import request
import re

# applications_html = "http://10.206.35.109:8081/applications.html"
# services_html = "http://10.206.35.109:8081/services.html"
# service_consumers = "http://10.206.35.109:8081/consumers.html?service=cn.uce.gis.base.api.IGisJobApi"
# service_providers = "http://10.206.35.109:8081/providers.html?service=cn.uce.gis.base.api.IGisJobApi"
# application_providers = "http://10.206.35.109:8081/providers.html?application=nos-opm-provder"
# application_consumers = "http://10.206.35.109:8081/consumers.html?application=nos-opm-provder"
# services = request.urlopen(applications_html)
# applications = request.urlopen(applications_html)
# # soup = BeautifulSoup(services)
# soup = BeautifulSoup(applications)
# #print(soup.prettify())
# print(soup)
#
# # class GetApi(object):
# #     __init__ = def(self,)
# key_word = ["applications","services","consumers","providers"]

# class Url_Handler()
#     pass
#
# class Services_Handler():
#     def __init__(self,services):
#         self.services = services
#
#     def getServicesName(self):
#



# class Applications_Handler():
#     pass

#
# def getUrl(url,page):
#     url = '/'.join([url,page])
#     return url


# if __name__ == "__main__":
# dubbo_moitor_url = "http://10.206.35.109:8081"
# applications_page = "applications.html"
# services_page = "services.html"
# applications_html = getUrl(dubbo_moitor_url,applications_page)
# services_html = getUrl(dubbo_moitor_url, services_page)
# print(applications_html)
# print(services_html)
# applications = request.urlopen(applications_html)
# print(applications)
# services = request.urlopen(services_html)
# print(services)
# applications_bs4 = BeautifulSoup(applications,"html.parser").find_all(href=re.compile("application"))
# #print(applications_bs4)
# for app_desc in applications_bs4:
#     # app = app_desc.strip().split(' ')
#     # print(app_desc.name)
#     # print(app)
#     print(type(app_desc))
#     print(app_desc.title)


# services_html = "http://10.206.35.109:8081/services.html"
# service_req = request.urlopen(services_html)
# bs4_service = BeautifulSoup(service_req,"html5lib")
# #print(bs4_service.find_all('td'))
#
# for application in bs4_service.find_all('td'):
#     print(application.get("href"))
#
# applications_html = "http://10.206.35.109:8081/applications.html"
# services_html = "http://10.206.35.109:8081/services.html"
# service_consumers = "http://10.206.35.109:8081/consumers.html?service=cn.uce.gis.base.api.IGisJobApi"
# service_providers = "http://10.206.35.109:8081/providers.html?service=cn.uce.gis.base.api.IGisJobApi"
# application_providers = "http://10.206.35.109:8081/providers.html?application=nos-opm-provder"
# application_consumers = "http://10.206.35.109:8081/consumers.html?application=nos-opm-provder"
# service_req = request.urlopen(application_consumers)
# #print(BeautifulSoup(service_req,"html5lib"))
# with open("application_consumers.html",'w') as f:
#     f.write(str(BeautifulSoup(service_req,"html5lib")))
