#!/usr/bin/env python3
__Author__ = "limugen"

from urllib import request

with request.urlopen('http://www.python.org') as url:
    print(url.read())