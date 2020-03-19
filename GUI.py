import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QStringListModel
from gui_test import Ui_Form


class MyPyQT_Form(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(MyPyQT_Form,self).__init__()
        self.setupUi(self)
        self.itemModel = QStringListModel(self)
        self.itemList = ["100G 误码测试仪","200G 误码测试仪"]
        self.itemModel.setStringList(self.itemList)
        self.listView_instrument.setModel(self.itemModel)

    def radiobtn_wire_click(self):
        print("有线连接")

    def radiobtn_wireless_click(self):
        print("无线连接")

    def listView_instrument_click(self,index):
        self.label_instrument.setText(self.itemList[index.row()])

    def pushBtn_send_click(self):
        text = self.textEdit_input.toPlainText()
        print(text)







if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    mainWindow.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint|QtCore.Qt.WindowCloseButtonHint)
    ui = MyPyQT_Form()
    ui.show()
    sys.exit(app.exec_())
