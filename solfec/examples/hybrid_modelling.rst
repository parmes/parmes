.. _solfec-examples-hybrid_modelling:

Hybrid modeling
===============

By hybrid modeling we mean multi--body modeling combining rigid bodies connected
via springs with finite--element bodies interacting via non--smooth laws. For certain
class of problems, this type of modeling can be useful, allowing for shorter runtime,
in cases where solely non--smooth models could be computationally prohibitive. For example,
when analyzing frequency response of a large scale multi--body structure, certain fraction
of it (an area of interest) can be modelled by means of the NSCD approach, while the remaining
(predominate) part can be modeled in a simplified manner.

In the current example we analyse elastic cubes subject to a sine sweep excitation.
First, we look into a two--body problem, based on which we find out equivalent spring and
dashpot parameters, for a simplified model representing a non--smooth model of two elastic
interacting blocks. Second, we look into a many--body problem, where such equivalent properties
are used for a one--dimensional chain of :math:`n` cubes. Finally, we look into a generalization
of the problem into a three--dimensional array of :math:`n \times n \times n` cubes.

Stages of model creation, modeling rationale, comparison of results between non--smooth, simplified
and hybrid cases, as well as, comparison of run times and parallel scaling, are detailed in the
following two sections.

Two cubes
---------

Statics
+++++++

Non--smooth model
_________________

Simplified model 
_________________

Dynamics
++++++++

Non--smooth model
_________________

Simplified model 
_________________

Chain of cubes
--------------

Non--smooth model
+++++++++++++++++

Simplified model 
++++++++++++++++

Hybrid model
++++++++++++

Comparison
++++++++++

Array of cubes
--------------

Non--smooth model
+++++++++++++++++

Simplified model
++++++++++++++++

Hybrid model
++++++++++++

Comparison
++++++++++
