# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mus.ui',
# licensing of 'mus.ui' applies.
#
# Created: Tue Dec 17 15:28:34 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
import requests

class Mus(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(972, 628)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(230, 70, 201, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(150, 80, 54, 12))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(180, 210, 101, 41))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "音乐下载", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "音乐名", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("Form", "下载", None, -1))

