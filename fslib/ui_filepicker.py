# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'filepicker.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(565, 302)
        self.FileList = QtWidgets.QListWidget(Dialog)
        self.FileList.setGeometry(QtCore.QRect(0, 30, 561, 192))
        self.FileList.setObjectName("FileList")
        self.DirList = QtWidgets.QComboBox(Dialog)
        self.DirList.setGeometry(QtCore.QRect(100, 0, 461, 29))
        self.DirList.setObjectName("DirList")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 68, 17))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 240, 101, 17))
        self.label_3.setObjectName("label_3")
        self.file_type = QtWidgets.QLineEdit(Dialog)
        self.file_type.setGeometry(QtCore.QRect(110, 240, 341, 25))
        self.file_type.setObjectName("file_type")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(480, 240, 81, 241))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Open)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Look in:"))
        self.label_3.setText(_translate("Dialog", "Files of type:"))

