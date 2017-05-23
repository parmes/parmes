.. _solfec-examples-81array:

81 bricks array
===============

.. warning:: Under construction

This is example illustrates multiple aspects of Solfec functionality and serves as a validation test. It is also included with :ref:`TR1 <tr1>`.
The input files for this example are located in the `solfec/examples/81array <https://github.com/tkoziara/solfec/tree/master/examples/81array>`_
directory. These are:

- `README <https://github.com/tkoziara/solfec/blob/master/examples/81array/README>`_ -- a text based summary of the problem

- `81array.py <https://github.com/tkoziara/solfec/blob/master/examples/81array/81array.py>`_ -- array excitation analysis input file

- `81fbi.py <https://github.com/tkoziara/solfec/blob/master/examples/81array/81fbi.py>`_ -- fuel brick impact test input file

- `81postp.py <https://github.com/tkoziara/solfec/blob/master/examples/81array/81postp.py>`_ -- post-processing script for the 81array.py input deck

- `81array[*].inp files <https://github.com/tkoziara/solfec/blob/master/examples/81array/81array.inp>`_ -- ABAQUS input decks used by 81array.py

- `81fbi[*].inp files <https://github.com/tkoziara/solfec/blob/master/examples/81array/81fbi.inp>`_ -- ABAQUS input decks used by 81fbi.py

- `81array[*]base.pikle.gz files <https://github.com/tkoziara/solfec/blob/master/examples/81array>`_ -- saved reduced
  `POD <https://en.wikipedia.org/wiki/Principal_component_analysis>`_ base files used by 81array.py and 81fbi.py

- `FB[*].csv files <https://github.com/tkoziara/solfec/blob/master/examples/81array>`_ -- experimental results curves used by 81postp.py

- `ts81.py.bz2 file <https://github.com/tkoziara/solfec/blob/master/examples/81array>`_ -- compressed time history of a seisimic excitation signal used by 81array.py

.. _81array: https://github.com/tkoziara/solfec/tree/master/examples/81array
