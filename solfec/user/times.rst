.. |br| raw:: html

  <br />

.. _solfec-user-times:

Time series
===========

An object of type TIME_SERIES is a linear spline based on a series of 2-points.

.. topic:: obj = TIME_SERIES (points | label, cache)

  This routine creates a TIME_SERIES object.

  * obj -- created TIME_SERIES object

  * points -- either a list [t0, v0, t1, v1, ....] or a list of lists [[t0,v0], [t1,v1], ...]
    of points (where ti < tj, when i < j), or a path to a file storing times and values pairs in format:

    # comment 1 ... |br|
    # comment 2 ... |br|
    t0 v0 |br|
    t1 v1 |br|
    # comment 3 ... |br|
    t2 v2 |br|
    ... |br|

  * label -- optional label string; if a label is provided than the TIME_SERIES object is stored in
    memory just once; this facilitates more optimal memory usage in cases where many identical
    TIME_SERIES objects are used in multiple constraints (for example); the label should be unique;
    **Note:** labeled time series should be declared globally on all MPI ranks and must not be defined
    within if blocks dependent on the :ref:`HERE(...) <solfec-command-HERE>` command

  * cache -- optional partial cache size; if **points** = file path and **cache** > 0 then only the
    cache size of points is stored in memory at any given time; this helps to save memory in case of
    a need for many large time series objects; default: 0 (entire time series is stored in memory)

Some parameters can also be accessed as members of a TIME_SERIES object, cf. :numref:`times-params`.

.. _times-params:

.. table:: TIME_SERIES object parameters.

  +---------------------------------------------------------------------------------------------------------+
  | **Read only members:**                                                                                  |
  +---------------------------------------------------------------------------------------------------------+
  | **obj.times** - list [t0, t1, ...] storing times                                                        |
  +---------------------------------------------------------------------------------------------------------+
  | **obj.values** - list [v0, v1, ...] storing values                                                      |
  +---------------------------------------------------------------------------------------------------------+
  | **obj.derivative** - returns a TIME_SERIES object representing a derivative of the current object       |
  +---------------------------------------------------------------------------------------------------------+
  | **obj.integral** - returns a TIME_SERIES object representing an integral of the current object          |
  +---------------------------------------------------------------------------------------------------------+
