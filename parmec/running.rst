.. _parmec-running:

Running Parmec
==============

PARMEC is a command line program. Typical usage:

#. Include parmec directory into your PATH variable.

#. Create a directory where your input/output files will be stored (e.g. *mkdir test*).

#. Edit your `Python <http://www.python.org/>`__ input file in this
   directory (e.g. *test.py*); See :ref:`input commands <parmec-input_commands>`.

#. Run PARMEC (e.g. *parmec4 path/to/test/test.py*, or *parmec8
   path/to/test/test.py*).

#. Time histories can be generated during analysis using the
   :ref:`HISTORY command <parmec-command-HISTORY>`;

#. Upon termination output files are created in the same directory
   (e.g. *path/to/test/test.dump*);

#. The output files can be viewed with `OVITO <http://www.ovito.org>`__,
   `ParaView <http://www.paraview.org>`__, or
   `VisIt <https://wci.llnl.gov/simulation/computer-codes/visit>`__;
   See the :ref:`OUTPUT command <parmec-command-OUTPUT>`.
