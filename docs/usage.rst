fs_filepicker QT GUI
====================

The executable for the user interface application is "**fs_filepicker**".
At the current state this is only for checking if the packages are all installed.

fs_filepicker is based on `PyFilesystem2 <http://pyfilesystem2.readthedocs.io/>`_ and is a QT application.
So as fs_url you can enter any valid url which the fs.open_fs accepts.

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

Standalone example::

  filename = fs_filepicker(parent=None, fs_url=u'~/', file_pattern=u'*.json', default_filename=u'config.json',
                           show_save_action=True, title=u'Save Config File')


As modal widget snippet::

  from fslib.fs_filepicker import fs_filepicker
  filename = fs_filepicker(self, fs_url=u'~/', file_pattern=u'*.json', default_filename=u'config.json',
                           show_save_action=True, title=u'Save Config File')

