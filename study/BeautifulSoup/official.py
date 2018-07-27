#!/usr/bin/env python3
__Author__ = "limugen"
"""https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/"""
from bs4 import BeautifulSoup
from urllib import request
import re

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc,"lxml")
# print(soup.prettify())
#print(type(soup))
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.title.parent.name)
# print(soup.title.parent.parent.name)
# print(soup.title.parent.parent.parent.name)
print(soup.find_all("p"))

for link in soup.find_all('a'):
    print(link.get("href"))