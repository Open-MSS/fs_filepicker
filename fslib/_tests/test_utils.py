# -*- coding: utf-8 -*-
"""

    fslib._tests.test_utils
    ~~~~~~~~~~~~~~~~~~~~~~~

    tests fslib.utils

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

from fslib.utils import match_extension

def test_match_extensions():
    data = [(u"example.csv", [u"*.csv"], True),
            (u"example.csv", [u"*.txt"], False),
            (u"example.csv", [u"*.txt", u"*.csv"], True),
            (u"example.csv", [u"*.csv", u"*.txt"], True),
            (u"example.csv", [u"*.txt", u"*.png"], False)
           ]
    for name, pattern, state in data:
        assert match_extension(name, pattern) is state
