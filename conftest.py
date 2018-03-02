# -*- coding: utf-8 -*-
"""

    fslib.conftest
    ~~~~~~~~~~~~~~

    common definitions for py.test

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
from __future__ import print_function

import pytest
import fs
import fs.path
from fs.tempfs import TempFS

try:
    from pyvirtualdisplay import Display
except ImportError:
    Display = None

try:
    import git
except ImportError:
    SHA = ""
else:
    REPO = git.Repo(search_parent_directories=True)
    SHA = REPO.head.object.hexsha

ROOT_FS = TempFS(identifier=u"fs_filepicker_{}".format(SHA))
ROOT_DIR = ROOT_FS.root_path
TESTDATA_DIR = u'testdata'
SUB_DIRS = [fs.path.join(u"testdata", u"foo"),
            fs.path.join(u"testdata", u"bar"),
            fs.path.join(u"testdata", u"empty")]


def setup_testdata():
    for testdir in SUB_DIRS:
        if not ROOT_FS.exists(testdir):
            ROOT_FS.makedirs(testdir)

    data_fs = fs.open_fs(fs.path.join(ROOT_DIR, TESTDATA_DIR))
    with data_fs.open(u'example.csv', 'w') as file_object:
        file_object.write(u'testdata')
    with data_fs.open(u'example.txt', 'w') as file_object:
        file_object.write(u'testdata')
    with data_fs.open(u'foo.txt', 'w') as file_object:
        file_object.write(u'testdata')

    testdirs = [fs.path.join(u"testdata", u"foo"), fs.path.join(u"testdata", u"bar")]
    for testdir in testdirs:
        data_fs = fs.open_fs(fs.path.join(ROOT_DIR,  testdir))
        with data_fs.open(u'foo.txt', 'w') as file_object:
            file_object.write(u'testdata')


@pytest.fixture(scope="session", autouse=True)
def configure_testsetup(request):
    if Display is not None:
        # needs for invisible window output xvfb installed,
        # default backend for visible output is xephyr
        # by visible=0 you get xvfb
        VIRT_DISPLAY = Display(visible=0, size=(1280, 1024))
        VIRT_DISPLAY.start()
        yield
        VIRT_DISPLAY.stop()
    else:
        yield


class Dummy_Filepicker(object):
    def __init__(self, authentification=u"", active_url=ROOT_FS.geturl(TESTDATA_DIR), selected_dir=None,
                 filename=u"foo.txt", wparm=None, selected_file_pattern=None, show_save_action=False):
        self.authentification = authentification
        self.active_url = active_url
        self.selected_dir = selected_dir
        self.filename = filename
        self.wparm = wparm
        self.show_save_action = show_save_action
        if selected_file_pattern is None:
            self.selected_file_pattern = ["All Files (*)"]
        else:
            self.selected_file_pattern = selected_file_pattern

    def setModal(self, boolean):
        pass

    def exec_(self):
        pass


setup_testdata()
