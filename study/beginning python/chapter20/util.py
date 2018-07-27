#!/usr/bin/env python3
__Author__ = "limugen"

def lines(file):
    for line in file:
        yield line
    yield '\n'

def blocks(file):
    block = []
    for line in line(file):
        if line.strip():
            block.append()
        else:
            yield ''.join(block).strip()
            block = []







