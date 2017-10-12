# -*- coding: utf-8 -*-
"""

    fslib.fs_filepicker
    ~~~~~~~~~~~~~~~~~~~

    This module provides the QT main window for accessing a pyfilesystem2

    This file is part of fs_filepicker.

    :copyright: Copyright 2017 Reimar Bauer
    :license: APACHE-2.0, see LICENSE for details.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""
import sys

from fs import open_fs
from PyQt5 import QtWidgets
from fslib import fs_filedialog


class FilePicker(QtWidgets.QMainWindow, fs_filedialog.Ui_MainWindow):
    def __init__(self, parent=None, fs_name=u"~/", file_pattern=u'*.*'):
        super(FilePicker, self).__init__(parent)
        self.setupUi(self)
        self.filename = None
        self.setWindowTitle("FS File Picker")
        self.fs_name = fs_name
        self.home_fs = None
        self.last_index = 0
        self.file_pattern = file_pattern
        self.file_type.setText(self.file_pattern)
        self.browse_folder()
        self.file_type.returnPressed.connect(self.selection_file_type)
        self.buttonBox.button(self.buttonBox.Cancel).clicked.connect(self.cancel)
        self.buttonBox.button(self.buttonBox.Open).clicked.connect(self.open)

    def browse_folder(self):
        self.DirList.clear()
        self.home_fs = open_fs(self.fs_name)
        for dir_path in self.home_fs.walk.dirs():
            self.DirList.addItem(dir_path)
        self.selection_directory(0)
        self.DirList.currentIndexChanged.connect(self.selection_directory)

    def selection_directory(self, i):
        self.last_index = i
        selected_dir = self.DirList.currentText()
        self.FileList.clear()
        file_type = self.file_type.text()
        for files in self.home_fs.walk.files(selected_dir, filter=[unicode(file_type)]):
            self.FileList.addItem(files)

    def selection_file_type(self):
        self.selection_directory(self.last_index)

    def cancel(self):
        self.close()

    def open(self):
        self.filename = self.FileList.item(self.FileList.currentRow()).text()
        self.close()


def filepicker(parent=None, fs_name=u'~/', file_pattern=u'*.*'):
    app = QtWidgets.QApplication(sys.argv)
    form = FilePicker(parent, fs_name, file_pattern)
    form.show()
    app.exec_()
    return form.filename

if __name__ == '__main__':
    print(filepicker())

