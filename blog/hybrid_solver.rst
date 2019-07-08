.. post:: Apr 27, 2017
   :tags: solfec-1.0, parmec
   :author: Tomek

.. _blog-hybrid-solver:

Hybrid solver in Solfec
=======================

:ref:`Solfec's hybrid solver <solfec-command-HYBRID_SOLVER>` is now ready for testing. This solver combines the ability
of modeling non--smooth multi--body structures in Solfec (e.g. as fully resolved FE models) in conjunction with a lightweight
rigid--body/nonlinear--spring approach implemented in :ref:`PARMEC <parmec-index>`. A simple example of that can be
seen in the video below:

.. youtube:: https://www.youtube.com/watch?v=CW080-GCB1w
  :width: 486
  :height: 324

The inner three bodies (with colorful velocity map on them) are modeled in Solfec, while the outer bodies are modeled
in Parmec (used as a library from within Solfec). This type of approach can potentially help speed up calculations for
some Solfec models, where an area of interest can be fully resolved, while the remaining part of the model can be simplified
into a set of (geometry--less) rigid bodies interacting via :ref:`non--linear springs and dampers <parmec-command-SPRING>`
(defined in a tabular manner). See also :ref:`hybrid modeling examples <solfec-examples-hybrid_modeling>` where more of this
functionality is explained.
