#!/usr/bin/env python3
__Author__ = "limugen"

from urllib import request


url = "http://pythonscraping.com/pages/page1.html"
req = request.Request(url)
html = request.urlopen(req)
print(html.read())