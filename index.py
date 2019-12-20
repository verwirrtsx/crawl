# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui',
# licensing of 'login.ui' applies.
#
# Created: Fri Dec 13 16:59:42 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
import sys
from choose import Choose

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(795, 620)
        self.ui = Form
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(230, 160, 331, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(230, 240, 331, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(360, 340, 91, 41))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton.clicked.connect(self.login)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "登录", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("Form", "登录", None, -1))
    def login(self):
        if self.lineEdit.text() == 'sx' and self.lineEdit_2.text() == '520' :
            form1 = QtWidgets.QDialog()
            ui = Choose()
            ui.setupUi(form1)
            self.ui.hide()
            form1.show()
            form1.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv) # 创建一个QApplication，也就是你要开发的软件app
    MainWindow = QtWidgets.QMainWindow()  # 创建一个QMainWindow，用来装载你需要的各种组件、控件
    ui = Ui_Form()             # ui是你创建的ui类的实例化对象
    ui.setupUi(MainWindow)         # 执行类中的setupUi方法，方法的参数是第二步中创建的QMainWindow
    MainWindow.show()            # 执行QMainWindow的show()方法，显示这个QMainWindow
    sys.exit(app.exec_())
