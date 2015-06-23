#!/usr/bin/env python3
import socket

def colorization(is_color):
    if is_color: color_ss, color_cs = '\033[0;31m', '\033[0;32m' #red, green
    else: color_ss, color_cs = '', ''
    return color_ss, color_cs

def valid_ip(address):
    try:
        host_bytes = address.split('.')
        valid = [int(b) for b in host_bytes]
        valid = [b for b in valid if b >= 0 and b<=255]
        return len(host_bytes) == 4 and len(valid) == 4
    except:
        return False

def parsing_from_cl():
    import argparse
    parser = argparse.ArgumentParser(description='This is a simple chat. It contains both client and server code.')
    parser.add_argument('ip', help='set the server ip address, use ipv4')
    parser.add_argument('port', help='set the port number (must be between 0 and 65535)', type=int)
    parser.add_argument('--as-server', help='start server, by default will run the client', action='store_true')
    parser.add_argument('--bsize', help='set the buffer size, (the default buffer size is 1024)', type=int, action='store', default=1024)
    parser.add_argument('--color', help='turn on color dialog', action='store_true')
    args = parser.parse_args()
    import sys
    if args.ip == 'localhost': args.ip = '127.0.0.1'
    if not valid_ip(args.ip): sys.exit('Ip address is incorrect.')
    if not (0<args.port and args.port<65535): sys.exit('Port number is incorrect. The port number must be between 0 and 65535.')
    return args.ip, args.port, args.bsize, args.color, args.as_server

def start_server(tcp_ip, tcp_port, buffer_size, is_color):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((tcp_ip, tcp_port))
    s.listen(1)
    conn, addr = s.accept()
    print('Connection address:', addr)
    color_ss, color_cs = colorization(is_color)
    while 1:
        data = conn.recv(buffer_size)
        if not data:
            break
        print(color_cs, "<Interlocutor>:", data.decode())
        my_message = input(color_ss +" <i>           : ")
        conn.send(my_message.encode(encoding='UTF-8'))
    conn.close()

def chatting(tcp_ip, tcp_port, buffer_size, is_color):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((tcp_ip, tcp_port))
    color_ss, color_cs = colorization(is_color)
    while 1:
        my_message = input(color_cs+' <I>           : ')
        s.send(my_message.encode())
        response = s.recv(buffer_size)
        print(color_ss, "<Interlocutor>:", response.decode(encoding='UTF-8'))
    s.close()

if __name__=='__main__':
    tcp_ip, tcp_port, buffer_size, is_color, is_server = parsing_from_cl()
    if is_server: start_server(tcp_ip, tcp_port, buffer_size, is_color)
    else: chatting(tcp_ip, tcp_port, buffer_size, is_color)
    