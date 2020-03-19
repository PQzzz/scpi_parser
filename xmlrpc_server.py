# -*- coding:utf-8 -*-
import os
import re
from xmlrpc.server import SimpleXMLRPCServer

import parse_test


class ServiceMethod(object):
    """
    这个类包含客户端所有能被执行的方法
    每个方法必须要有一个返回值，如果没有合适的返回值可以直接返回True
    """
    @staticmethod
    def get_server_ip():
        """
        获取服务器端的IP地址
        :return:
        """
        result = os.popen('ipconfig')
        ip_address = re.search(r'IPv4.+?: (\d+?\.\d+?\.\d+?\.\d+)', result .read())
        if ip_address:
            return ip_address.group(1)
        else:
            return 'Server ip address was not found'


def get_server_host_name():
    """
    这是获取服务器端计算机主机名的函数
    :return:
    """
    result = os.popen('ipconfig /all')
    host_name = re.search(r'主机名.+?: (\w+)', result.read())
    if host_name:
        return host_name.group(1)
    else:
        return 'Server host name was not found'

def parse_scpi():
    res = parse_test.parse_scpi_test()
    return res




def setup_socket_server(ip_address='localhost', port=6666):
    """
    注册一个函数或者类来响应XML-RPC请求，并启动XML-RPC服务器
    :param ip_address: 供客户端连接的IP地址，默认使用localhost，localhost为当前网卡IP，也可以自己指定合法有效的IP地址
    :param port: 供客户端连接的端口号，默认为6666
    :return:
    """
    try:
        service = SimpleXMLRPCServer((ip_address, port))  # 初始化XML-RPC服务
        print('Server {} Listening on port {} ...'.format(ip_address, port))
        service.register_function(get_server_host_name)  # 注册一个函数
        service.register_function(parse_scpi)  # 注册一个函数
        service.register_instance(ServiceMethod())  # 注册一个类
        service.serve_forever()  # 启动服务器并永久运行
    except Exception as ex:
        raise Exception('Setup socket server error:\n{}'.format(ex))


if __name__ == '__main__':
    setup_socket_server(ip_address='localhost')
