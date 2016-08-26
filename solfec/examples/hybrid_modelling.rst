.. _solfec-examples-hybrid_modelling:

Hybrid modeling
===============

By hybrid modeling we mean multi--body modeling combining rigid bodies connected
via springs with finite--element bodies interacting via non--smooth laws. For certain
class of problems, this type of modeling can be useful, allowing for shorter runtime,
in cases where solely non--smooth models could be computationally prohibitive. For example,
when analyzing frequency response of a large scale multi--body structure, certain fraction
of it (an area of interest) could be modelled using the NSCD approach, while the remaining
(predominate) part could be modeled in a simplified manner (rigid bodies + springs).
