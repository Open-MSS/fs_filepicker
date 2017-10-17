fs_filepicker
~~~~~~~~~~~~~

This project is based on `PyFilesystem2 <http://pyfilesystem2.readthedocs.io/>`_
As fs_url you can enter any valid url which the fs.open_fs accepts.


Standalone example::
  from fslib.fs_filepicker import fs_filepicker
  filename = fs_filepicker(parent=None, fs_url=u'~/', file_pattern=u'*.*',
                           title=u'Open Config File')
  print(filename)


As modal widget snippet::
  from fslib.fs_filepicker import fs_filepicker
  filename = fs_filepicker(self, fs_url=u'ftp.debian.org/debian', u'*.*', title=u"Debian files")
