.. _solfec-index:

SOLFEC
======

**Website:** https://parmes.org/solfec

**Blog authors:** `Tomek <../blog/author/tomek.html>`_

**Kind:** open-source

.. raw:: html
  
  <iframe src="https://ghbtns.com/github-btn.html?user=parmes&repo=solfec&type=watch&count=true&size=large&v=2"
  allowtransparency="true" frameborder="0" scrolling="0" width="200px" height="35px"></iframe>

Solfec implements instances of the Non--Smooth `Contact Dynamics <https://en.wikipedia.org/wiki/Contact_dynamics>`_
Method [1]_, [2]_ and the `Discrete Element Method <https://en.wikipedia.org/wiki/Discrete_element_method>`_ using
MPI, C, Python and several 3rd party codes written in C/C++/Fortran. It includes mesh, convex polyhedra,
sphere and ellipsoid based shapes, linear elastic first order finite elements, pseudo-rigid and rigid
kinematics, velocity based Signorini--Coulomb contact/impact law, and a parallel time stepping combined
with a simple dynamic load balancing. Solfec has been developed as a part of research [3]_, and it continues
to be developed and maintained since.

More details can be found in:

.. toctree::
   :maxdepth: 1

   Installation <installation>
   Running <running>
   User Manual <user>
   Theory Manual <theory>
   Validation Manual <validation>
   XDMF export <xdmf>
   Applications <applications>
   Examples <examples>
   Google group <https://groups.google.com/forum/#!forum/solfec>
..   ABAQUS import <abaqus>

References:

.. [1] `CMAME, 177(3--4):329--349, 1999. <http://www.sciencedirect.com/science/article/pii/S0045782598003879>`_
.. [2] `CMAME, 177(3--4):235--257, 1999. <http://www.sciencedirect.com/science/article/pii/S0045782598003831>`_
.. [3] `IJNME, 87(1--5):437--456, 2011. <http://onlinelibrary.wiley.com/doi/10.1002/nme.3158/full>`_
