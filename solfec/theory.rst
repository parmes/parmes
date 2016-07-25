.. _solfec-theory:

Solfec Theory Manual
====================

Solfec implements the Non--Smooth `Contact Dynamics <https://en.wikipedia.org/wiki/Contact_dynamics>`_ Method [1]_, [2]_
and the `Discrete Element Method <https://en.wikipedia.org/wiki/Discrete_element_method>`_.  The software originated from
the PhD research [3]_ and its further development [4]_. Thesis [3]_ can be used as an auxiliary "theory manual". The intention
behind this document is to provide a minimalist exposition of core computational methods and algorithms implemented in Solfec
and facilitate cross--referencing with the functionalities described in the :ref:`User Manual <solfec-user>`. The theory manual
comprises the following sections:

.. toctree::

   theory/basics
   theory/kinematics
   theory/dynamics
   theory/timeint
   theory/locdyn
   theory/joints
   theory/conpnt
   theory/conform
   theory/solvers
   theory/materials

.. [1] `CMAME, 177(3--4):329--349, 1999. <http://www.sciencedirect.com/science/article/pii/S0045782598003879>`_
.. [2] `CMAME, 177(3--4):235--257, 1999. <http://www.sciencedirect.com/science/article/pii/S0045782598003831>`_
.. [3] `Koziara, PhD thesis, 2008. <http://theses.gla.ac.uk/429/>`_
.. [4] `IJNME, 87(1--5):437--456, 2011. <http://onlinelibrary.wiley.com/doi/10.1002/nme.3158/full>`_
