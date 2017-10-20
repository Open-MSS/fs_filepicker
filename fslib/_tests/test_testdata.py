# -*- coding: utf-8 -*-
"""

    fslib._tests.testdata
    ~~~~~~~~~~~~~~~~~~~~~

    tests predefined testdata set by conftest

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

from conftest import ROOT_FS, ROOT_DIR, TESTDATA_DIR

class TestTestdata(object):
    def test_data_available(self):
        assert ROOT_FS.exists(u'.')
        data_fs = fs.open_fs(fs.path.join(ROOT_DIR, TESTDATA_DIR))
        assert len(data_fs.listdir(u'.')) == 5

    def test_dir_available(self):
        data_fs = fs.open_fs(fs.path.join(ROOT_DIR, TESTDATA_DIR))
        dirs = []
        for item in data_fs.listdir(u'.'):
            if data_fs.isdir(item):
                dirs.append(item)
        assert len(dirs) == 2
        assert u'foo' in dirs
        assert u'bar' in dirs
