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

import mock
import fs
import pytest

from PyQt5 import QtWidgets, QtTest
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

    @mock.patch("fslib.fs_filepicker.QtWidgets.QDialogButtonBox.Cancel",
                 return_value=None)
    def test_fs_filepicker_cancel(self, mockcancel):
        assert self.window.filename is None

    @mock.patch("fslib.fs_filepicker.QtWidgets.QDialogButtonBox.Open",
                return_value=u"example.csv")
    def test_fs_filepicker_ok(self, mockopen):
        pytest.skip("not finished")
        data_fs = fs.open_fs(fs.path.join(ROOT_DIR, TESTDATA_DIR))
        files = []
        for item in data_fs.listdir(u'.'):
            if data_fs.isfile(item):
                files.append(item)
        assert self.window.filename == files[0]


