#!/usr/bin/env python3
__Author__ = "limugen"

from bs4 import BeautifulSoup
from urllib import request
import re
import sys

# url = 'https://book.douban.com/top250'
# url_request = request.urlopen(url)
# url_content = BeautifulSoup(url_request,"html5lib")
# # print(url_content)
# for link in url_content.find_all('tr', attrs={"class": "item"}):
#     # name = link.find("a")
#     # print(name['href'])
#     # info = link.find('p')
#     # print(info.text)
#     title = link.find('div')
#     print((str(title.a.text)).strip())
    # quote = link.find('span', class_="inq")
    # if quote:
    #     print
    #     quote.text
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

"""将取出来的表格数据放入到csv"""
html = urlopen("http://en.wikipedia.org/wiki/Comparison_of_text_editors")
bsObj = BeautifulSoup(html,"html5lib")
table = bsObj.findAll("table", {"class":"wikitable"})[0]
rows = table.findAll("tr")

csvFile = open("editors.csv", 'wt', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
try:
    for row in rows:
        csvRow = []
    for cell in row.findAll(['td', 'th']):
        csvRow.append(cell.get_text())
    writer.writerow(csvRow)
finally:
    csvFile.close()