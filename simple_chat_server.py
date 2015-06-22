#!/usr/bin/env python3
import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 13337
BUFFER_SIZE = 1024
RED = '\033[0;31m'
GREEN = '\033[0;32m'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(10)

conn, addr = s.accept()
print('Connection address:', addr)
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data:
        break
    print(GREEN,"<Interlocutor>:", data.decode())
    mymessage = input(RED +" <i>           : ")
    conn.send(mymessage.encode(encoding='UTF-8'))
conn.close()