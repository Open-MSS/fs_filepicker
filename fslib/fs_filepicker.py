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
import argparse

import fs
from PyQt5 import QtWidgets, QtCore
from fslib import ui_filepicker, __version__
from fslib.utils import match_extension

class FilePicker(QtWidgets.QDialog, ui_filepicker.Ui_Dialog):
    def __init__(self, parent=None, fs_url=u"~/", file_pattern=u'*.*', title=u'FS File Picker',
                 default_filename=None, show_save_action=False):
        super(FilePicker, self).__init__(parent)
        self.setupUi(self)
        self.selected_dir = None
        self.filename = None
        self.setWindowTitle(title)
        self.fs_url = unicode(fs_url)
        self.fs = None
        self.last_index = 0
        self.default_filename = default_filename
        self.file_pattern = file_pattern
        self.show_save_action = show_save_action
        self.show_action()
        self.ui_FileType.setText(self.file_pattern)
        self.browse_folder()
        self.ui_FileType.returnPressed.connect(self.selection_file_type)
        self.ui_ButtonBox.button(self.ui_ButtonBox.Cancel).clicked.connect(self.cancel)
        self.action_buttons()
        self.ui_FileList.itemClicked.connect(self.show_name)

    def action_buttons(self):
        try:
            self.ui_ButtonBox.button(self.ui_ButtonBox.Open).clicked.connect(self.action)
        except AttributeError:
            pass
        try:
            self.ui_ButtonBox.button(self.ui_ButtonBox.Save).clicked.connect(self.action)
        except AttributeError:
            pass

    def browse_folder(self):
        """
        walks through all folders and selects first directory
        """
        self.ui_DirList.clear()
        self.fs = fs.open_fs(self.fs_url)
        self.ui_DirList.addItem(u'.')
        for dir_path in sorted(self.fs.listdir(u'.')):
            if self.fs.isdir(dir_path):
                self.ui_DirList.addItem(dir_path)
        self.selection_directory(0)
        self.ui_DirList.currentIndexChanged.connect(self.selection_directory)

    def selection_directory(self, i):
        """
        Fills the filenames based on file_type into a FileList

        :param i: index of selelection
        """
        self.last_index = i
        self.selected_dir = self.ui_DirList.currentText()
        self.ui_FileList.clear()
        file_type = self.ui_FileType.text()
        for item in sorted(self.fs.listdir(self.selected_dir)):
            if not self.fs.isdir(item) and match_extension(item, [file_type]):
                self.ui_FileList.addItem(item)
        if self.last_index == 0 and not self.show_save_action:
            self.ui_FileList.setCurrentRow(0)
            if self.ui_FileList.currentItem() is not None:
               self.ui_SelectedName.setText(self.ui_FileList.currentItem().text())


    def selection_file_type(self):
        """
        Action for line edit of file type
        """
        self.selection_directory(self.last_index)
        self.ui_FileList.setCurrentRow(-1)
        self.ui_SelectedName.setText(None)

    def show_name(self):
        self.filename = self.ui_FileList.item(self.ui_FileList.currentRow()).text()
        self.ui_SelectedName.setText(self.filename)

    def cancel(self):
        """
        Action on cancel button
        """
        self.close()

    def show_action(self):
        """
        changes the Open Button into a Save Button

        :param show_save_action: True for showing the Save dialog
        """
        if self.show_save_action:
            self.ui_SelectedName.setEnabled(True)
            self.ui_ButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
            if self.default_filename is not None:
                self.ui_SelectedName.setText(self.default_filename)

    def action(self):
        """
        Action on open / save button
        """
        if self.show_save_action:
            self.filename = self.ui_SelectedName.text()
            if self.filename == u"":
                return
            if self.fs.exists(fs.path.join(self.selected_dir, self.filename)):
                sel = QtWidgets.QMessageBox.question(
                    self, "Replace Filename",
                    "This will replace the filename: {0}. Continue?".format(self.filename),
                    QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
                if sel == QtWidgets.QMessageBox.Yes:
                    self.close()
            else:
                self.close()
        else:
            try:
                self.filename = self.ui_FileList.item(self.ui_FileList.currentRow()).text()
            except AttributeError:
                pass
            else:
                self.close()


def fs_filepicker(parent=None, fs_url=u'~/', file_pattern=u'*.*', title=u'FS File Picker',
                  default_filename=None, show_save_action=False):
    """
    Selects a file by FilePicker for a given pyfilesystem2 Url.

    :param parent: parent Widget
    :param fs_url: pyfilesystem2 url
    :param file_pattern: filter pattern of pyfilesystem2
    :param title: title of QtWidget
    :return: selected filename
    """
    fp = FilePicker(parent, fs_url, file_pattern, title=title,
                    default_filename=default_filename, show_save_action=show_save_action)
    fp.setModal(True)
    fp.exec_()
    filename = None
    if fp.filename is not None:
        filename = fs.path.combine(fp.fs_url, fs.path.join(fp.selected_dir, fp.filename))
    return filename

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--version", help="show version", action="store_true", default=False)
    parser.add_argument("-s", "--save", help="show save button", action="store_true", default=False)
    parser.add_argument("-d", "--default_name", help="default name for saving", default=None)
    parser.add_argument("-u", "--fs_url", help="fs url to filesystem", default=u"~/")
    parser.add_argument("-f", "--file_pattern", help="file pattern", default=u"*.*")
    parser.add_argument("-t", "--title", help="title of window", default=u'FS File Picker')

    args = parser.parse_args()
    if args.version:
        print("***********************************************************************")
        print("\n            File Picker Version \n")
        print("***********************************************************************")
        print("Version:", __version__)
        sys.exit()
    app = QtWidgets.QApplication([])
    return fs_filepicker(parent=None, fs_url=args.fs_url, file_pattern=args.file_pattern,
                         title=args.title, default_filename=args.default_name,
                         show_save_action=args.save)

if __name__ == '__main__':
    print(main())


