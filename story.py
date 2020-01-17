# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'story.ui',
# licensing of 'story.ui' applies.
#
# Created: Wed Dec 18 10:50:24 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
from get_stoty import Getsotry

class MThread(QtCore.QThread):

    def __init__(self,story_name):
        super().__init__()
        self.story_name= story_name

    def run(self):
        # 线程相关代码
        if Getsotry(self.story_name) :
            print('ok')
        else:
            print('no')

class Story(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1088, 720)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(140, 50, 31, 20))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(200, 40, 261, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(150, 150, 101, 41))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton.clicked.connect(self.down)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "小说", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "小说", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("Form", "下载", None, -1))
    def down(self):
        story_name = self.lineEdit.text()
        print(story_name)
        new_thread = MThread(story_name)
        new_thread.start()
        sys.exit(app.exec_())


