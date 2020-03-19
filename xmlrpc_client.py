# -*- coding:utf-8 -*-
from xmlrpc.client import ServerProxy


def setup_socket_client(ip_address, port=6666):
    proxy = ServerProxy('http://%s:%s/' % (ip_address, port), allow_none=True)
    print('Connect to {}:{} successful ...'.format(ip_address, port))

    host_name = proxy.get_server_host_name()
    print('Received the server host name: {}'.format(host_name))

    server_ip = proxy.get_server_ip()
    print('Received the server ip: {}'.format(server_ip))

    while True:
        s = input()
        if s == "exit" or s == "q":
            print("连接已断开...")
            break
        else:
            print(s)
            res = proxy.parse_scpi()
            print(res)

if __name__ == '__main__':
    setup_socket_client(ip_address='localhost')
