.. _solfec-theory-solvers:

Constraint solvers
==================

Constraint solvers are used to find approximate a solution to the :ref:`constraints <solfec-theory-constraints>` equations

.. math::

  \mathbf{C}\left(\mathbf{U},\mathbf{R}\right)=\mathbf{0}

expressing :ref:`joints <solfec-theory-joints>` and :ref:`contact conditions <solfec-theory-conform>`, together with
the :ref:`local dynamics <solfec-theory-locdyn>` equations

.. math::

  \mathbf{U}=\mathbf{B}+\mathbf{WR}
  
The merit function used as one of the termination conditions by all solvers, and the algorithms of the Solfec solvers themselves,
are described in sections below.

Merit function
--------------

As discussed on the :ref:`basics page <solfec-theory-basics>`, at every time step an implicit equation
:math:`\mathbf{C}\left(\mathbf{R}\right)=\mathbf{0}` is solved. This solution is approximate. In order to express its accuracy
as a scalar value, we formulate :math:`\mathbf{C}\left(\mathbf{R}\right)` in terms of velocity
(see :ref:`the non-smooth velocity equation formulation <solfec-theory-conform-nsveq>`) and use

.. math::

   g\left(\mathbf{R}\right)=\sum_{\alpha}\left\langle \mathbf{W}_{\alpha\alpha}^{-1}\mathbf{C}_{\alpha}\left(\mathbf{R}\right),
   \mathbf{C}_{\alpha}\left(\mathbf{R}\right)\right\rangle /\sum_{\alpha}\left\langle \mathbf{W}_{\alpha\alpha}^{-1}\mathbf{B}_{\alpha},
   \mathbf{B}_{\alpha}\right\rangle

in order to approximately measure the relative amount of “energy”, due to an inexact satisfaction of constraints. The denominator corresponds
to the kinetic energy of the relative free motion, hence :math:`g\left(\mathbf{R}\right)` is the ratio of the “spurious energy” over the nominal
amount of the “energy available at the constraints”. Since inverting :math:`\mathbf{W}` would be unpractical or impossible due to its singularity,
we only use the diagonal blocks, which are always positive definite. To recapitulate, in short

.. math::

  g\left(\mathbf{R}\right)\simeq\frac{\mbox{"spurious energy due to inaccurate solution"}}{\mbox{"free energy available at the constraints"}}
  
Such merit function is used as one of the stopping criterions for the solvers described below.

.. _solfec-theory-solvers-gs:

Gauss--Seidel solver
--------------------

.. _solfec-theory-solvers-pqn:

Projected Newton solver
-----------------------

.. _solfec-theory-solvers-penalty:

Penalty Solver
--------------
