#!/usr/bin/env python3
__Author__ = "limugen"

import sys

for line in sys.stdin:
    ss = line.strip().split(' ')
    for word in ss:
        print("\t".join([word.strip(),1]))