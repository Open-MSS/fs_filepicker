# -*- coding: utf-8 -*-
"""

    fslib.utils
    ~~~~~~~~~~~~~~~~

    This module provides utils for the fslib.

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
import fnmatch


def match_extension(name, extensions=None):
    """
    Determines if a file name matches an extension

    :param name: filename to be examined
    :param extensions: fnmatch file pattern
    :return: boolean True, if match is successful
    """
    if extensions is None:
        extensions = [u"*.*"]
    state = []
    for pattern in extensions:
        state.append(fnmatch.fnmatch(name, pattern))
    return True in state
