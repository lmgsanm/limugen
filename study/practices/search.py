#!/usr/bin/env python3
__Author__ = "limugen"
'二分法查找'

def search(seq,num,lower=0,upper=None):
    if upper == None:
        upper = len(seq) - 1
        num = seq[upper]
    else:
        lower = min(seq)
        upper = max(seq)
        middle = (lower + upper) // 2
        if num > middle:
            return search(seq,num,middle+1,upper)
        else:
            return search(seq,num,lower,middle)

seq = [3,3,57,89,123,345,999]
search(seq,57,3,123)
