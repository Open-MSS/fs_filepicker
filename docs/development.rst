Development
============================

This chapter will get you started with fs_filepicker development.

The fs_filepicker is written in Python.

Style guide
~~~~~~~~~~~~~~~~

We generally follow pep8, with 120 columns instead of 79.


Building a development environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you want to contribute make a fork on github of `fs_filepicker <https://github.com/ReimarBauer/fs_filepicker>`_.
For building you have to use the conda recipe localy and install in a new environment.

Some of used packages are in the conda-forge channel located, so we have to add this channel to the default::

  $ conda config --add channels conda-forge

Or add the channel by an editor to the .condarc config file::

  $ more ~/.condarc
  channels:
  - defaults
  - conda-forge


On top level dir::

  $ git clone https://github.com/yourfork/fs_filepicker.git
  $ cd fs_filepicker
  $ conda create -n devenv python=2
  $ source activate devenv
  $ conda build .
  $ conda install --use-local fs_filepicker


To install some additional packages needed for running the tests, activate your virtual env and run::

  $ conda install --file requirements.d/development.txt


Running tests
~~~~~~~~~~~~~~~~~~~

We have implemented demodata as data base for testing. On first call of py.test a set of demodata becomes stored
in a /tmp/tmp* folder. If you have installed gitpython a postfix of the revision head is added.

::

   $ python -m pytest


Use the -v option to get a verbose result. By the -k option you could select one test to execute only.

A pep8 only test is done by py.test --pep8 -m pep8

Instead of running a ibrary module as a script by the -m option you may also use the py.test command.

::

   $ py.test --cov

This plugin produces a coverage report.

Profiling can be done by e.g.::

   $ python -m cProfile  -s time ./demodata.py > profile.txt



Building the docs with Sphinx
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The documentation (in reStructuredText format, .rst) is in docs/.

To build the html version of it, you need to have sphinx installed::

   cd docs/
   make html


Then point a web browser at docs/_build/html/index.html.


