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
        Dialog.resize(573, 304)
        self.ui_DirList = QtWidgets.QComboBox(Dialog)
        self.ui_DirList.setGeometry(QtCore.QRect(110, 10, 421, 29))
        self.ui_DirList.setObjectName("ui_DirList")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 68, 17))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 270, 101, 17))
        self.label_3.setObjectName("label_3")
        self.ui_FileType = QtWidgets.QLineEdit(Dialog)
        self.ui_FileType.setGeometry(QtCore.QRect(120, 270, 361, 25))
        self.ui_FileType.setObjectName("ui_FileType")
        self.SaveName = QtWidgets.QLabel(Dialog)
        self.SaveName.setGeometry(QtCore.QRect(20, 240, 81, 17))
        self.SaveName.setObjectName("SaveName")
        self.ui_SelectedName = QtWidgets.QLineEdit(Dialog)
        self.ui_SelectedName.setEnabled(True)
        self.ui_SelectedName.setGeometry(QtCore.QRect(120, 240, 361, 25))
        self.ui_SelectedName.setText("")
        self.ui_SelectedName.setObjectName("ui_SelectedName")
        self.ui_mkdir = QtWidgets.QPushButton(Dialog)
        self.ui_mkdir.setGeometry(QtCore.QRect(540, 10, 31, 27))
        self.ui_mkdir.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ui_mkdir.setObjectName("ui_mkdir")
        self.ui_Action = QtWidgets.QPushButton(Dialog)
        self.ui_Action.setEnabled(False)
        self.ui_Action.setGeometry(QtCore.QRect(490, 240, 81, 27))
        self.ui_Action.setObjectName("ui_Action")
        self.ui_Cancel = QtWidgets.QPushButton(Dialog)
        self.ui_Cancel.setGeometry(QtCore.QRect(490, 270, 81, 27))
        self.ui_Cancel.setObjectName("ui_Cancel")
        self.ui_FileList = QtWidgets.QTableWidget(Dialog)
        self.ui_FileList.setGeometry(QtCore.QRect(0, 40, 571, 192))
        self.ui_FileList.setObjectName("ui_FileList")
        self.ui_FileList.setColumnCount(0)
        self.ui_FileList.setRowCount(0)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Look in:"))
        self.label_3.setText(_translate("Dialog", "Files of type:"))
        self.SaveName.setText(_translate("Dialog", "File name:"))
        self.ui_mkdir.setText(_translate("Dialog", "MD"))
        self.ui_Action.setText(_translate("Dialog", "Open"))
        self.ui_Cancel.setText(_translate("Dialog", "Cancel"))

