#!/usr/bin/env python3
import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 13337
BUFFER_SIZE = 1024
RED = '\033[0;31m'
GREEN = '\033[0;32m'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
while 1:
    mymessage = input(GREEN+' <I>           : ')
    s.send(mymessage.encode())
    response = s.recv(BUFFER_SIZE)
    print(RED,"<Interlocutor>:", response.decode(encoding='UTF-8'))


s.close()
