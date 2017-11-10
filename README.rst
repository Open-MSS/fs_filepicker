fs_filepicker
~~~~~~~~~~~~~


|Source| |Conda| |Codecov| |Codacy| |License|

.. |Source| image:: https://img.shields.io/badge/source-GitHub-303030.svg?maxAge=300&style=flat-square
   :target: https://github.com/ReimarBauer/fs_filepicker

.. |Conda| image:: https://anaconda.org/conda-forge/fs_filepicker/badges/installer/conda.svg
   :target: https://anaconda.org/conda-forge/fs_filepicker

.. |License| image:: https://anaconda.org/conda-forge/fs_filepicker/badges/license.svg
   :target: https://choosealicense.com/licenses/apache-2.0/

.. |Codecov| image:: https://codecov.io/gh/ReimarBauer/fs_filepicker/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/ReimarBauer/fs_filepicker


This project is based on `PyFilesystem2 <http://pyfilesystem2.readthedocs.io/>`_
As fs_url you can enter any valid url which the fs.open_fs accepts.

The examples shows the setup for Open and Save.

Open
----

Standalone example::

  from fslib.fs_filepicker import fs_filepicker
  filename = fs_filepicker(parent=None, fs_url=u'~/', file_pattern=u'*.*',
                           title=u'Open Config File')
  print(filename)


As modal widget snippet::

  from fslib.fs_filepicker import fs_filepicker
  filename = fs_filepicker(self, fs_url=u'ftp.debian.org/debian', u'*.*', title=u"Debian files")


Save
----

Example::

  filename = fs_filepicker(parent=None, fs_url=u'~/', file_pattern=u'*.json', default_filename=u'config.json',
                           show_save_action=True, title=u'Save Config File')
