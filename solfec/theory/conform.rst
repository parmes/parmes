.. _solfec-theory-conform:

Contact formulations
====================

Contact formulations are used in Solfec to facilitate solution of the constraints equation

.. math::

  \mathbf{C}\left(\mathbf{U},\mathbf{R}\right)=\mathbf{0}

once contact points are detected between bodies and included into the :ref:`constraints <solfec-theory-constraints>`.
Depending on a solver type a contact formulation can be either used locally (on a single contact point level) or globally
(on the level of a all contact points simultaneously). This however does not affect the mathematics of a contact formulation
itself. Sections below describe the formulations employed by Solfec and point to references, source code sections and solver
settings related to these formulations.

Projected gradient formulation
------------------------------

De Saxce and Feng formulation
-----------------------------

Semismooth Newton formulation
-----------------------------

Projected Newton formulation
----------------------------

Semi-explicit penalty formulation
---------------------------------

.. [1] P. Alart, A. Curnier, A mixed formulation for frictional contact problems prone to Newton like solution methods,
       Computer Methods in Applied Mechanics and Engineering, 92 (3), 353-375, 1991.
.. [2] G. De Saxcé and Z. Q. Feng, The bipotential method: a constructive approach to design the complete contact law with
       friction and improved numerical algorithms, Mathematical and Computer Modelling, 28, 225-245, 1998.
.. [3] S. Hüeber, G. Stadler, and B. I. Wohlmuth, A primal--dual active set algorithm for three--dimensional contact problems
       with Coulomb friction, SIAM Journal on Scientific Computing, 30 (2), 572-596, 2007.
