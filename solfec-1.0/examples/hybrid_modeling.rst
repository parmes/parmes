.. _solfec-1.0-examples-hybrid_modeling:

Hybrid modeling
===============

By hybrid modeling we mean multi--body modeling combining rigid bodies connected
via springs with finite--element or rigid bodies interacting via non--smooth laws. For some
problems, this type of modeling can be useful, allowing for shorter runtime, in cases where
solely non--smooth models could be computationally prohibitive. For example, when analyzing
frequency response of a large scale multi--body structure, a fraction of it (an area of interest)
could be modeled using the NSCD approach, while the remaining (predominate) part could be modeled
in a simplified manner (using rigid bodies and springs).

Hybrid modeling is available in Solfec-1.0 via the :ref:`HYBRID_SOLVER <solfec-1.0-command-HYBRID_SOLVER>`
interface.  In this case :ref:`Parmec <parmec-index>` is used as a software library facilitating
modeling of the rigid body -- spring systems. Currently available examples of the hybrid modeling
functionality include:

.. toctree::
  :maxdepth: 1

  hybrid_modeling/hs0
  hybrid_modeling/hs123
  hybrid_modeling/hs3_scaling
