# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fs_filedialog.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(568, 366)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 68, 17))
        self.label.setObjectName("label")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setGeometry(QtCore.QRect(480, 250, 81, 241))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Open)
        self.buttonBox.setObjectName("buttonBox")
        self.file_type = QtWidgets.QLineEdit(self.centralwidget)
        self.file_type.setGeometry(QtCore.QRect(100, 240, 341, 25))
        self.file_type.setObjectName("file_type")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 250, 101, 17))
        self.label_3.setObjectName("label_3")
        self.DirList = QtWidgets.QComboBox(self.centralwidget)
        self.DirList.setGeometry(QtCore.QRect(100, 10, 461, 29))
        self.DirList.setObjectName("DirList")
        self.FileList = QtWidgets.QListWidget(self.centralwidget)
        self.FileList.setGeometry(QtCore.QRect(0, 40, 561, 192))
        self.FileList.setObjectName("FileList")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Look in:"))
        self.label_3.setText(_translate("MainWindow", "Files of type:"))

