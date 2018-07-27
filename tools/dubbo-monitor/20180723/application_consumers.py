#!/usr/bin/env python3
__Author__ = "limugen"


from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

url = "http://10.206.35.109:8081/consumers.html?service=cn.uce.gis.base.api.IGisJobApi"
html = BeautifulSoup(urlopen(url),"html5lib")
print(html)

# def open_file_handler(f):
#     fd = open(f,'r')
#     return fd
#
# html_doc_name = "application_consumers.html"
# html_doc = open_file_handler(html_doc_name)
# # print(html_doc)
# soup = BeautifulSoup(open_file_handler(html_doc_name),"html5lib")
# print(soup)
# consumer_list = soup.find_all("td").find_all("button")
# print(consumer_list)
# # applications_consumers = soup.find_all(href=re.compile("consumers"))
# # applications_providers = soup.find_all(href=re.compile("providers"))
# # applications_list = []
# # for consumers in applications_consumers:
# #     applications_list.append(consumers)
# #
# # for providers in applications_providers:
# #     applications_list.append(providers)
# # # print(len(applications_list))
# # applications = []
# # for tags in applications_list:
# #     # print(tags["href"])
# #     #print(tags.string)
# #     #print(tags["href"].split("?")[1].split("=")[1],tags.contents[0])
# #     application = tags["href"].split("?")[1].split("=")[1]
# #     applications.append(application)
# #
# # # print(applications)
# # application = set(applications)
# # print(len(application))
