#!/usr/bin/env python3
__Author__ = "limugen"

from bs4 import BeautifulSoup
#from bs4 import NavigableString
import re
def open_file_handler(f):
    fd = open(f,'r')
    return fd

html_doc_name = "applications.html"
html_doc = open_file_handler(html_doc_name)
#print(type(html_doc))
soup = BeautifulSoup(open_file_handler(html_doc_name),"html5lib")
applications_consumers = soup.find_all(href=re.compile("consumers"))
applications_providers = soup.find_all(href=re.compile("providers"))
applications_list = []
for consumers in applications_consumers:
    applications_list.append(consumers)

for providers in applications_providers:
    applications_list.append(providers)
# print(len(applications_list))
applications = []
for tags in applications_list:
    # print(tags["href"])
    #print(tags.string)
    #print(tags["href"].split("?")[1].split("=")[1],tags.contents[0])
    application = tags["href"].split("?")[1].split("=")[1]
    applications.append(application)

# print(applications)
application = set(applications)
# print(len(application))
print(application)
