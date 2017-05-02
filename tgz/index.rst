.. _tgz-index:

parmes.tar.gz 
=============

On a Unix system, you can download:

* `parmes.tar.gz file <https://drive.google.com/uc?export=download&id=0B0lQ6Rj8GeMVWk9ZTEtTeTZ5YVE>`_

and unpack it into a ``parmes`` directory by typing:

::

  tar -xzvf parmes.tar.gz

You can edit files:

* ``parmes/config/dynlb/Config.mak``

* ``parmes/config/parmec/Config.mak``

* ``parmes/config/solfec/Config.mak``

in order to set up compilation flags and paths. Then, you can enter the ``parmec`` directory and type:

::

    make

This will update the entire source code tree and recompile all software. **Note, that all local changes inside of the parmes directory will be lost.**
Serial, shared memory parallel, and MPI parallel versions of the software are all compiled by default.

The ``parmec/Makefile`` also supports the following targets:

* ``make update`` to only update the source tree; this will also clean all object and executable files

* ``make compile`` to compile everything

* ``make clean`` to clean all object and executable files

* ``make code-update``, ``make code-compile``, ``make code-clean`` to update, compile and clean a particular ``code`` -- one of: ``dynlb``, ``parmec``, ``solfec``
