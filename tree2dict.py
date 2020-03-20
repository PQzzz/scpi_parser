from itertools import groupby

from Node import Node
from xml2tree import Xml2Tree


def tree2dictPublic(root):
    public_dict = {}
    for node in root.children:
        if node.name == "Public":
            key = node.attributes["cmd"]
            value = Node(node.attributes)
            public_dict[key] = value
    return public_dict


def tree2dictSecific(root,specific_dict):
    if not root.children:
        return
    for node in root.children:
        if node.name == "Specific":
            cmd = node.attributes["cmd"]
            key = cmdShorten(cmd)
            value = Node(node.attributes)
            specific_dict[key] = value

            tree2dictSecific(node, specific_dict[key].lowAddrSet)

    return specific_dict



def cmdShorten(cmd):
    cmd_list = [''.join(list(g)) for k, g in groupby(cmd, key=lambda x: x.isdigit())]
    if len(cmd_list) > 1:
        key = cmd_list[0][:4] if cmd_list[0][:4].isupper() else cmd_list[0][:3]
        key = key + cmd_list[1]
    else:
        key = cmd[:4] if cmd[:4].isupper() else cmd[:3]

    return key


def tree2dict():
    public_dict = {}
    public_dict = tree2dictPublic(root)
    specific_dict = {}
    specific_dict = tree2dictSecific(root, specific_dict)

    return public_dict, specific_dict


if __name__ == '__main__':
    root = Xml2Tree().Parse('Bert_100G.xml')
    public_dict, specific_dict = tree2dict()
    print(specific_dict)
    print(specific_dict["SOUR1"].info)
    print(specific_dict["SOUR1"].lowAddrSet)
    print(specific_dict["SOUR1"].lowAddrSet["PATT"].info)
    print(specific_dict["SOUR1"].lowAddrSet["PATT"].lowAddrSet)
    print(specific_dict["SOUR1"].lowAddrSet["PATT"].lowAddrSet["LENG"].info)
    print(specific_dict["SOUR1"].lowAddrSet["PATT"].lowAddrSet["LENG"].lowAddrSet)
