.. _solfec-user:

Solfec User Manual
==================

.. role:: red

Solfec input file is a Python source code. Python interpreter is embedded in Solfec.
At the same time Solfec extends Python by adding a number of objects and routines.
There are few general principles to remember:

* Zero based indexing is observed in routine arguments.

* Parameters after the bar | are optional. For example FUNCTION (a, b | c, d) has two optional parameters c, d.

* Passing Solfec objects to some routines empties them. This means that a variable,
  that was passed as an argument, no longer stores data. For example: let x = CREATE1 () create an object x,
  and let y = CREATE2 (x) create an object y, using x. If CREATE2 (x) empties x, then after the call x
  becomes an empty placeholder. One can use it to assign value, x = CREATE1 (), but using it as an argument,
  z = CREATE2 (x), will cause an abnormal termination. One can create a copy of an object by calling
  z = COPY (x), hence using y = CREATE2 (COPY (x)) leaves x intact.

* Routines marked as :red:`(Under development)` are functional, although they may be unstable.

Sections below document Solfec objects and routines used for their manipulation:

.. toctree::

   user/solfec
   user/body
   user/geometry
   user/materials
   user/times
   user/loads
   user/constraints
   user/solvers
   user/simulation
   user/results
   user/utilities
