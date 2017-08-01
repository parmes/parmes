.. _solfec-examples-time_series:

Time series
===========

This example illustrates the :ref:`TIME_SERIES <solfec-user-times>` functionality in Solfec. The input files for this example
are located in the `solfec/examples/time--series <https://github.com/tkoziara/solfec/tree/master/examples/time-series>`_ directory.
These are:

- `README <https://github.com/tkoziara/solfec/blob/master/examples/time-series/README>`_ -- a text based summary of the examples

- `basic--ts.py <https://github.com/tkoziara/solfec/blob/master/examples/time-series/basic-ts.py>`_ -- example of simple time series without a simulation

- `cached--ts.py <https://github.com/tkoziara/solfec/blob/master/examples/time-series/cached-ts.py>`_ -- example of the partially cached time series capablity

- `labeled--ts.py <https://github.com/tkoziara/solfec/blob/master/examples/time-series/labeled-ts.py>`_ -- example of the labeled time series capability

- `ts--gen.py <https://github.com/tkoziara/solfec/blob/master/examples/time-series/ts-gen.py>`_ -- generates time series data files ts--data--{1 .. 10}.txt

- `ts--data--{0 .. 10}.txt <https://github.com/tkoziara/solfec/blob/master/examples/time-series/ts-data-0.txt>`_ -- time series data files

.. _timeseries: https://github.com/tkoziara/solfec/tree/master/examples/time-series

:ref:`TIME_SERIES <solfec-user-times>` object can be used in Solfec to prescribe time--dependent :ref:`constraints <solfec-user-constraints>` and
:ref:`loads <solfec-user-loads>`. The three minimalist input files included with this example illustrate the ways the time series can be used:
:numref:`basic-ts`, :numref:`cached-ts`, :numref:`labeled-ts` below include comments and are self--explanatory. An animated output of the *cached--ts.py*
example is included as video [1]_.

.. literalinclude:: ../../../solfec/examples/time-series/basic-ts.py
   :linenos:
   :caption: Listing of basic--ts.py
   :name: basic-ts

.. literalinclude:: ../../../solfec/examples/time-series/cached-ts.py
   :linenos:
   :caption: Listing of cached--ts.py
   :name: cached-ts

.. literalinclude:: ../../../solfec/examples/time-series/labeled-ts.py
   :linenos:
   :caption: Listing of labeled--ts.py
   :name: labeled-ts

.. [1] Animated output of the `cached--ts.py <https://github.com/tkoziara/solfec/blob/master/examples/time-series/cached-ts.py>`_
   example from :numref:`cached-ts`.

.. youtube:: https://www.youtube.com/watch?v=X9_aS4RILTA
  :width: 648
  :height: 364


