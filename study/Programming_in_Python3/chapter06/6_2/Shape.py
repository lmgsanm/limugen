#!/usr/bin/env python3
__Author__ = "limugen"
import math
#define class Point beginning
class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
##define class Point end

    def distance_form_orgin(self):
        return math.hypot(self.x,self.y)

    def __eq__(self,other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return "Point({0,x!r},{0,y!r})".format(self)

    def __str__(self):
        return "({0,x!r},{0,y!r})".format(self)

