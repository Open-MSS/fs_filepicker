Changelog
=========

Version 0.2.9
~~~~~~~~~~~~~

 - bug fix, all remaining os.path replaced by fs.path
 - set only logo if the application runs standalone
 - improved fs_file_exists

Version 0.2.8
~~~~~~~~~~~~~

 - forcedir to fs urls added
 - introduced fs_file_exists
 - path issues for windows platform fixed


Version 0.2.7
~~~~~~~~~~~~~

 - open files on double click
 - bug fix, disable open button for nonexisting preselected file
 - detect parent class and store settings based on that
 - abspath for selected filename


Version 0.2.6
~~~~~~~~~~~~~

 - feature remove once added fs directories
 - feature store/restore by QSettings of once entered fs_urls
 - feature of multiple fs_urls added

Version 0.2.5
~~~~~~~~~~~~~

 - bug fix, don't call twice listdir
 - remove not accessible names from listdir, because of bytestr

Version 0.2.4
~~~~~~~~~~~~~

   - ui element added for defining more fs urls

Version 0.2.3
~~~~~~~~~~~~~

   - select filter based on extension of default_name
   - bug fixes

Version 0.2.2
~~~~~~~~~~~~~

   - bug fix for multi types


Version 0.2.1
~~~~~~~~~~~~~

   - extensions input field changed to a QCombobox, new Syntax e.g. All Files (*)
   - list of extensions for an item e.g.  Images (*.png *.jpg)
   - seperate functions getOpenFileName, getOpenFileNameAndFilter, getSaveFileName,
     getSaveFileNameAndFilter, getExistingDirectory


Version 0.2.0
~~~~~~~~~~~~~

   - default size 700x400
   - sorting of columns implemented
   - alternating row colors
   - fs icon added to widget

Version 0.1.9
~~~~~~~~~~~~~

  - refactored "./" placeholder
  - seperated authentication from url in widget
  - grid layout used in widget
  - handle IOError and OperationFailed


Version 0.1.8
~~~~~~~~~~~~~

 - no focus for buttons
 - py2topy3 compatibilty fixed #11


Version 0.1.7
~~~~~~~~~~~~~

 - resizeable UI


Version 0.1.6
~~~~~~~~~~~~~

 - catch exception on make_dir for RO directorie
 - any cell click selects the row
 - size for directories replaced by the word Folder


Version 0.1.5
~~~~~~~~~~~~~

 - handle incorrect fs urls
 - size and modtime added to additional columns
 - on save mode rejecting an existing name does not close


Version 0.1.4
~~~~~~~~~~~~~

  - improved directory history navigation, fixes #3


Version 0.1.3
~~~~~~~~~~~~~

  - improved directory scan
  - nested directory creation fixed
  - on time consuming functions cursor changed to wait cursor
  - windows root url fixed
  - double click introduced for changing into a directory


Version 0.1.2
~~~~~~~~~~~~~

  - refactoring of amount fs open calls
  - refactored onCellClicked
  - pyqt Property for value defined
  - refactored tests


Version 0.1.1
~~~~~~~~~~~~~

   - fix, on makedir stay in selected_dir
   - navigation to other resources added, home, computer, fs
   - resizing of dialog disabled
   - test coverage improved

Version 0.1.0
-------------

   - tango icons for actions added
   - file list shows directories on same level
   - directory navigation, goto top fs url added
   - Cancel returns always None as filename

Version 0.0.9
-------------

   - refactored WidgetList to TableWidget, currently 1 column
   - fs.webdavfs module added
   - make_dir feature added
   - File Name moved above File of type, Makedir button added right of dirs, buttonbox replaced by two buttons.
     Tests and Logic adapted.

Version 0.0.8
-------------

  - fix clear selected name if file_type is changed and not save action
  - sphinx documentation introduced
  - py.test tests introduced
  - fix match_extensions to handle many extensions
  - check on save with selected dir and filename

Version 0.0.7
-------------

  - fixed if file list is empty
  - replaced walk by listdir
  - module level import of fs because of extensions

Version 0.0.6
-------------

 - default filename for storage added
 - refactoring of internal names
 - enabled SelectedName only for save
 - on save action first element of ui_FileList not highlighted
 - confirmation needed if a file should be replaced

Version 0.0.5
-------------

 - name field added, shows selected name
 - Save feature added

Version 0.0.4
-------------

 - commandline call added
 - simplified loader function
 - fixed return path
 - sorted directores and files


Version 0.0.3
-------------

 - selecting of files improved
 - filelist shows only files, matching by fnmatch
 - fs_url directory added
 - on enter selection of a file is checked
 - renamed fs_name to fs_url


Version 0.0.2
-------------

 - changed widget baseclass to QDialog of FilePicker
 - refactored ui to dialog
 - title attribute added

Version 0.0.1
-------------

- Project ininitiated

