# -*- coding: utf-8 -*-
"""

    fslib._tests.test_utils
    ~~~~~~~~~~~~~~~~~~~~~~~

    tests fslib.utils

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
from datetime import datetime
from fslib.utils import (
    match_extension,
    get_extension_from_string,
    human_readable_info,
    fs_url_exists,
)


def test_human_readable_info():
    class info(object):
        modified = datetime(2018, 2, 4, 10, 10, 10)
        size = 100

    assert human_readable_info(info) == ("2018-02-04 10:10:10", "100 bytes")
    assert human_readable_info(("D", "D")) == (" ", " ")


def test_get_extension_from_string():
    data = [
        ("All Files (*)", ["*"]),
        ("(*.*)", ["*.*"]),
        ("Images (*.jpg *.png *.svg)", ["*.jpg", "*.png", "*.svg"]),
    ]
    for text, pattern in data:
        assert get_extension_from_string(text) == pattern


def test_match_extensions():
    data = [
        ("example.csv", ["*.csv"], True),
        ("example.csv", ["*.txt"], False),
        ("example.csv", ["*.txt", "*.csv"], True),
        ("example.csv", ["*.csv", "*.txt"], True),
        ("example.csv", ["*.txt", "*.png"], False),
        ("example.csv", None, True),
    ]

    for name, pattern, state in data:
        assert match_extension(name, pattern) is state


def test_fs_url_exists():
    assert fs_url_exists("~/")
