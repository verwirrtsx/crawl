# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'choose.ui',
# licensing of 'choose.ui' applies.
#
# Created: Mon Dec 16 15:32:34 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
import sys
from mus import Mus
from story import Story

class Choose(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(987, 724)
        self.ui = Form
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(200, 110, 151, 61))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(560, 260, 151, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(200, 260, 151, 61))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(560, 110, 151, 61))
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton.clicked.connect(self.goto)
        self.pushButton_4.clicked.connect(self.tostory)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "选择", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("Form", "图片下载", None, -1))
        self.pushButton_2.setText(QtWidgets.QApplication.translate("Form", "其他", None, -1))
        self.pushButton_3.setText(QtWidgets.QApplication.translate("Form", "音乐下载", None, -1))
        self.pushButton_4.setText(QtWidgets.QApplication.translate("Form", "小说下载", None, -1))

    def goto(self):
        form1 = QtWidgets.QDialog()
        ui = Mus()
        ui.setupUi(form1)
        self.ui.hide()
        form1.show()
        form1.exec_()

    def tostory(self):
        form2 = QtWidgets.QDialog()
        ui = Story()
        ui.setupUi(form2)
        self.ui.hide()
        form2.show()
        form2.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv) # 创建一个QApplication，也就是你要开发的软件app
    MainWindow = QtWidgets.QMainWindow()  # 创建一个QMainWindow，用来装载你需要的各种组件、控件
    ui = Choose()             # ui是你创建的ui类的实例化对象
    ui.setupUi(MainWindow)         # 执行类中的setupUi方法，方法的参数是第二步中创建的QMainWindow
    MainWindow.show()            # 执行QMainWindow的show()方法，显示这个QMainWindow
    sys.exit(app.exec_())

