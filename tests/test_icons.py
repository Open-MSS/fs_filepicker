# -*- coding: utf-8 -*-
"""

    fslib.icons._test.test_icons
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    tests icons

    This file is part of fs_filepicker.

    :copyright: Copyright 2018 Reimar Bauer
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

import os.path
from fslib.icons import icons


def test_icons():
    assert os.path.exists(icons("text-x-generic.png", origin="flaticon"))
    assert os.path.exists(icons("fs_logo.png", origin="fs"))
    assert os.path.exists(icons("folder.png", origin="flaticon"))
    assert os.path.exists(icons("search_file.png", origin="flaticon"))
    assert os.path.exists(icons("search_folder.png", origin="flaticon"))
    assert os.path.exists(icons("go-next.png", origin="tango"))
    assert os.path.exists(icons("go-previous.png", origin="tango"))
    assert os.path.exists(icons("remove.png", origin="tango"))
