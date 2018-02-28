# -*- coding: utf-8 -*-
"""

    fslib.icons
    ~~~~~~~~~~~~

    init of fslib.icons

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
import fs.path


def icons(name, origin=u"tango"):
    return fs.path.join(fs.path.abspath(fs.path.normpath(fs.path.dirname(__file__))), origin, name)
