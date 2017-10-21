# -*- coding: utf-8 -*-
"""

    fslib.conftest
    ~~~~~~~~~~~~~~

    common definitions for py.test

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
from __future__ import print_function



import pytest
import fs
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
SUB_DIRS = [u'testdata/foo', u'testdata/bar']
    
def setup_testdata():
    for dir in SUB_DIRS:
        if not ROOT_FS.exists(dir):
            ROOT_FS.makedirs(dir)

    data_fs = fs.open_fs(fs.path.join(ROOT_DIR, TESTDATA_DIR))
    with data_fs.open(u'example.csv', 'w') as file_object:
        file_object.write(u'testdata')
    with data_fs.open(u'example.txt', 'w') as file_object:
        file_object.write(u'testdata')
    with data_fs.open(u'foo.txt', 'w') as file_object:
        file_object.write(u'testdata')

    for dir in SUB_DIRS:
        data_fs = fs.open_fs(fs.path.join(ROOT_DIR,  dir))
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


setup_testdata()