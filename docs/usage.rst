fs_filepicker QT GUI
====================

The executable for the user interface application is "**fs_filepicker**".
At the current state this is only for checking if the packages are all installed.

fs_filepicker is based on `PyFilesystem2 <http://pyfilesystem2.readthedocs.io/>`_ and is a QT application.
So as fs_url you can enter any valid url which the fs.open_fs accepts.

The examples shows the setup for Open and Save.

Examples::

  from PyQt5 import QtWidgets
  app = QtWidgets.QApplication([])
  from fslib.fs_filepicker import getOpenFileName, getSaveFileName, getExistingDirectory, getOpenFileNameAndFilter, \
                                  getSaveFileNameAndFilter
  filename = getOpenFileName(parent=None, fs_url=u'~/', file_pattern=u'All Files (*)',
                           title=u'Open Config File')
  print(filename)

  patterns = [u'All Files (*)', u'Config Files (*.json)']
  filename = getSaveFileName(parent=None, fs_url=u'~/', file_pattern=patterns,
                             default_filename=u'config.json',
                             title=u'Save Config File')
  print(filename)

  dirname = getExistingDirectory(parent=None, fs_url=u'~/')
  print(dirname)

  patterns = [u'Data Files (*.xml)', u'Config Files (*.json)']
  filename, pattern = getOpenFileNameAndFilter(parent=None, fs_url=u'~/', file_pattern=patterns)
  print(filename, pattern)

  patterns = [u'Data Files (*.xml)', u'Config Files (*.json)']
  filename, pattern = getSaveFileNameAndFilter(parent=None, fs_url=u'~/', file_pattern=patterns)
  print(filename, pattern)

  def load_file(self):
      from fslib.fs_filepicker import getOpenFileName
      filename = getOpenFileName(self, fs_url=u'ftp://ftp.de.debian.org/debian', file_pattern=u'All Files (*)',
                                 title=u"Debian files")
