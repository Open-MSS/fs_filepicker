# -*- coding: utf-8 -*-
"""

    fslib._tests.test_fs_filepicker
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    tests fslib.fs_filepicker

    This file is part of fs_filepicker.

    :copyright: Copyright 2017-2018 Reimar Bauer
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
import fs.path
import pytest

from PyQt5 import QtWidgets, QtTest
from conftest import ROOT_FS, TESTDATA_DIR, ROOT_DIR, SUB_DIRS, Dummy_Filepicker
from fslib import fs_filepicker
from fslib.fs_filepicker import fs_filepicker as fsfp
from fslib.fs_filepicker import main as fsmain


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

    def test_fs_filepicker_nothing_selected_ok(self):
        self.window.action()
        filename = self.window.filename
        self.window.close()
        assert filename == u""

    def test_fs_filepicker_files_selected_ok(self):
        data_fs = fs.open_fs(fs.path.join(ROOT_DIR, TESTDATA_DIR))
        for item in sorted(data_fs.listdir(u'.')):
            if data_fs.isfile(item):
                self.window.ui_SelectedName.setText(item)
                QtWidgets.QApplication.processEvents()
                self.window.selection_name()
                QtWidgets.QApplication.processEvents()
                assert self.window.filename == item
        self.window.close()

    def test_selection_directory(self):
        index = sorted(SUB_DIRS).index(fs.path.join(u"testdata", u"foo"))
        self.window.ui_FileList.selectRow(index)
        QtWidgets.QApplication.processEvents()
        self.window.onCellDoubleClicked(index, 0)
        QtWidgets.QApplication.processEvents()
        self.window.selection_directory()

        QtWidgets.QApplication.processEvents()
        QtWidgets.QApplication.processEvents()
        self.window.action()
        _file_names = [list(name)[0] for name in self.window.file_list_items]
        assert fs.path.join(u"foo", u"foo.txt") in _file_names
        assert len(self.window.file_list_items) == 1

    def test_showname_close(self):
        self.window.show_name()
        self.window.close()
        assert self.window.filename == u""

    def test_showname_on_filename(self):
        self.window.show_name()
        filename = u"example.csv"
        _file_names = [list(name)[0] for name in self.window.file_list_items]
        all_items = self.window.dir_list_items + _file_names
        index = all_items.index(filename)
        self.window.ui_FileList.selectRow(index)
        QtWidgets.QApplication.processEvents()
        self.window.onCellClicked(index, 0)
        QtWidgets.QApplication.processEvents()
        self.window.show_name()
        self.window.close()
        assert self.window.filename == fs.path.basename(filename)

    def test_selection_file_type(self):
        self.window.file_pattern = u"Does not exist (*.never)"
        self.window.ui_FileType.addItem(self.window.file_pattern)
        QtWidgets.QApplication.processEvents()
        self.window.selection_file_type()
        QtWidgets.QApplication.processEvents()
        QtWidgets.QApplication.processEvents()
        self.window.browse_folder()
        self.window.selection_directory()
        QtWidgets.QApplication.processEvents()
        assert self.window.filename is None
        self.window.ui_FileType.addItem(u"Text Files (*.txt)")
        QtWidgets.QApplication.processEvents()
        self.window.selection_file_type()
        QtWidgets.QApplication.processEvents()
        self.window.ui_FileList.setFocus()
        QtWidgets.QApplication.processEvents()
        self.window.ui_SelectedName.setText(u"example.txt")
        QtWidgets.QApplication.processEvents()
        self.window.action()
        QtWidgets.QApplication.processEvents()
        assert self.window.filename == u"example.txt"

    def test_subdirectory(self):
        _folder_names = [list(name)[0] for name in self.window.dir_list_items]
        index = _folder_names.index(u'bar')
        self.window.onCellDoubleClicked(index, 0)
        QtWidgets.QApplication.processEvents()
        _file_names = [list(name)[0] for name in self.window.file_list_items]
        assert _file_names[0] == fs.path.join(u"bar", u"foo.txt")
        self.window.onCellClicked(0, 0)
        QtWidgets.QApplication.processEvents()
        self.window.action()
        QtWidgets.QApplication.processEvents()
        self.window.close()
        assert self.window.filename == "foo.txt"

    def test_onCellClicked(self):
        self.window.onCellDoubleClicked(0, 0)
        QtWidgets.QApplication.processEvents()
        self.window.close()
        _file_names = [list(name)[0] for name in self.window.file_list_items]
        assert u"bar" in self.window.ui_DirList.currentText()
        assert fs.path.join(u"bar", u"foo.txt") in _file_names

    def test_selectedFileBeforeSelectingDir(self):
        """
        on Open the Action button has to become disabled if the other directory don't have a preselected file
        """
        _names = [list(name)[0] for name in self.window.dir_list_items + self.window.file_list_items]
        index = _names.index(u'example.csv')
        self.window.onCellClicked(index, 0)
        QtWidgets.QApplication.processEvents()
        _folder_names = [list(name)[0] for name in self.window.dir_list_items]
        index = _folder_names.index(u'bar')
        self.window.onCellDoubleClicked(index, 0)
        QtWidgets.QApplication.processEvents()
        assert self.window.ui_Action.isEnabled() is False

    def test_selectFileinSubDir_andChangeDir(self):
        _folder_names = [list(name)[0] for name in self.window.dir_list_items]
        index = _folder_names.index(u'bar')
        self.window.onCellDoubleClicked(index, 0)
        QtWidgets.QApplication.processEvents()
        _file_names = [list(name)[0] for name in self.window.file_list_items]
        sel_name = _file_names[0]
        assert sel_name == u"bar/foo.txt"
        self.window.onCellClicked(0, 0)
        QtWidgets.QApplication.processEvents()
        self.window.history_previous()
        QtWidgets.QApplication.processEvents()
        _file_names = [list(name)[0] for name in self.window.file_list_items]
        result = sel_name in _file_names
        # history previous, name not there
        assert self.window.ui_Action.isEnabled() is result
        index = _folder_names.index(u'bar')
        self.window.onCellDoubleClicked(index, 0)
        QtWidgets.QApplication.processEvents()
        _file_names = [list(name)[0] for name in self.window.file_list_items]
        sel_name = self.window.ui_SelectedName.text()
        assert sel_name == u""
        assert self.window.ui_Action.isEnabled() is False

    def test_open_file_on_doubleClick(self):
        _names = [list(name)[0] for name in self.window.dir_list_items + self.window.file_list_items]
        index = _names.index(u'example.csv')
        self.window.onCellDoubleClicked(index, 0)
        QtWidgets.QApplication.processEvents()
        assert self.window.filename == "example.csv"


class Test_Save_FilePicker(object):
    def setup(self):
        self.application = QtWidgets.QApplication([])
        self.fs_url = ROOT_FS.geturl(TESTDATA_DIR)
        self.window = fs_filepicker.FilePicker(fs_url=self.fs_url, show_save_action=True)
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

    def test_filename_cancel(self):
        self.window.ui_SelectedName.setText(u"example.txt")
        QtWidgets.QApplication.processEvents()
        self.window.action()
        QtWidgets.QApplication.processEvents()
        self.window.cancel()
        QtWidgets.QApplication.processEvents()
        filename = self.window.filename
        self.window.close()
        assert filename is None

    def test_filename_save_newname(self):
        self.window.ui_SelectedName.setText(u"newexample.txt")
        QtWidgets.QApplication.processEvents()
        self.window.action()
        QtWidgets.QApplication.processEvents()
        self.window.close()
        filename = self.window.filename
        self.window.close()
        assert filename == u"newexample.txt"

    def test_filename_high_light_by_selectedname(self):
        index = sorted(SUB_DIRS).index(fs.path.join(u"testdata", u"foo"))
        self.window.ui_FileList.selectRow(index)
        QtWidgets.QApplication.processEvents()
        self.window.onCellDoubleClicked(index, 0)
        QtWidgets.QApplication.processEvents()
        self.window.ui_SelectedName.setText(u'foo.txt')
        QtWidgets.QApplication.processEvents()
        self.window.selection_name()
        QtWidgets.QApplication.processEvents()
        index = self.window.ui_FileList.selectedIndexes()[0].row()
        self.window.close()
        assert index == 0

    def test_default_filename(self):
        self.window.default_filename = u"abc.txt"
        self.window.show_action()
        QtWidgets.QApplication.processEvents()
        self.window.action()
        QtWidgets.QApplication.processEvents()
        self.window.close()
        filename = self.window.filename
        self.window.close()
        assert filename == u"abc.txt"

    def test_save_in_empty_dir(self):
        index = sorted(SUB_DIRS).index(fs.path.join(u"testdata", u"empty"))
        self.window.ui_FileList.selectRow(index)
        QtWidgets.QApplication.processEvents()
        self.window.onCellDoubleClicked(index, 0)
        QtWidgets.QApplication.processEvents()
        self.window.selection_directory()
        self.window.ui_SelectedName.setText(u"example.txt")
        QtWidgets.QApplication.processEvents()
        self.window.action()
        QtWidgets.QApplication.processEvents()
        self.window.close()
        assert list(self.window.wparm.value)[0] == u"empty"
        assert u"example.txt" in self.window.filename

    @mock.patch("fslib.fs_filepicker.QtWidgets.QInputDialog.getText",
                return_value=(u"exampledir", True))
    def test_makedir(self, mocktext):
        index = sorted(SUB_DIRS).index(fs.path.join(u"testdata", u"empty"))
        self.window.ui_FileList.selectRow(index)
        QtWidgets.QApplication.processEvents()
        self.window.onCellDoubleClicked(index, 0)
        QtWidgets.QApplication.processEvents()
        self.window.make_dir()
        QtWidgets.QApplication.processEvents()
        self.window.close()
        _folder_names = [list(name)[0] for name in self.window.dir_list_items]
        assert fs.path.join(u"empty", u"exampledir") in _folder_names

    @mock.patch("fslib.fs_filepicker.QtWidgets.QInputDialog.getText",
                return_value=(u"thisexampledir", True))
    def test_history_makedir(self, mocktext):
        _folder_names = [list(name)[0] for name in self.window.dir_list_items]
        index = _folder_names.index(u'empty')
        self.window.onCellDoubleClicked(index, 0)
        QtWidgets.QApplication.processEvents()
        self.window.history_previous()
        index = _folder_names.index(u'bar')
        self.window.onCellDoubleClicked(index, 0)
        QtWidgets.QApplication.processEvents()
        self.window.history_previous()
        assert self.window.ui_DirList.currentText() == 'empty'
        QtWidgets.QApplication.processEvents()
        self.window.make_dir()
        QtWidgets.QApplication.processEvents()
        _folder_names = [list(name)[0] for name in self.window.dir_list_items]
        self.window.close()
        assert fs.path.join(u"empty", u"thisexampledir") in _folder_names
        assert self.window.last_dir_index == 1


class Test_Save_FilePicker_default(object):
    def setup(self):
        self.application = QtWidgets.QApplication([])
        self.fs_url = ROOT_FS.geturl(TESTDATA_DIR)
        self.window = fs_filepicker.FilePicker(fs_url=[self.fs_url, TESTDATA_DIR], show_save_action=True,
                                               file_pattern=[u'All Files (*)', u'CSV Files (*.csv)'],
                                               default_filename="result.txt")
        self.window.show()
        QtWidgets.QApplication.processEvents()
        QtTest.QTest.qWaitForWindowExposed(self.window)
        QtWidgets.QApplication.processEvents()

    def teardown(self):
        self.application.quit()

    def test_default_filename(self):
        self.window.close()
        assert self.window.default_filename == u"result.txt"

    @mock.patch("fslib.fs_filepicker.QtWidgets.QMessageBox.warning",
                return_value=QtWidgets.QMessageBox.No)
    @mock.patch("fslib.fs_filepicker.QtWidgets.QMessageBox.question",
                return_value=QtWidgets.QMessageBox.Yes)
    def test_action(self, mockwarning, mockinformation):
        self.window.ui_SelectedName.setText(u"foo")
        QtWidgets.QApplication.processEvents()
        assert self.window.show_save_action is True
        self.window.action()
        assert QtWidgets.QMessageBox.No
        self.window.ui_SelectedName.setText(u"example.csv")
        QtWidgets.QApplication.processEvents()
        self.window.action()
        QtWidgets.QApplication.processEvents()
        assert QtWidgets.QMessageBox.Yes
        tmp_filename = u"{}{}".format(fs.path.forcedir(u'.'), u"example.csv")
        assert self.window.filename[7:] == fs.path.join(ROOT_DIR, TESTDATA_DIR, fs.path.forcedir(u'.'), tmp_filename)


class Test_FilePicker_dirs(object):
    def setup(self):
        self.application = QtWidgets.QApplication([])
        self.fs_url = ROOT_FS.geturl(TESTDATA_DIR)
        self.window = fs_filepicker.FilePicker(fs_url=self.fs_url, show_save_action=True, show_dirs_only=True)
        self.window.show()
        QtWidgets.QApplication.processEvents()
        QtTest.QTest.qWaitForWindowExposed(self.window)
        QtWidgets.QApplication.processEvents()

    def teardown(self):
        self.application.quit()

    def test_show_action(self):
        assert self.window.ui_Action.text() == u"Get Directory"
        assert self.window.ui_Action.isEnabled() is True

    def test_select_directory(self):
        self.window.ui_FileList.selectRow(0)
        QtWidgets.QApplication.processEvents()
        self.window.onCellClicked(0, 0)
        QtWidgets.QApplication.processEvents()
        self.window.action()
        name = self.window.filename
        self.window.close()
        assert name.endswith(u'bar')


class Test_MoreUrls(object):
    def setup(self):
        self.application = QtWidgets.QApplication([])
        self.fs_url = [ROOT_FS.geturl(_dir) for _dir in SUB_DIRS]
        self.fs_url.append(fs.path.join(u"never", u"never", u"exists"))
        self.window = fs_filepicker.FilePicker(fs_url=self.fs_url)
        self.window.show()
        QtWidgets.QApplication.processEvents()
        QtTest.QTest.qWaitForWindowExposed(self.window)
        QtWidgets.QApplication.processEvents()

    def teardown(self):
        self.application.quit()

    def test_dirs(self):
        items = []
        for index in xrange(self.window.ui_fs_serverlist.count()):
            items.append(self.window.ui_fs_serverlist.item(index).text())
        cmp_items = ','.join(items)
        self.window.close()
        assert SUB_DIRS[0] in cmp_items.replace(u"\\", u"/")
        assert SUB_DIRS[1] in cmp_items.replace(u"\\", u"/")
        assert SUB_DIRS[2] in cmp_items.replace(u"\\", u"/")
        assert fs.path.join(u"never", u"never", u"exists") not in cmp_items


class Test_Filepicker(object):
    def setup(self):
        self.application = QtWidgets.QApplication([])
        self.fs_url = [ROOT_FS.geturl(_dir) for _dir in SUB_DIRS]

    def teardown(self):
        self.application.quit()

    def test_fsfp_nothing_selected(self):
        result = fsfp(parent=None, fs_url=self.fs_url)
        assert result == (None, None)

    fp = Dummy_Filepicker(authentification=u"",
                          filename=u"foo.txt",
                          selected_file_pattern=[u"All Files (*)"],
                          selected_dir=SUB_DIRS[0],
                          wparm=u"something")

    @mock.patch("fslib.fs_filepicker.FilePicker", return_value=fp)
    def test_fsfp_fileselected(self, mockresult):
        fn, tf = fsfp(parent=None, fs_url=self.fs_url)
        assert fn.startswith(u'file://')
        assert u'testdata/foo/foo.txt' in fn
        assert tf == 'All Files (*)'

    @mock.patch("fslib.fs_filepicker.fs_filepicker", return_value=[None])
    def test_main_call(self, mockresult):
        pytest.skip("won't work with coverage")
        assert fsmain() is None


class Test_Navigation(object):
    def setup(self):
        self.other_fs_url = [ROOT_FS.geturl(_dir) for _dir in SUB_DIRS]
        self.application = QtWidgets.QApplication([])
        self.fs_url = ROOT_FS.geturl(TESTDATA_DIR)
        self.window = fs_filepicker.FilePicker(fs_url=self.fs_url)
        self.window.show()
        QtWidgets.QApplication.processEvents()
        QtTest.QTest.qWaitForWindowExposed(self.window)
        QtWidgets.QApplication.processEvents()

    def teardown(self):
        self.application.quit()

    @mock.patch("fslib.fs_filepicker.QtWidgets.QInputDialog.getText",
                return_value=(ROOT_FS.geturl(TESTDATA_DIR), True))
    def test_other_fs_button(self, mockinput):
        self.window.other_fs_button()
        items = [self.window.ui_fs_serverlist.item(index).text()
                 for index in xrange(self.window.ui_fs_serverlist.count())]
        self.window.close()
        assert self.fs_url in items

    @mock.patch("fslib.fs_filepicker.QtWidgets.QInputDialog.getText",
                return_value=(ROOT_FS.geturl(TESTDATA_DIR), True))
    def test_fs_select_other(self, mockinput):
        self.window.other_fs_button()
        items = [self.window.ui_fs_serverlist.item(index).text()
                 for index in xrange(self.window.ui_fs_serverlist.count())]
        index = items.index(self.fs_url)
        self.window.ui_fs_serverlist.setCurrentRow(index)
        QtWidgets.QApplication.processEvents()
        self.window.fs_select_other()
        self.window.close()
        assert self.window.wparm is None
        assert self.window.fs._closed is False

    @mock.patch("fslib.fs_filepicker.QtWidgets.QInputDialog.getText",
                return_value=(ROOT_FS.geturl(TESTDATA_DIR), True))
    @mock.patch("fslib.fs_filepicker.QtWidgets.QMessageBox.information",
                return_value=(QtWidgets.QMessageBox.Ok))
    def test_fs_select_other_context(self, mockinput, mockremove):
        self.window.other_fs_button()
        items = [self.window.ui_fs_serverlist.item(index).text()
                 for index in xrange(self.window.ui_fs_serverlist.count())]
        assert self.fs_url in items
        _index = items.index(self.fs_url)
        self.window.ui_fs_serverlist.setCurrentRow(_index)
        QtWidgets.QApplication.processEvents()
        self.window.fs_select_other_context()
        items = [self.window.ui_fs_serverlist.item(index).text()
                 for index in xrange(self.window.ui_fs_serverlist.count())]
        self.window.close()
        assert self.fs_url not in items
