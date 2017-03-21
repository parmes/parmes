:orphan:

.. _solfec-examples-hybrid_modelling:

Hybrid modeling
===============

By hybrid modeling we mean multi--body modeling combining rigid bodies connected
via springs with finite--element or rigid bodies interacting via non--smooth laws. For some
problems, this type of modeling can be useful, allowing for shorter runtime, in cases where
solely non--smooth models could be computationally prohibitive. For example, when analyzing
frequency response of a large scale multi--body structure, a fraction of it (an area of interest)
could be modelled using the NSCD approach, while the remaining (predominate) part could be modeled
in a simplified manner (using rigid bodies and springs).

Hybrid modeling is available in Solfec via the :ref:`HYBRID_SOLVER <hybrid-solver>` interface.
In this case :ref:`Parmec <parmec-index>` is used as a software library facilitating modeling
of the rigid body -- spring systems. :ref:`HYBRID_SOLVER <hybrid-solver>` is supported both in the serial
and MPI version of Solfec. The Parmec library is shared memory parallel and in the MPI mode this part of
modeling is executed on MPI rank 0 process, employing maximum available shared memory parallelism.

Currently available examples of the hybrid modelling functionality include:

.. toctree::
  :maxdepth: 1

  hybrid_modelling/hs0
