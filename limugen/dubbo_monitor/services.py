#!/usr/bin/env python3
__Author__ = "limugen"

from bs4 import BeautifulSoup
import re
import urllib

url = "http://10.205.54.130:8080/services.html"
html_doc_name = urllib.request.urlopen(url)
#html_doc_name = "services.html"
#html_doc = open_file_handler(html_doc_name)
soup = BeautifulSoup(open_file_handler(html_doc_name),"html5lib")
services_consumers = soup.find_all(href=re.compile("consumers"))
services_providers = soup.find_all(href=re.compile("providers"))
services_list = []
for consumers in services_consumers:
    services_list.append(consumers)
for providers in services_providers:
    services_list.append(providers)
services = []
for tags in services_list:
    service = tags["href"].split("?")[1].split("=")[1]
    services.append(service)
service = set(services)
print(service)
