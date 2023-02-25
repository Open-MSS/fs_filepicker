# -*- coding: utf-8 -*-
"""

    fslib.setup
    ~~~~~~~~~~~

    setuptools script

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

# The README.txt file should be written in reST so that PyPI can use
# it to generate your project's PyPI page.
from fslib.version import __version__
from setuptools import setup, find_packages

long_description = open("README.rst").read()

setup(
    name="fs_filepicker",
    version=__version__,
    description="QT Filepicker for pyfilesystem2",
    long_description=long_description,
    classifiers="Development Status :: 5 - Production/Stable",
    keywords="fs",
    maintainer="Reimar Bauer",
    maintainer_email="rb.proj@gmail.com",
    author="Reimar Bauer",
    author_email="rb.proj@gmail.com",
    license="Apache 2.0",
    url="https://github.com/ReimarBauer/fs_filepicker",
    platforms="any",
    packages=find_packages(),
    namespace_packages=[],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "fs==2.4.16",
        "future==0.18.3",
        "humanfriendly==10.0",
        "PyQt5==5.15.7",
        ""
    ],  # we use conda build recipe
    entry_points={
        "console_scripts": [
            "fs_filepicker=fslib.fs_filepicker:main",
        ]
    },
)
