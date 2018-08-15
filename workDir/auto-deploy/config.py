#!/usr/bin/env python3
__Author__ = "limugen"

from yaml import load,dump

try:
    from yaml import CLoader as Loader,CDumper as Dumper
except ImportError:
    from yaml import Loader,Dumper

def get_config_path(f):
    file = dump(load(f))
    return file


data = get_config_path("config/config.yml")
print(data)