#!/usr/bin/env python3
__Author__ = "limugen"
import socket

sk = socket.socket()
sk.bind(('127.0.0.1',8080))
sk.listen(4)
while True:
    conn,addr = sk.accept()
    data = conn.recv(8096)
    conn.send(b'testsanm')
    conn.close()