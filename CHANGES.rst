Changelog
=========

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

