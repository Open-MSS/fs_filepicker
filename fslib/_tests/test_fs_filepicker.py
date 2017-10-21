# -*- coding: utf-8 -*-
"""

    fslib._tests.test_fs_filepicker
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    tests fslib.fs_filepicker

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


import fs
import pytest

from PyQt5 import QtCore, QtWidgets, QtTest
from conftest import ROOT_FS, TESTDATA_DIR, ROOT_DIR
from fslib import fs_filepicker




class Test_Open_FilePicker(object):
    def setup(self):
        self.application = QtWidgets.QApplication([])
        self.fs_url = ROOT_FS.geturl(TESTDATA_DIR)
        self.window = fs_filepicker.FilePicker(fs_url=self.fs_url)
        self.window.show()
        QtWidgets.QApplication.processEvents()
        QtTest.QTest.qWaitForWindowExposed(self.window)
        QtWidgets.QApplication.processEvents()

    def teardown(self):
        self.application.quit()

    def test_fs_filepicker_cancel(self):
        self.window.cancel()
        filename = self.window.filename
        self.window.close()
        assert filename is None

    def test_fs_filepicker_ok(self):
        self.window.action()
        filename = self.window.filename
        self.window.close()
        data_fs = fs.open_fs(fs.path.join(ROOT_DIR, TESTDATA_DIR))
        files = []
        for item in sorted(data_fs.listdir(u'.')):
            if data_fs.isfile(item):
                files.append(item)
        assert filename == files[0]

    def test_selection_directory(self):
        self.window.ui_DirList.setCurrentIndex(1)
        self.window.selection_directory(0)
        QtWidgets.QApplication.processEvents()
        self.window.close()
        assert self.window.ui_FileList.currentItem().text() == u"foo.txt"

    def test_showname(self):
        self.window.show_name()
        self.window.close()
        assert self.window.filename == u"example.csv"



    def test_selection_file_type(self):
        self.window.file_pattern = u"*.never"
        self.window.ui_FileType.setText(u"*.never")
        QtWidgets.QApplication.processEvents()
        self.window.selection_file_type()
        QtWidgets.QApplication.processEvents()
        QtWidgets.QApplication.processEvents()
        self.window.browse_folder()
        self.window.selection_directory(0)
        QtWidgets.QApplication.processEvents()
        assert self.window.filename == None
        pytest.skip("not finished")
        self.window.ui_FileType.setText(u"*.txt")
        QtWidgets.QApplication.processEvents()
        self.window.selection_file_type()
        QtWidgets.QApplication.processEvents()
        self.window.ui_FileList.setFocus()
        QtWidgets.QApplication.processEvents()
        self.window.ui_FileList.AnyKeyPressed
        QtWidgets.QApplication.processEvents()
        self.window.action()
        QtWidgets.QApplication.processEvents()
        assert self.window.filename == u"example.txt"