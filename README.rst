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
  from fs import open_fs, path
  from fslib.fs_filepicker import FilePicker
  ....
      dlg = FilePicker(self, fs_url=u'ftp.debian.org/debian', u'*.*', title=u"Debian files")
      dlg.setModal(True)
      dlg.exec_()
      fs_filename = path.combine(dlg.fs_url, dlg.filename)
