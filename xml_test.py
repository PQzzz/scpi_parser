#!/usr/bin/python3

from xml.dom.minidom import parse
import xml.dom.minidom


# 生成SCPI树
SCPITree = xml.dom.minidom.parse("Bert_100G.xml")
root = SCPITree.documentElement
if root.hasAttribute("Device"):
   print ("设备名称 : %s" % root.getAttribute("Device"))

print(root.getElementsByTagName("Specific")[4].getAttribute("Cmd"))


# cmd = ":CHAN:PATT?"
# if cmd.startswith(":"):
#     # 特定命令
#     if cmd.endswith("?"):
#         # 查询命令
#         cmd = cmd[1:-1]
#         cmd_list = cmd.split(":")
#
#         level1 = root.getElementsByTagName("Specific")
#         for node in level1:
#             if node.getAttribute("Level")=="1":
#                 print(node.getAttribute("Cmd"))
#                 if cmd[0] in node.getAttribute("Cmd"):
#                     cmd_list.pop(0)
#
#     else:
#         # 执行命令
#         pass
# elif cmd.startswith("*"):
#     # 公用命令
#     pass



# def specific_parser(level):
#     print(level)
#     level_num = 1
#     level_str = "Level" + str(level_num)
#     level_n = level.getElementsByTagName(level_str)
#     for lev in level_n:
#
#     if level_n.getAttribute("IsEnd") == "0":
#         pass













# 使用minidom解析器打开 XML 文档
# DOMTree = xml.dom.minidom.parse("movies.xml")
# collection = DOMTree.documentElement
# print(collection.childNodes[0].getElementsByTagName('year')[1].childNodes[0].data)

# if collection.hasAttribute("shelf"):
#    print ("Root element : %s" % collection.getAttribute("shelf"))

# 在集合中获取所有电影
# movies = collection.getElementsByTagName("movie")
# print(movies[0].nodeName)

# 打印每部电影的详细信息
# for movie in movies:
#    print ("*****Movie*****")
#    if movie.hasAttribute("title"):
#       print ("Title: %s" % movie.getAttribute("title"))
#
#    type = movie.getElementsByTagName('type')[0]
#    print ("Type: %s" % type.childNodes[0].data)
#    format = movie.getElementsByTagName('format')[0]
#    print ("Format: %s" % format.childNodes[0].data)
#    rating = movie.getElementsByTagName('rating')[0]
#    print ("Rating: %s" % rating.childNodes[0].data)
#    description = movie.getElementsByTagName('description')[0]
#    print ("Description: %s" % description.childNodes[0].data)