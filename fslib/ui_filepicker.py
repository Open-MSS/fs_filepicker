# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_filepicker.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(573, 346)
        self.ui_FileList = QtWidgets.QListWidget(Dialog)
        self.ui_FileList.setGeometry(QtCore.QRect(0, 70, 561, 192))
        self.ui_FileList.setObjectName("ui_FileList")
        self.ui_DirList = QtWidgets.QComboBox(Dialog)
        self.ui_DirList.setGeometry(QtCore.QRect(100, 40, 461, 29))
        self.ui_DirList.setObjectName("ui_DirList")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 50, 68, 17))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 280, 101, 17))
        self.label_3.setObjectName("label_3")
        self.ui_FileType = QtWidgets.QLineEdit(Dialog)
        self.ui_FileType.setGeometry(QtCore.QRect(110, 280, 341, 25))
        self.ui_FileType.setObjectName("ui_FileType")
        self.ui_ButtonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.ui_ButtonBox.setGeometry(QtCore.QRect(480, 280, 81, 241))
        self.ui_ButtonBox.setOrientation(QtCore.Qt.Vertical)
        self.ui_ButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Open)
        self.ui_ButtonBox.setObjectName("ui_ButtonBox")
        self.SaveName = QtWidgets.QLabel(Dialog)
        self.SaveName.setGeometry(QtCore.QRect(10, 10, 67, 17))
        self.SaveName.setObjectName("SaveName")
        self.ui_SelectedName = QtWidgets.QLineEdit(Dialog)
        self.ui_SelectedName.setGeometry(QtCore.QRect(100, 10, 461, 25))
        self.ui_SelectedName.setObjectName("ui_SelectedName")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Look in:"))
        self.label_3.setText(_translate("Dialog", "Files of type:"))
        self.SaveName.setText(_translate("Dialog", "Name:"))

