Development
===========

This chapter will get you started with fs_filepicker development.

The fs_filepicker is written in Python.

Once a stable release is published we do only bug fixes in stable and release regulary
new minor versions. If a fix needs a API change or it is likly more a new feature you have
to make a pull request to the develop branch. Documentation of changes is done by using our
`issue tracker <https://github.com/Open-MSS/fs_filepicker/issues>`_.

When it is ready the developer version becomes the next stable.

Style guide
-----------

We generally follow pep8, with 120 columns instead of 79.


Building a development environment
----------------------------------

Using predefined docker images instead of installing all requirements
.....................................................................

You can easily use our testing docker images which have all libraries pre installed. These are based on mambaforgen.
We provide two images. In openmss/fsfp-testing-stable we have fsfp-stable-env and in openmss/fsfp-testing-develop we have fsfp-develop-env defined.


You can either mount your MSS workdir in the container or use the environment from the container as environment on your machine.


Running pytest inside the docker container
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We mount the MSS workdir into the docker container and use an env var to access the directory for running pytest on that dir. ::

    ~/workspace/fs_filepicker$ docker pull openmss/fsfp-testing-develop:latest  # get recent version
    ~/workspace/fs_filepicker$ docker run -it --mount src=`pwd`,target=`pwd`,type=bind -e FSDIR=`pwd` openmss/fsfp-testing-develop  # mount dir into container, create env var MSSDIR with dir
    (base) root@78f42ac9ded7:/# cd $FSDIR  # change directory to the mounted dir
    (base) root@78f42ac9ded7:~/workspace/fs_filepicker# conda activate fsfp-develop-env  # activate env
    (mss-stable-env) root@78f42ac9ded7:/# pytest tests  # run pytest



Use the docker env on your computer, initial setup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example shows by using mss-stable-env how to set it up for testing and development of stable branch. The images gets updates
when we have to add new dependencies or have do pinning of existing modules. On an updated image you need to redo these steps ::

    rm -rf $HOME/mambaforge/envs/fsfp-develop-env # cleanup the existing env
    mkdir $HOME/mambaforge/envs/fsfp-develop-env  # create the dir to bind to
    xhost +local:docker                           # may be needed
    docker run -it --rm --mount type=volume,dst=/opt/conda/envs/fsfp-develop-env,volume-driver=local,volume-opt=type=none,volume-opt=o=bind,volume-opt=device=$HOME/mambaforge/envs/fsfp-develop-env --network host openmss/fsfp-testing-develop # do the volume bind
    exit                                          # we are in the container, escape :)
    sudo ln -s $HOME/mambaforge/envs/fsfp-develop-env /opt/conda/envs/fsfp-develop-env # we need the origin location linked because hashbangs interpreters are with that path. (only once needed)
    conda activate fsfp-develop-env               # activate env
    cd workspace/fs_filepicker                    # go to your workspace MSS dir
    export PYTHONPATH=`pwd`                       # add it to the PYTHONPATH
    python fslib/fs_filepicker.py                 # test if the UI starts
    pytest tests                                  # run pytest


After the image was configured you can use it like a self installed env ::

    xhost +local:docker                 # may be needed
    conda activate fsfp-develop-env     # activate env
    cd workspace/fs_filepicker          # go to your workspace MSS dir
    export PYTHONPATH=`pwd`             # add it to the PYTHONPATH
    pytest tests                        # run pytest



Manual Installing dependencies
..............................

1. System requirements

  | Any system with basic configuration.
  | Operating System : Any (Windows / Linux / Mac).

2. Software requirement

  | Python
  | `Mambaforge <https://mamba.readthedocs.io/en/latest/installation.html>`_
  | `Additional Requirements <https://github.com/Open-MSS/fs_filepicker/blob/develop/requirements.d/development.txt>`_


3. Skill set

  | Knowledge of git & github
  | Python



fs_filepicker is based on the software of the conda-forge channel located. The channel is predefined in Mambaforge.

Create an environment and install the dependencies needed for the mss package::

  $ mamba create -n fsfp-develop-env
  $ mamba activate fsfp-develop-env
  $ mamba install fs_filepicker --only-deps

Compare versions used in the meta.yaml between stable and develop branch and apply needed changes.::

  $ git diff stable develop -- localbuild/meta.yaml


Install requirements for local testing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With sending a Pull Request our defined CIs do run all tests on github.
You can do run tests own system too.

For developers we provide additional packages for running tests, activate your env and run::

  $ mamba install --file requirements.d/development.txt

On linux install the `xvfb` from your linux package manager.
This is used to run tests by `pyvirtualdisplay` on a virtual display.
If you don't want tests redirected to the xvfb display just setup an environment variable::

 $ export TESTS_VISIBLE=TRUE



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


