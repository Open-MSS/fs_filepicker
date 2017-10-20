Installation
=================

Current Releases of fs_filepicker are based on *python 2* or *python 3*.

.. image:: https://anaconda.org/conda-forge/fs_filepicker/badges/installer/conda.svg


Install distributed version by conda
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Anaconda <https://www.continuum.io/why-anaconda>`_ provides an enterprise-ready data analytics
platform that empowers companies to adopt a modern open data science analytics architecture.

The fs_filepicker is available as anaconda package on a channel.

 * `conda-forge <https://anaconda.org/conda-forge/mss>`_

The conda-forge packages are based on defaults and other conda-forge packages.
This channel conda-forge has builds for osx-64, linux-64, win-64, win-32.


The conda-forge `github organization <https://conda-forge.github.io/>`_ uses various automated continuos integration
build processes.


conda-forge channel
+++++++++++++++++++++

Please add the channel conda-forge to your defaults::

  $ conda config --add channels conda-forge
  $ conda config --add channels defaults

The last channel added gets on top of the list. This gives the order: First search in default packages
then in conda-forge.

Then you could choose between as system wide installation or one in a prefered environment::

   $ conda install fs_filepicker

You also could install this project into an environment. ::

   $ conda create -n env python=2
   $ source activate env
   $ conda install fs_filepicker


