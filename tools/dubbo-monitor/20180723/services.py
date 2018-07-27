#!/usr/bin/env python3
__Author__ = "limugen"

from bs4 import BeautifulSoup
import re
def open_file_handler(f):
    fd = open(f,'r')
    return fd

html_doc_name = "services.html"
html_doc = open_file_handler(html_doc_name)
#print(type(html_doc))
soup = BeautifulSoup(open_file_handler(html_doc_name),"html5lib")
#print(soup)
# service_tag = soup.find_all(href=re.compile("service"))
# print(service_tag)
services_consumers = soup.find_all(href=re.compile("consumers"))
services_providers = soup.find_all(href=re.compile("providers"))
# print(services_consumers)
services_list = []
for consumers in services_consumers:
    services_list.append(consumers)
#
for providers in services_providers:
    services_list.append(providers)
# print(len(services_list))
#print(services_list)
services = []
for tags in services_list:
    # print(tags["href"])
    #print(tags.string)
    # print(tags["href"].split("?")[1].split("=")[1],tags.contents[0])
    service = tags["href"].split("?")[1].split("=")[1]
    # print(services)
    services.append(service)
service = set(services)
print(service)
# print(len(service))
# print(len(services))