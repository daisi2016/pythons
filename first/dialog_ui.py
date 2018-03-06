# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created: Tue Jun 13 10:45:07 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!
from PySide import QtCore,QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.timeEdit = QtGui.QTimeEdit(Dialog)
        self.timeEdit.setGeometry(QtCore.QRect(10, 20, 118, 22))
        self.timeEdit.setObjectName("timeEdit")
        self.dateEdit = QtGui.QDateEdit(Dialog)
        self.dateEdit.setGeometry(QtCore.QRect(290, 30, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.fontComboBox = QtGui.QFontComboBox(Dialog)
        self.fontComboBox.setGeometry(QtCore.QRect(10, 60, 213, 22))
        self.fontComboBox.setObjectName("fontComboBox")
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(290, 60, 113, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))

