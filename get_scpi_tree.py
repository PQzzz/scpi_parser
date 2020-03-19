from xml.dom.minidom import parse
import xml.dom.minidom
from itertools import groupby

from Node import PublicNode, SpecificNode


def get_scpi_tree():
    SCPITree = xml.dom.minidom.parse("Bert_100G.xml")
    root = SCPITree.documentElement
    if root.hasAttribute("Device"):
        print("设备名称 : %s" % root.getAttribute("Device"))

    pulic_scpi_tree = get_public_cmd(root)
    specific_scpi_tree = get_specific_cmd(root)
    print(specific_scpi_tree['SOUR1'])



def get_public_cmd(root):
    public_dict = {}
    public_root_list = root.getElementsByTagName("Public")
    for i in range(len(public_root_list)):
        key = public_root_list[i].getAttribute('Cmd')
        value = PublicNode()
        value.setCmdID = public_root_list[i].getAttribute('SetCmdID')
        value.queryCmdID = public_root_list[i].getAttribute('QueryCmdID')
        public_dict[key] = value

    return public_dict


def get_specific_cmd(root):
    specific_dict = {}
    specific_root_list = root.getElementsByTagName("Specific")

    for node in specific_root_list:
        cmd = node.getAttribute('Cmd')

        cmd_list = [''.join(list(g)) for k, g in groupby(cmd, key=lambda x: x.isdigit())]
        if len(cmd_list) > 1:
            key = cmd_list[0][:4] if cmd_list[0][:4].isupper() else cmd_list[0][:3]
            key = key + cmd_list[1]
        else:
            key = cmd[:4] if cmd[:4].isupper() else cmd[:3]

        value = SpecificNode()
        value.cmd = cmd
        value.level = node.getAttribute('Level')
        value.isEnd = node.getAttribute('isEnd')
        value.queryCmdID = node.getAttribute('QueryCmdID')
        value.setCmdID = node.getAttribute('SetCmdID')
        value.omissible = node.getAttribute('Omissible')
        value.nextLevel = node.getAttribute('NextLevel')

        specific_dict[key] = value



    return specific_dict


# 清除xml中的"\n"
def clr_line_feeds(node):
    for child in node.childNodes:
        if child.nodeType == 3:
            node.childNodes.remove(child)

    return node


if __name__ == '__main__':
    get_scpi_tree()