#!/usr/bin/env python3
__Author__ = "limugen"

from bs4 import BeautifulSoup
import urllib.request
import re

url = "http://10.206.35.109:8081/hosts.html"
headers = {"User-Agent" : "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11",
          "Content-Type" : "application/json",
          "Charset" : "utf8"
          }

req = urllib.request.Request(url=url,headers=headers)

html = BeautifulSoup(urllib.request.urlopen(req),"html5lib")

Consumers = html.find_all(href=re.compile("consumers"))
Providers = html.find_all(href=re.compile("providers"))
consumer_dict = {}
for consumer in Consumers:
    ip = consumer["href"].split("?")[1].split("=")[1]
    # num = consumer.string
    num = consumer.string.encode("utf-8").decode("utf-8").split("(")[1].split(")")[0]
    consumer_dict[ip] = num
provider_dict = {}
for provider in Providers:
    ip = provider["href"].split("?")[1].split("=")[1]
    # num = consumer.string
    num = provider.string.encode("utf-8").decode("utf-8").split("(")[1].split(")")[0]
    provider_dict[ip] = num

ip_list = []
consumer_sum = 0
provider_sum = 0

#for ip in consumer_dict.keys() or provider_dict.keys():
for ip in consumer_dict:
    ip_list.append(ip)
    consumer_sum += int(consumer_dict[ip])
for ip in provider_dict:
    ip_list.append(ip)
    provider_sum += int(provider_dict[ip])
ip = set(ip_list)
ip_sum = len(ip_list)
print(ip)
print(consumer_dict)
print(provider_dict)
print(ip_list)
print(consumer_sum)
print(provider_sum)
print(ip_sum)
