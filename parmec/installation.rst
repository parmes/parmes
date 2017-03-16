.. _parmec-installation:

Parmec Installation
===================

Clone parmec sources from `GitHub <https://github.com/tkoziara/parmec>`__:

::

  git clone https://github.com/tkoziara/parmec

Enter parmec directory:

::

  cd parmec

Edit Makefile variables:

::

  # C++ compiler (ISPC is assumed to be in the PATH; http://ispc.github.io)
  CXX=g++

  # Python paths
  PYTHONINC=-I/usr/include/python2.7
  PYTHONLIB=-L/usr/lib -lpython2.7

  # HDF5 paths
  HDF5INC=-I/usr/include
  HDF5LIB=-L/usr/lib -lhdf5 -lhdf5\_hl

  # Debug version
  DEBUG=no

Compile sources:

::

  make

Parmec executable files are:

::

  parmec4 (single precision)
  parmec8 (double precision)

Parmec library files are:

::

  libparmec4.a, parmec4.h (single precision library, header)
  libparmec8.a, paremc8.h (double precision library, header)

To update parmec type:

:: 

  make clean
  git pull
  make
