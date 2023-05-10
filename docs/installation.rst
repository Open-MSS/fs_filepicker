Installation
============

The fs_filepicker is available as
`conda-forge <https://anaconda.org/conda-forge/fs_filepicker>`_ package.

This channel conda-forge has builds for osx-64, linux-64, win-64

The conda-forge `github organization <https://conda-forge.github.io/>`_ uses various automated continuos integration
build processes.

We recommend to use Mamba for an installation.




Install distributed version by mamba
------------------------------------

We strongly recommend to start from `Mambaforge <https://mamba.readthedocs.io/en/latest/installation.html>`_,
a community project of the conda-forge community.

As **Beginner** start with an installation of Mambaforge
- Get `mambaforge <https://github.com/conda-forge/miniforge#mambaforge>`__ for your Operation System

Install fs_filepicker
.....................

You must install fs_filepicker into a new environment to ensure the most recent
versions for dependencies. ::

    $ mamba create -n fsenv
    $ mamba activate fsenv
    (fsenv) $ mamba install fs_filepicker python
    (fsenv) $ fs_filepicker
