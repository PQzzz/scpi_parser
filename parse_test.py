# import funcFile
from Node import Node
import os


def parse_scpi_test():
    NAME = ""
    pwd = os.getcwd()
    for f in os.listdir(pwd):
        if f == "funcFile.py":
            NAME = f[0:-3]
            exec("import " + f[0:-3])


    s1 = Node()
    s1.isEnd, s1.setCmdID = 1, 'setChannelPattern'

    s2 = Node()
    s2.isEnd, s2.queryCmdID = 1, 'queryChannelPattern'

    if (s1.isEnd == 1):
        ch = None
        param = None
        res = eval(NAME + "." +s1.setCmdID)()
        # print(res)
        return res

if __name__ == '__main__':

    parse_scpi_test()

#-------------------------------------------------------------------------

# import threading
# import time
#
# # 为线程定义一个函数
# def print_time( threadName, delay):
#    count = 0
#    while count < 5:
#       time.sleep(delay)
#       count += 1
#       print ("%s: %s" % ( threadName, time.ctime(time.time()) ))
#
# # 创建两个线程
# try:
#    threading.Thread(target=print_time, args=("t1",2)).start()
#    threading.Thread(target=print_time, args=("Thread-2", 4, ) ).start()
# except:
#    print ("Error: 无法启动线程")




#--------------------------------------------------------------------------

# import visa
# rm = visa.ResourceManager()
# print(rm.list_resources())
