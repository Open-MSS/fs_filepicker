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
        Dialog.resize(714, 400)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("../../fsfp/Menu/fsfp.ico"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        Dialog.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.main_horizontal = QtWidgets.QHBoxLayout()
        self.main_horizontal.setObjectName("main_horizontal")
        self.fs_buttons_vertical = QtWidgets.QVBoxLayout()
        self.fs_buttons_vertical.setObjectName("fs_buttons_vertical")
        self.ui_fs_serverlist = QtWidgets.QListWidget(Dialog)
        self.ui_fs_serverlist.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.ui_fs_serverlist.sizePolicy().hasHeightForWidth()
        )
        self.ui_fs_serverlist.setSizePolicy(sizePolicy)
        self.ui_fs_serverlist.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui_fs_serverlist.setObjectName("ui_fs_serverlist")
        self.fs_buttons_vertical.addWidget(self.ui_fs_serverlist)
        self.main_horizontal.addLayout(self.fs_buttons_vertical)
        self.Files_vertical = QtWidgets.QVBoxLayout()
        self.Files_vertical.setObjectName("Files_vertical")
        self.TopNavgation_horizontal = QtWidgets.QHBoxLayout()
        self.TopNavgation_horizontal.setObjectName("TopNavgation_horizontal")
        self.ui_other_fs = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ui_other_fs.sizePolicy().hasHeightForWidth())
        self.ui_other_fs.setSizePolicy(sizePolicy)
        self.ui_other_fs.setMinimumSize(QtCore.QSize(32, 32))
        self.ui_other_fs.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ui_other_fs.setObjectName("ui_other_fs")
        self.TopNavgation_horizontal.addWidget(self.ui_other_fs)
        self.ui_label_Lookin = QtWidgets.QLabel(Dialog)
        self.ui_label_Lookin.setObjectName("ui_label_Lookin")
        self.TopNavgation_horizontal.addWidget(self.ui_label_Lookin)
        self.ui_DirList = QtWidgets.QComboBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ui_DirList.sizePolicy().hasHeightForWidth())
        self.ui_DirList.setSizePolicy(sizePolicy)
        self.ui_DirList.setMinimumSize(QtCore.QSize(380, 0))
        self.ui_DirList.setObjectName("ui_DirList")
        self.TopNavgation_horizontal.addWidget(self.ui_DirList)
        self.top_buttongroup_right = QtWidgets.QHBoxLayout()
        self.top_buttongroup_right.setObjectName("top_buttongroup_right")
        self.ui_mkdir = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ui_mkdir.sizePolicy().hasHeightForWidth())
        self.ui_mkdir.setSizePolicy(sizePolicy)
        self.ui_mkdir.setMinimumSize(QtCore.QSize(32, 32))
        self.ui_mkdir.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ui_mkdir.setObjectName("ui_mkdir")
        self.top_buttongroup_right.addWidget(self.ui_mkdir)
        self.TopNavgation_horizontal.addLayout(self.top_buttongroup_right)
        self.Files_vertical.addLayout(self.TopNavgation_horizontal)
        self.ui_FileList = QtWidgets.QTableWidget(Dialog)
        self.ui_FileList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui_FileList.setAlternatingRowColors(True)
        self.ui_FileList.setShowGrid(False)
        self.ui_FileList.setWordWrap(False)
        self.ui_FileList.setColumnCount(3)
        self.ui_FileList.setObjectName("ui_FileList")
        self.ui_FileList.setRowCount(0)
        self.ui_FileList.horizontalHeader().setCascadingSectionResizes(True)
        self.ui_FileList.horizontalHeader().setDefaultSectionSize(200)
        self.ui_FileList.horizontalHeader().setSortIndicatorShown(True)
        self.ui_FileList.horizontalHeader().setStretchLastSection(True)
        self.Files_vertical.addWidget(self.ui_FileList)
        self.Botton_Selection_horizontal = QtWidgets.QHBoxLayout()
        self.Botton_Selection_horizontal.setObjectName("Botton_Selection_horizontal")
        self.File_Label_grid = QtWidgets.QGridLayout()
        self.File_Label_grid.setObjectName("File_Label_grid")
        self.ui_label_filename = QtWidgets.QLabel(Dialog)
        self.ui_label_filename.setObjectName("ui_label_filename")
        self.File_Label_grid.addWidget(self.ui_label_filename, 0, 0, 1, 1)
        self.ui_label_filetype = QtWidgets.QLabel(Dialog)
        self.ui_label_filetype.setObjectName("ui_label_filetype")
        self.File_Label_grid.addWidget(self.ui_label_filetype, 1, 0, 1, 1)
        self.Botton_Selection_horizontal.addLayout(self.File_Label_grid)
        self.File_name_Files_of_type_grid = QtWidgets.QGridLayout()
        self.File_name_Files_of_type_grid.setObjectName("File_name_Files_of_type_grid")
        self.ui_SelectedName = QtWidgets.QLineEdit(Dialog)
        self.ui_SelectedName.setEnabled(True)
        self.ui_SelectedName.setText("")
        self.ui_SelectedName.setObjectName("ui_SelectedName")
        self.File_name_Files_of_type_grid.addWidget(self.ui_SelectedName, 1, 0, 1, 1)
        self.ui_FileType = QtWidgets.QComboBox(Dialog)
        self.ui_FileType.setEditable(True)
        self.ui_FileType.setObjectName("ui_FileType")
        self.File_name_Files_of_type_grid.addWidget(self.ui_FileType, 2, 0, 1, 1)
        self.Botton_Selection_horizontal.addLayout(self.File_name_Files_of_type_grid)
        self.Open_Cancel_grid = QtWidgets.QGridLayout()
        self.Open_Cancel_grid.setObjectName("Open_Cancel_grid")
        self.ui_Action = QtWidgets.QPushButton(Dialog)
        self.ui_Action.setEnabled(False)
        self.ui_Action.setMinimumSize(QtCore.QSize(80, 25))
        self.ui_Action.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ui_Action.setObjectName("ui_Action")
        self.Open_Cancel_grid.addWidget(self.ui_Action, 0, 0, 1, 1)
        self.ui_Cancel = QtWidgets.QPushButton(Dialog)
        self.ui_Cancel.setMinimumSize(QtCore.QSize(80, 25))
        self.ui_Cancel.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ui_Cancel.setObjectName("ui_Cancel")
        self.Open_Cancel_grid.addWidget(self.ui_Cancel, 1, 0, 1, 1)
        self.Botton_Selection_horizontal.addLayout(self.Open_Cancel_grid)
        self.Files_vertical.addLayout(self.Botton_Selection_horizontal)
        self.main_horizontal.addLayout(self.Files_vertical)
        self.verticalLayout.addLayout(self.main_horizontal)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.ui_other_fs.setText(_translate("Dialog", "OTHER"))
        self.ui_label_Lookin.setText(_translate("Dialog", "Look in:"))
        self.ui_mkdir.setText(_translate("Dialog", "MD"))
        self.ui_FileList.setSortingEnabled(True)
        self.ui_label_filename.setText(_translate("Dialog", "File name: "))
        self.ui_label_filetype.setText(_translate("Dialog", "Files of type:"))
        self.ui_Action.setText(_translate("Dialog", "Open"))
        self.ui_Cancel.setText(_translate("Dialog", "Cancel"))
