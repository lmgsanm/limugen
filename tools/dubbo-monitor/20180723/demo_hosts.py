#!/usr/bin/env python3
__Author__ = "limugen"

from bs4 import BeautifulSoup
from urllib import request
import re
import sys

url = "http://10.206.35.109:8081/hosts.html"

header = {"User-Agent" : "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11",
          "Content-Type" : "application/json",
          "Charset" : "utf8"
          }
reg = re.compile(("<[^>]*>"))
url_request = request.urlopen(url)
url_content = BeautifulSoup(url_request,"html5lib")

table = url_content.findAall("table",{"class":""})
# for child in url_content.children:
#     print(child)
#     sys.exit()

# tag = url_content.find_all("thead")
# tag_th_list = []
# tag_td_list = []
# for tag in url_content.find_all("thead"):
#     #print(tag.th.string)
#     print(type(tag.th))
#     tag_th_list.append(tag.th.string)
#
#     print(type(tag.td))
#     for td_tag in tag.td:
#         print(td_tag)
# print(tag_th_list)
# print(tag_td_list)
# print(len(tag_td_list))

    # print(tag.th)
    # print(type(tag.th))
    # print(tag.td)
    # print(type(tag.td))
# print(url_content.find_all("thead"))
# print(type(url_content.find_all(href=re.compile("servers"))))

# url_request = request.urlopen(url)
# url_content = BeautifulSoup(url_request,"html5lib")


# # print(url_content)
# host_dict = {}
# host_content = url_content.find_all(href=re.compile("host="))
# for tag in host_content:
#     content_attr = tag["href"].split("?")[1].split("=")[1]
#     content_string = tag.string
#     host_dict[content_attr] = content_string
# # print(host_dict)
#     print(tag)
# # host_list = []
# host_consumers = url_content.find_all(href=re.compile("consumers"))
# host_providers = url_content.find_all(href=re.compile("providers"))
# for consumers in host_consumers:
#     host_list.append(consumers)
#
# for providers in host_providers:
#     host_list.append(providers)
# print(host_list)

# total = url_content.find_all('thead')
# taglist = url_content.find_all('th',attrs={'href'})
# taglist = url_content.find_all('colspan')
# for tag in taglist:
#     print(tag)
# # slect = url_content.select("th.colspan")
#
# print(total)
# print(type(total))
# print(slect)
