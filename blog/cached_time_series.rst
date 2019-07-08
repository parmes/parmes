.. post:: Aug 1, 2017
   :tags: solfec-1.0
   :author: Tomek

.. _blog-cached-time-series:

Partially cached time series in Solfec
======================================

Motivated by user feedback a partially cached time series capability has been included into :ref:`solfec-1.0-index`.
This allows to use many large :ref:`TIME_SERIES <solfec-1.0-user-times>` objects without running out of
memory. To facilitate that an optional *cache* argument has been added -- please see the :ref:`documentation
<solfec-1.0-user-times>` and :ref:`example <solfec-1.0-examples-time_series>`.
