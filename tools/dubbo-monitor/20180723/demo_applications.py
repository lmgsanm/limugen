#!/usr/bin/env python3
__Author__ = "limugen"

from bs4 import BeautifulSoup
from urllib import request
import re

url = "http://10.206.35.109:8081/applications.html"

url_request = request.urlopen(url)
url_content = BeautifulSoup(url_request,"html5lib")
# print(url_content)
host_dict = {}
host_content = url_content.find_all(href=re.compile("application="))
for tag in host_content:
    content_attr = tag["href"].split("?")[1].split("=")[1]
    # content_string = tag.string
    content_string = tag.get_text
    host_dict[content_attr] = content_string
    print(content_string)
# print(host_dict)
#     print(tag)
# host_list = []
# host_consumers = url_content.find_all(href=re.compile("consumers"))
# host_providers = url_content.find_all(href=re.compile("providers"))
# for consumers in host_consumers:
#     host_list.append(consumers)
#
# for providers in host_providers:
#     host_list.append(providers)
# print(host_list)