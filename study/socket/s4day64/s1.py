#!/usr/bin/env python3
__Author__ = "limugen"
import socket
IP = '127.0.0.1'
PORT = 8088

sock = socket.socket()
sock.bind((IP,PORT))
sock.listen(5)

while True:
    conn,add = sock.accept()
    data = conn.recv(8096)
    conn.send(b'123123')
    conn.close()
