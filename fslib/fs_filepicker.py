# -*- coding: utf-8 -*-
"""

    fslib.fs_filepicker
    ~~~~~~~~~~~~~~~~~~~

    This module provides the QT main window for accessing a pyfilesystem2

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

import sys
import time
import logging
import argparse
import inspect
import fs
import fs.path
from fs.opener import parse
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QAbstractItemView, QInputDialog, QErrorMessage, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSettings
from fslib import ui_filepicker, __version__
from fslib.utils import root_url, human_readable_info, match_extension, \
    FOLDER_SPACES, FILES_SPACES, WidgetImage, get_extension_from_string,\
    fs_url_exists, who_called_me
from fslib.icons import icons


class FilePicker(QtWidgets.QDialog, ui_filepicker.Ui_Dialog):
    def __init__(self, parent=None, fs_url=u"~/", file_pattern=u'All Files (*)', title=u'FS File Picker',
                 default_filename=None, show_save_action=False, show_dirs_only=False):
        super(FilePicker, self).__init__(parent)
        frame = inspect.stack()[1][0]
        self.scope = who_called_me(frame)
        self.setupUi(self)
        self.settings = QSettings("fs_filepicker", self.scope)
        self.setWindowIcon(QIcon(icons('fs_logo.png', origin='fs')))
        self.file_icon = icons('text-x-generic.png')
        self.dir_icon = icons('folder.png')
        self.selected_dir = None
        self.selected_file_pattern = None
        self.filename = None
        self.wparm = None
        self.setWindowTitle(title)
        stored_fs_url = self.settings.value("fs_urls", fs_url)
        if isinstance(fs_url, list):
            self.fs_url = fs_url[0]
            if isinstance(stored_fs_url, list):
                for _fs_url in stored_fs_url:
                    if fs_url_exists(_fs_url):
                        self.ui_fs_serverlist.addItem(_fs_url)
                for _fs_url in fs_url:
                    if fs_url_exists(_fs_url):
                        self.ui_fs_serverlist.addItem(_fs_url)
        else:
            if isinstance(stored_fs_url, list):
                for _fs_url in stored_fs_url:
                    if fs_url_exists(_fs_url):
                        self.ui_fs_serverlist.addItem(_fs_url)
            else:
                self.ui_fs_serverlist.hide()
            self.fs_url = fs_url
        self.fs_home_url = u"~/"
        self.fs_root_url = root_url()
        self.active_url = self.fs_url
        self.authentification = None
        self.parent_url = self.fs_url
        self.fs = None
        self.file_list_items = []
        self.directory_history = []
        self.last_index = 0
        self.last_dir_index = 0
        self.default_filename = default_filename
        self.file_pattern = file_pattern
        self.show_save_action = show_save_action
        self.show_dirs_only = show_dirs_only
        self.button_icons()
        self.show_action()
        self.configure()
        self.fs_button()
        self.ui_FileType.currentIndexChanged.connect(self.selection_file_type)
        self.ui_SelectedName.textChanged.connect(self.selection_name)
        self.ui_Cancel.clicked.connect(self.cancel)
        self.action_buttons()
        self.ui_FileList.itemClicked.connect(self.show_name)
        self.ui_mkdir.clicked.connect(self.make_dir)
        self.ui_history_top.clicked.connect(self.history_top)
        self.ui_history_previous.clicked.connect(self.history_previous)
        self.ui_history_next.clicked.connect(self.history_next)
        self.ui_home.clicked.connect(self.home_button)
        self.ui_root.clicked.connect(self.root_button)
        self.ui_fs.clicked.connect(self.fs_button)
        self.ui_other_fs.clicked.connect(self.other_fs_button)
        self.ui_FileList.cellClicked.connect(self.onCellClicked)
        self.ui_FileList.cellDoubleClicked.connect(self.onCellDoubleClicked)
        self.ui_FileList.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui_DirList.currentIndexChanged.connect(self.selection_directory)

        self.ui_fs_serverlist.clicked.connect(self.fs_select_other)
        self.ui_fs_serverlist.customContextMenuRequested.connect(self.fs_select_other_context)
        # ToDo check order of calls
        self.active_url = self.fs_url
        self.select_fs()

    def configure(self):
        if isinstance(self.file_pattern, list):
            stored_file_type = self.settings.value("selected_file_pattern", self.file_pattern[0])
            try:
                index = self.file_pattern.index(stored_file_type)
            except ValueError:
                index = 0
            for pattern in self.file_pattern:
                self.ui_FileType.addItem(pattern)
            self.ui_FileType.setCurrentIndex(index)
        else:
            self.ui_FileType.addItems([self.file_pattern])
        if self.default_filename is not None:
            name, extension = self.default_filename.split('.')
            idx = 0
            for pattern in self.file_pattern:
                if u".{}".format(extension) in pattern:
                    self.ui_FileType.setCurrentIndex(idx)
                idx += 1
        if self.show_dirs_only:
            self.ui_label_filename.hide()
            self.ui_label_filetype.hide()
            self.ui_FileType.hide()
            self.ui_SelectedName.hide()

    def button_icons(self):
        """
        Set icon image to button
        """
        self.ui_history_top.setText("")
        self.ui_history_top.setIcon(QIcon(icons('go-top.png')))
        self.ui_history_next.setText("")
        self.ui_history_next.setIcon(QIcon(icons('go-next.png')))
        self.ui_history_previous.setText("")
        self.ui_history_previous.setIcon(QIcon(icons('go-previous.png')))
        self.ui_mkdir.setText("")
        self.ui_mkdir.setIcon(QIcon(icons('folder-new.png')))
        self.ui_home.setText("")
        self.ui_home.setIconSize(QtCore.QSize(64, 64))
        self.ui_home.setIcon(QIcon(icons('go-home.png')))
        self.ui_root.setText("")
        self.ui_root.setIconSize(QtCore.QSize(64, 64))
        self.ui_root.setIcon(QIcon(icons('computer.png')))
        self.ui_fs.setText("")
        self.ui_fs.setIconSize(QtCore.QSize(64, 64))
        if self.scope == u"fs_filepicker":
            self.ui_fs.setIcon(QIcon(icons('fs_logo.png', origin=u'fs')))
        self.ui_other_fs.setText("")
        self.ui_other_fs.setIconSize(QtCore.QSize(64, 64))
        self.ui_other_fs.setIcon(QIcon(icons('goto-other-computer.png')))

    def home_button(self):
        """
        Action home button
        """
        self.active_url = self.fs_home_url
        self.select_fs()

    def root_button(self):
        """
        Action root button
        """
        self.active_url = self.fs_root_url
        self.select_fs()

    def fs_button(self):
        """
        Action fs button
        """
        self.active_url = fs.path.forcedir(self.fs_url)
        self.select_fs()

    def other_fs_button(self):
        fs_url, ok = QInputDialog.getText(self, 'Other FS Urls', 'Enter FS Url:')
        if ok:
            if fs_url_exists(fs_url):
                self.ui_fs_serverlist.setVisible(True)
                all_urls = [self.ui_fs_serverlist.item(idx).text() for idx in range(self.ui_fs_serverlist.count())]
                if fs_url not in all_urls:
                    self.ui_fs_serverlist.addItem(fs_url)
                self.save_settings()
            else:
                msg = u'"%s" Url not valid' % fs_url
                QErrorMessage(self).showMessage(msg)
                logging.info(msg)

    def fs_select_other(self):
        url = self.ui_fs_serverlist.currentItem().text()
        # ToDo needs a check for archives
        self.active_url = fs.path.forcedir(url)
        self.select_fs()

    def fs_select_other_context(self):
        """
        simple context option, removes item from list
        """
        url = self.ui_fs_serverlist.currentItem().text()
        selected = QMessageBox.information(self, u"Remove FS Dir", url, QMessageBox.Ok | QMessageBox.Cancel)
        if selected == QMessageBox.Ok:
            self.ui_fs_serverlist.clear()
            for item in self.settings.value("fs_urls"):
                if item != url:
                    self.ui_fs_serverlist.addItem(item)
            self.save_settings()

    def select_fs(self):
        """
        loads the selected fs to the file list ui
        """
        self.directory_history = []
        self.wparm = None
        if self.fs:
            self.fs.close()
        try:
            self.fs = fs.open_fs(self.active_url)
        except IOError:
            logging.error(u"{} does not exist!".format(self.active_url))
            exit()
        try:
            parseresult = parse(self.active_url)
        except fs.opener.errors.ParseError:
            parseresult = None
        if parseresult is not None and parseresult.username is not None:
            self.authentification = "{}:{}@".format(parseresult.username, parseresult.password)
            self.active_url = self.active_url.replace(self.authentification, u"")
        self.browse_folder()

    def action_buttons(self):
        """
        Open / Save button action connect
        """
        try:
            self.ui_Action.clicked.connect(self.action)
        except AttributeError:
            pass

    def browse_folder(self, subdir=u"."):
        """
        list folder in drop down
        """
        if self.show_save_action:
            self.ui_Action.setEnabled(True)
        if self.show_dirs_only:
            self.ui_Action.setEnabled(True)
        self.ui_DirList.clear()
        if subdir == u".":
            _sub_dir = self.active_url
        else:
            _sub_dir = subdir
        if len(self.directory_history) == 0:
            self.directory_history.append(_sub_dir)
        for item in reversed(self.directory_history):
            self.ui_DirList.addItem(item)
        self.ui_DirList.setCurrentIndex(self.last_dir_index)

    def selection_directory(self):
        """
        Fills the filenames based on file_type into a FileList, also directories
        """
        if not self.show_save_action:
            self.ui_SelectedName.setText(None)
        QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        self.selected_dir = self.ui_DirList.currentText()
        self.ui_FileList.clearContents()
        file_type = self.ui_FileType.currentText()
        self.file_list_items = []
        self.dir_list_items = []
        self.ui_FileList.verticalHeader().setVisible(False)
        self.ui_FileList.horizontalHeader().setVisible(True)
        self.ui_FileList.setHorizontalHeaderLabels([u'Name', u'Size', u'Modified'])
        self.ui_FileList.setShowGrid(False)
        self.ui_FileList.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)

        if self.selected_dir == self.active_url:
            _sel_dir = u""
        else:
            _sel_dir = self.selected_dir
        # on clearing ui_DirList also index changes and makes an additional call of that method
        if self.ui_DirList.count() > 0:
            try:
                names = self.fs.listdir(_sel_dir)
                # cleanup not valid names
                # ToDo improve make those problematic files not clickable
                for item in names:
                    _item = fs.path.combine(_sel_dir, item)
                    try:
                        self.fs.isdir(_item)
                    except (TypeError, fs.errors.PermissionDenied):
                        names.remove(item)
                        logging.error("item name %s removed from list" % item)
                for item in sorted(names):
                    _item = fs.path.combine(_sel_dir, item)
                    try:
                        self.selected_file_pattern = get_extension_from_string(file_type)
                        if not self.fs.isdir(_item) and match_extension(item, self.selected_file_pattern):
                            if not self.show_dirs_only:
                                info = self.get_info(_item)
                                self.file_list_items.append({_item: info})
                        elif self.fs.isdir(_item):
                            info = self.get_info(_item)
                            self.dir_list_items.append({_item: info})
                    except (fs.errors.PermissionDenied, fs.errors.OperationFailed):
                        logging.info(u"can't access {}".format(item))
            except UnicodeDecodeError as e:
                logging.error(u"Error: {}".format(e))

        self.ui_FileList.setRowCount(len(self.file_list_items) + len(self.dir_list_items))
        index = 0
        for item in self.dir_list_items:
            self.table_row(item, index, self.dir_icon, FOLDER_SPACES, folder=True)
            index = index + 1
        for item in self.file_list_items:
            self.table_row(item, index, self.file_icon, FILES_SPACES, folder=False)
            index = index + 1
        if self.last_index == 0 and not self.show_save_action:
            self.ui_FileList.clearSelection()
            if self.ui_FileList.currentItem() is not None:
                self.ui_SelectedName.setText(self.ui_FileList.currentItem().text())
        self.ui_FileList.resizeRowsToContents()
        QtWidgets.QApplication.restoreOverrideCursor()

    def table_row(self, item, index, icon, spaces, folder):
        info = list(item.values())[0]
        _mod_time, _size = human_readable_info(info)
        if folder:
            _size = u"Folder"
        self.ui_FileList.setCellWidget(index, 0, WidgetImage(fs.path.basename(list(item)[0]),
                                                             icon, item))
        time.sleep(0.001)
        _item = " " * spaces + fs.path.basename(list(item)[0])
        self.ui_FileList.setItem(index, 0, QtWidgets.QTableWidgetItem(_item))
        self.ui_FileList.setItem(index, 1, QtWidgets.QTableWidgetItem(_size))
        self.ui_FileList.setItem(index, 2, QtWidgets.QTableWidgetItem(_mod_time))

    def get_info(self, _item):
        try:
            info = self.fs.getinfo(_item, namespaces=[u'details', u'access', u'stat'])
            time.sleep(0.001)
        except (fs.errors.ResourceNotFound, UnicodeEncodeError):
            info = None
        return info

    @QtCore.pyqtSlot(int, int)
    def onCellClicked(self, row, column):
        """
        Action for ui_FileList WidgetImageText
        :param row: position
        :param column: position
        """
        # Any cell click is always in column 0
        column = 0
        self.wparm = self.ui_FileList.cellWidget(row, column)
        if self.wparm is not None:
            if "text" in self.wparm.img:
                self.ui_SelectedName.setText(self.wparm.text)
            if self.show_dirs_only and "folder" in self.wparm.img:
                self.ui_SelectedName.setText(self.wparm.text)

    @QtCore.pyqtSlot(int, int)
    def onCellDoubleClicked(self, row, column):
        """
        Action for ui_FileList WidgetImageText on doubleclick
        :param row: position
        :param column: position
        """
        column = 0
        self.wparm = self.ui_FileList.cellWidget(row, column)
        try:
            if self.wparm is not None:
                if "folder" in self.wparm.img:
                    self.directory_history.append(list(self.wparm.value.keys())[0])
                    self.browse_folder(subdir=list(self.wparm.value.keys())[0])
                    if not self.show_save_action:
                        self.ui_SelectedName.setText(None)
                    self.selection_name()
                if "text" in self.wparm.img:
                    self.ui_SelectedName.setText(self.wparm.text)
                    self.action()
        except AttributeError:
            pass

    def selection_file_type(self):
        """
        Action for line edit of file type
        """
        self.selection_directory()
        self.ui_FileList.clearSelection()
        if not self.show_save_action:
            self.ui_SelectedName.setText(None)
        if self.show_save_action:
            text = self.ui_SelectedName.text()
            new_text = text.split('.')[0]
            self.ui_SelectedName.setText(new_text)

    def selection_name(self):
        """
        Action for filename changes, line edit text input
        """
        if not self.show_save_action and not self.show_dirs_only:
            self.ui_Action.setEnabled(False)
        self.filename = self.ui_SelectedName.text()
        dirname = fs.path.forcedir(u'.')
        if self.wparm is not None:
            _dirname = fs.path.forcedir(u'.')
            if self.wparm.value == u'{}{}'.format(_dirname, self.wparm.text):
                dirname = fs.path.dirname(u'{}{}'.format(_dirname, self.wparm.text))
            else:
                dirname = self.selected_dir
        if not self.show_dirs_only:
            _filename = fs.path.combine(dirname, self.filename)
            _file_names = [list(name)[0] for name in self.file_list_items]
            if dirname == fs.path.forcedir(u'.'):
                _file_names = [fs.path.combine(dirname, list(name)[0]) for name in self.file_list_items]
            if _filename in _file_names:
                self.ui_Action.setEnabled(True)
                index = _file_names.index(_filename) + len(self.dir_list_items)
                self.ui_FileList.selectRow(index)
            else:
                if not self.show_save_action:
                    self.ui_Action.setEnabled(False)
                self.ui_FileList.clearSelection()

    def show_name(self):
        """
        Action for showing clicked name as filename
        """
        try:
            self.filename = self.ui_SelectedName.text()
        except AttributeError:
            self.filename = u""
        if self.filename != u"":
            self.ui_SelectedName.setText(self.filename)
            info = self.get_info(self.filename)
            if info is not None and info.is_file:
                self.ui_Action.setEnabled(True)

    def cancel(self):
        """
        Action on cancel button
        """
        self.filename = None
        self.close()

    def show_action(self):
        """
        Changes the Open Button into a Save Button

        :param show_save_action: True for showing the Save dialog
        """
        if self.show_save_action:
            self.ui_SelectedName.setEnabled(True)
            self.ui_Action.setText("Save")
            if self.default_filename is not None:
                self.ui_SelectedName.setText(self.default_filename)
        if self.show_dirs_only:
            self.ui_SelectedName.setEnabled(True)
            self.ui_Action.setText("Get Directory")

    def make_dir(self):
        """
        Shows the make dir dialog und creates a new directory
        """
        new_dir_name, ok = QtWidgets.QInputDialog.getText(self, u"New Folder", u"Enter a new folder name:",
                                                          QtWidgets.QLineEdit.Normal, "")
        if ok:
            if self.wparm is None:
                dirname = u''
            else:
                dirname = self.selected_dir
            new_dir = fs.path.combine(dirname, new_dir_name)
            if not self.fs.isdir(new_dir):
                try:
                    self.fs.makedir(new_dir)
                except fs.errors.ResourceNotFound:
                    logging.error(u"Can't create {}".format(new_dir))
                self.last_dir_index = list(reversed(self.directory_history)).index(self.selected_dir)
                self.browse_folder(subdir=self.selected_dir)
            else:
                ok = QtWidgets.QMessageBox.warning(self, u"New Folder", u"Can't create this Folder: {}".format(new_dir))

    def history_top(self):
        """
        Action for top dir in history_list
        """
        self.browse_folder(self.active_url)
        if not self.show_save_action:
            self.ui_SelectedName.setText(None)
        self.selection_name()

    def history_next(self):
        """
        Action for next dir in history_list
        """
        index = list(reversed(self.directory_history)).index(self.selected_dir) - 1
        if index >= 0:
            self.ui_DirList.setCurrentIndex(index)
        if not self.show_save_action:
            self.ui_SelectedName.setText(None)
        self.selection_name()

    def history_previous(self):
        """
        Action for previous dir in history_list
        """
        index = list(reversed(self.directory_history)).index(self.selected_dir) + 1
        if index < len(self.directory_history):
            self.ui_DirList.setCurrentIndex(index)
        if not self.show_save_action:
            self.ui_SelectedName.setText(None)
        self.selection_name()

    def action(self):
        """
        Action on Open / Save button
        """
        self.filename = self.ui_SelectedName.text()
        if self.filename == u"":
            return

        if self.filename is not None:
            dirname = fs.path.forcedir(u'.')
            if self.wparm is not None:
                dirname = self.selected_dir
            if dirname.startswith(self.active_url):
                filename = u"{}{}".format(fs.path.forcedir(self.active_url), self.filename)
            else:
                # We can't use fs.path.join and also not fs.path.abspath because of protocol url
                filename = u"{}{}{}".format(fs.path.forcedir(self.active_url),
                                            fs.path.forcedir(dirname), self.filename)
            filename = filename.replace(fs.path.forcedir(u'.'), u'')
        if self.show_save_action and not self.show_dirs_only:
            self.save_settings()
            self.filename = self.ui_SelectedName.text()
            if self.filename == u"":
                return
            info = self.get_info(fs.path.split(filename)[1])
            if info is not None and info.is_dir:
                sel = QtWidgets.QMessageBox.warning(
                    self, u"Warning",
                    u"You can't create a file with this name: {0}".format(self.filename),
                    QtWidgets.QMessageBox.No)
            elif info is not None and info.is_file:
                sel = QtWidgets.QMessageBox.question(
                    self, u"Replace Filename",
                    u"This will replace the filename: {0}. Continue?".format(self.filename),
                    QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
                if sel == QtWidgets.QMessageBox.Yes:
                    self.filename = filename
                    self.close()
                else:
                    pass
            else:
                self.filename = filename
                self.close()
        else:
            self.filename = filename
            self.close()

    def save_settings(self):
        items = []
        for index in xrange(self.ui_fs_serverlist.count()):
            items.append(self.ui_fs_serverlist.item(index).text())
        self.settings.setValue('fs_urls', items)
        selected_file_pattern = self.ui_FileType.currentText()
        self.settings.setValue("selected_file_pattern", selected_file_pattern)
        self.settings.sync()


def fs_filepicker(parent=None, fs_url=u'~/', file_pattern=u'All Files (*)', title=u'FS File Picker',
                  default_filename=None, show_save_action=False, show_dirs_only=False):
    """
    Selects a file by FilePicker for a given pyfilesystem2 Url.

    :param parent: parent Widget
    :param fs_url: pyfilesystem2 url
    :param file_pattern: filter pattern of pyfilesystem2
    :param title: title of QtWidget
    :return: selected filename
    """
    fp = FilePicker(parent, fs_url, file_pattern, title=title,
                    default_filename=default_filename, show_save_action=show_save_action,
                    show_dirs_only=show_dirs_only)
    fp.setModal(True)
    fp.exec_()
    active_url = fp.active_url
    if fp.authentification is not None:
        try:
            parseresult = parse(fp.active_url)
        except fs.opener.errors.ParseError:
            parseresult = None
        if parseresult is not None:
            active_url = u"{}://{}{}".format(parseresult.protocol, fp.authentification, parseresult.resource)
    filename = None
    selected_file_pattern = None
    if fp.filename is not None:
        filename = fp.filename.replace(fp.active_url, active_url)
        try:
            selected_file_pattern = fp.selected_file_pattern[0]
        except TypeError:
            selected_file_pattern = file_pattern
    return filename, selected_file_pattern


def getOpenFileName(parent=None, fs_url=u'~/', file_pattern=u'All Files (*)', title=u'FS File Picker', **options):
    return fs_filepicker(parent, fs_url, file_pattern, title=title)[0]


def getOpenFileNameAndFilter(parent=None, fs_url=u'~/', file_pattern=u'All Files (*)',
                             title=u'FS File Picker', **options):
    return fs_filepicker(parent, fs_url, file_pattern, title=title)


def getSaveFileName(parent=None, fs_url=u'~/', file_pattern=u'All Files (*)', title=u'FS File Picker',
                    default_filename=None, show_save_action=True, **options):
    return fs_filepicker(parent, fs_url, file_pattern, title,
                         default_filename, show_save_action)[0]


def getSaveFileNameAndFilter(parent=None, fs_url=u'~/', file_pattern=u'All Files (*)', title=u'FS File Picker',
                             default_filename=None, show_save_action=True, **options):
    return fs_filepicker(parent, fs_url, file_pattern, title,
                         default_filename, show_save_action)


def getExistingDirectory(parent=None, fs_url=u'~/', title=u'FS File Picker', show_dirs_only=True, **options):
    return fs_filepicker(parent, fs_url, title=title, show_dirs_only=show_dirs_only)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--version", help="show version", action="store_true", default=False)
    parser.add_argument("-s", "--save", help="show save button", action="store_true", default=False)
    parser.add_argument("-fo", "--folder", help="show folders only", action="store_true", default=False)
    parser.add_argument("-d", "--default_name", help="default name for saving", default=None)
    parser.add_argument("-u", "--fs_url", help="fs url to filesystem", default=u"~/")
    parser.add_argument("-f", "--file_pattern", help="file pattern", default=u"All Files (*)")
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
                         show_save_action=args.save, show_dirs_only=args.folder)[0]
    # ToDO, solve this without del
    del app


if __name__ == '__main__':
    print(main())
