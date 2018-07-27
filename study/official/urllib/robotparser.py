#!/usr/bin/env python3
__Author__ = "limugen"

from urllib import robotparser

rp = robotparser.RobotFileParser()

rp.set_url("http://www.musi-cal.com/robots.txt")
rp.read()
rrate = rp.request_rate("*")
print(rrate)