#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as S:
    S.connect((HOST, PORT))
    S.sendall(b'Hello, world')
    data = S.recv(1024)

print('RECEIVED', repr(data))
