.. _solfec-installation:

Solfec-1.0 Installation
=======================

Solfec-1.0 is hosted on `GitHub <https://github.com/tkoziara/solfec>`_ and you will need the *git* command
installed in order to download its source code. Have a look at https://git-scm.com for instructions.
Once the git command is available at your command line, type

::

  git clone https://github.com/tkoziara/solfec.git

This will create a *solfec* directory in your current directory. The next thing you need is a Make/C/C++/Fortran/Python
development environment at your command line. Users of Unix type systems (e.g. Linux, FreeBSD, Mac OS X) may use a package
manager to install those tools. Windows users can install `Cygwin <http://www.cygwin.com/>`_ or `Mingw <http://mingw-w64.org>`_ instead.
Solfec-1.0 is written in C and it uses a simple makefile to get compiled.
The file *solfec-1.0/Config.mak* needs to be modified in order to set up library paths and compilation flags. Here is an example:

.. literalinclude:: ../../solfec-1.0/Config.mak

The above configuration works on Mac OS X. To recap, what you need is:

* C, C++, FORTRAN 95 compilers

* `HDF5 library <http://www.hdfgroup.org>`_

* (optional, deprecated) XDR (standard part of RPC on all Unix type systems)

* `BLAS and LAPACK <http://www.netlib.org/lapack/>`_ libraries (standard on most systems)

* Python together with development files and libraries (versions 2.x have been tested)

* OpenGL libraries and developments files (this enables Solfec-1.0's viewer)

* (optional) VBO (Vertex Buffer Object extension of OpenGL for faster rendering)

* MPI libraries and development files

* either `Zoltan <http://www.cs.sandia.gov/Zoltan/>`_ or `dynlb <https://github.com/tkoziara/dynlb>`_ load balancing library

* (optional) :ref:`Parmec <parmec-index>` source path if you wish to use the :ref:`HYBRID_SOLVER <solfec-command-HYBRID_SOLVER>`
  and :ref:`hybrid modeling <solfec-examples-hybrid_modeling>`

* (optional) `Siconos <http://siconos.gforge.inria.fr>`_ contact solvers library

To compile Solfec-1.0, after editing the Config.mak file, the first compilation may look like this

::

  cd solfec
  make all

This will create files *solfec-1.0/solfec* and *solec/solfec-mpi*, that is, the serial and the parallel versions of the code.
For every subsequent update and compilation you may like to do the following

* Back up your Config.mak file. For example

::

  cd solfec
  cp Config.mak ..

* Now update the sources

::

  git pull

* Recover your Config.mak file

::

  mv ../Congig.mak ./

* And finally compile again

::

  make clean
  make all

Use “DEBUG = no” most of the time: this will make Solfec-1.0 about 40% faster.
Nonetheless, when you experience trouble with running the code, recompile it with “DEBUG = yes”
(this is slower but outputs more information) and run it again.
The solfec-1.0/inp directory contains example input files. If you haven't used the “POSIX = yes” flag,
you will need to create output directories yourself, before running calculations (on systems where “POSIX = yes” works,
this is done automatically). It may be convenient to modify the PATH variable to point to the *solfec* directory,
making it easier to run Solfec-1.0 form any location within your filesystem.
You can ask for help, using the `Solfec-1.0 mailing list <http://groups.google.com/group/solfec>`_.
