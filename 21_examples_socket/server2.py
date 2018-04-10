#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-04-10 23:03:33
# @copyright by hoojo@2018
# @changelog Added python3 `socket -> server2` example


# Echo server program
import socket
import sys

HOST = 'localhost'               # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port

s = None
for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
    print('res', res)
    af, socktype, proto, canonname, sa = res
    # <AddressFamily.AF_INET6: 23>, <SocketKind.SOCK_STREAM: 1>, 0, '', ('::1', 50007, 0, 0)
    
    print('AddressFamily:', af)
    print('sockType:', socktype)
    print('proto:', proto)
    print('canonname', canonname)
    print('host/port:', sa)

    try:
        s = socket.socket(af, socktype, proto)
    except socket.error as msg:
        s = None
        continue
    
    try:
        s.bind(sa)
        s.listen(1)
    except socket.error as msg:
        s.close()
        s = None
        continue
    break

if s is None:
    print('could not open socket')
    sys.exit(1)
    
conn, addr = s.accept()
print('Connected by', addr)

while True:
    data = conn.recv(1024)
    if not data: break
    conn.send(data)
    
conn.close()