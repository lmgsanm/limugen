#!/usr/local/python3/bin/python3

from yaml import load,dump
import sys
import os


try:
    from yaml import CLoader as Loader,CDumper as Dumper
except ImportError:
    from yaml import Loader,Dumper

def get_config_path(f):
    file = dump(load(f))
    return file

#print(os.path[0])
print("hello world")
#data = get_config_path("config/config.yml")
#print(data)
