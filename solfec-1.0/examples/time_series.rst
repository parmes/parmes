.. _solfec-1.0-examples-time_series:

Time series
===========

This example illustrates the :ref:`TIME_SERIES <solfec-1.0-user-times>` functionality in Solfec-1.0. The input files for this example
are located in the `solfec-1.0/examples/time--series <https://github.com/tkoziara/solfec/tree/master/examples/time-series>`_ directory.
These are:

- `README <https://github.com/tkoziara/solfec/blob/master/examples/time-series/README>`_ -- a text based summary of the examples

- `basic--ts.py <https://github.com/tkoziara/solfec/blob/master/examples/time-series/basic-ts.py>`_ -- example of simple time series without a simulation

- `cached--ts.py <https://github.com/tkoziara/solfec/blob/master/examples/time-series/cached-ts.py>`_ -- example of the partially cached time series capablity

- `labeled--ts.py <https://github.com/tkoziara/solfec/blob/master/examples/time-series/labeled-ts.py>`_ -- example of the labeled time series capability

- `ts--gen.py <https://github.com/tkoziara/solfec/blob/master/examples/time-series/ts-gen.py>`_ -- generates time series data files ts--data--{1 .. 10}.txt

- `ts--data--{0 .. 10}.txt <https://github.com/tkoziara/solfec/blob/master/examples/time-series/ts-data-0.txt>`_ -- time series data files

.. _timeseries: https://github.com/tkoziara/solfec/tree/master/examples/time-series

:ref:`TIME_SERIES <solfec-1.0-user-times>` object can be used in Solfec-1.0 to prescribe time--dependent :ref:`constraints <solfec-1.0-user-constraints>` and
:ref:`loads <solfec-1.0-user-loads>`. The three minimalist input files included with this example illustrate the ways the time series can be used:
:numref:`basic-ts`, :numref:`cached-ts`, :numref:`labeled-ts` below include comments and are self--explanatory. An animated output of the *cached--ts.py*
example is included as video [1]_.

.. literalinclude:: ../../../solfec-1.0/examples/time-series/basic-ts.py
   :linenos:
   :caption: Listing of basic--ts.py
   :name: basic-ts

.. literalinclude:: ../../../solfec-1.0/examples/time-series/cached-ts.py
   :linenos:
   :caption: Listing of cached--ts.py
   :name: cached-ts

.. literalinclude:: ../../../solfec-1.0/examples/time-series/labeled-ts.py
   :linenos:
   :caption: Listing of labeled--ts.py
   :name: labeled-ts

.. [1] Animated output of the `cached--ts.py <https://github.com/tkoziara/solfec/blob/master/examples/time-series/cached-ts.py>`_
   example from :numref:`cached-ts`.

.. youtube:: https://www.youtube.com/watch?v=X9_aS4RILTA
  :width: 648
  :height: 364


