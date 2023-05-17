# -*- coding: utf-8 -*-
"""

    fslib.utils
    ~~~~~~~~~~~~~~~~

    This module provides utils for the fslib.

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
import fnmatch
import sys
import humanfriendly
import re
import fs
import fs.path
import inspect

from PyQt5.QtCore import pyqtProperty
from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout, QTableWidgetItem
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

FOLDER_SPACES = 11
FILES_SPACES = 12


def who_called_me(frame):
    _, _, _, value_dict = inspect.getargvalues(frame)
    try:
        return str(value_dict["parent"]).split()[0].split("<__main__.")[1]
    except (KeyError, IndexError):
        return "fs_filepicker"


def get_extension_from_string(text):
    try:
        pattern = re.search(r"\((.*?)\)", text).group(1)
    except AttributeError:
        return ".*"
    pattern = pattern.split()
    if isinstance(pattern, list):
        return pattern
    else:
        return [pattern]


def match_extension(name, extensions=None):
    """
    Determines if a file name matches an extension

    :param name: filename to be examined
    :param extensions: fnmatch file pattern
    :return: boolean True, if match is successful
    """
    if extensions is None:
        extensions = ["*.*"]
    state = []
    for pattern in extensions:
        state.append(fnmatch.fnmatch(name, pattern))
    return True in state


def root_url():
    if sys.platform.startswith("win"):
        return "file:///"
    else:
        return "/"


def human_readable_info(info):
    try:
        _mod_time = info.modified.strftime("%Y-%m-%d %H:%M:%S")
    except (AttributeError, TypeError):
        _mod_time = " "
    try:
        _size = humanfriendly.format_size(info.size)
    except (AttributeError, TypeError):
        _size = " "
    return _mod_time, _size


def fs_url_exists(fs_url):
    """
    verifies for a valid fs url

    :param fs_url: fs_url string
    :return: boolean
    """
    try:
        fs.open_fs(fs_url)
    except fs.errors.CreateFailed:
        return False
    return True


class WidgetImage(QWidget):
    # inspired by
    # https://stackoverflow.com/questions/45896291/how-to-show-image-and-text-at-same-cell-in-qtablewidget-in-pyqt
    # slightly modified
    def __init__(self, text, img, value, parent=None):
        QWidget.__init__(self, parent)
        self._text = text
        self._img = img
        self._value = value
        self.setLayout(QHBoxLayout())
        self.lbPixmap = QLabel(self)
        self.lbModtime = QLabel(self)
        self.layout().addWidget(self.lbPixmap)
        self.initUi()

    def initUi(self):
        self.lbPixmap.setPixmap(
            QPixmap(self._img).scaled(self.lbPixmap.size(), Qt.KeepAspectRatio)
        )

    @pyqtProperty(str)
    def img(self):
        return self._img

    @pyqtProperty(str)
    def text(self):
        return self._text

    @pyqtProperty(str)
    def value(self):
        return self._value


class TableWidgetItem(QTableWidgetItem):
    def __lt__(self, y):
        """
        sorting by directories/files and by uppercase
        whatsThis is used for classification
        :return: boolean
        """
        if self.whatsThis() + self.text().upper() < self.whatsThis() + y.text().upper():
            return True
        return False
