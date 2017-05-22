.. _solfec-examples-reduced_order-ro1:

Pipe impact
===========

This example, also included in :ref:`TR1 <tr1>`, illustrates the reduced order modeling functionality on a pipe impact problem. The input files for
this example are located in the `solfec/examples/reduced--order1 <https://github.com/tkoziara/solfec/tree/master/examples/reduced-order1>`_ directory.
These are:

- `README <https://github.com/tkoziara/solfec/blob/master/examples/reduced-order1/README>`_ -- a text based specification of the problem

- `ro1--fem--bc.py <https://github.com/tkoziara/solfec/blob/master/examples/reduced-order1/ro1-fem-bc.py>`_ -- finite element body co--rotated model

- `ro1--fem--tl.py <https://github.com/tkoziara/solfec/blob/master/examples/reduced-order1/ro1-fem-tl.py>`_ -- finite element Total Lagrangian model

- `ro1--reduced.py <https://github.com/tkoziara/solfec/blob/master/examples/reduced-order1/ro1-reduced.py>`_ -- finite element reduced order model

- `ro1--lib.py <https://github.com/tkoziara/solfec/blob/master/examples/reduced-order1/ro1-lib.py>`_ -- library functions used by other input files

- `ro1--modred.py <https://github.com/tkoziara/solfec/blob/master/examples/reduced-order1/ro1-modred.py>`_ -- calculation of a reduced
  `POD <https://en.wikipedia.org/wiki/Principal_component_analysis>`_ base

- `ro1--postp.py <https://github.com/tkoziara/solfec/blob/master/examples/reduced-order1/ro1-postp.py>`_ -- post--processing script

- `ro1--run--all.py <https://github.com/tkoziara/solfec/blob/master/examples/reduced-order1/ro1-run-all.py>`_ -- input file that runs all tests and generates all plots

- `ro1--view.py <https://github.com/tkoziara/solfec/blob/master/examples/reduced-order1/ro1-view.py>`_ -- input file suitable for use with Solfec :ref:`viewer <solfec-running>`

.. _reduced-order1: https://github.com/tkoziara/solfec/tree/master/examples/reduced-order1
