.. _solfec-theory-joints:

Joints
======

Joints in  Solfec-1.0 are defined by :ref:`FIX_POINT <solfec-command-FIX_POINT>`, :ref:`FIX_DIRECTION <solfec-command-FIX_DIRECTION>`,
:ref:`SET_DISPLACEMENT <solfec-command-SET_DISPLACEMENT>`, :ref:`SET_VELOCITY <solfec-command-SET_VELOCITY>`,
:ref:`SET_ACCELERATION <solfec-command-SET_ACCELERATION>`, :ref:`PUT_RIGID_LINK <solfec-command-PUT_RIGID_LINK>`, and
:ref:`PUT_SPRING <solfec-command-PUT_SPRING>` commands. Joints are also called bilateral constraints. They restrain absolute motion
of individual points of individual bodies, or relative motion of pairs of points between two bodies.

Joints are implemented via suitably setting values of components of relative constraint velocities or
constraint reactions. That is to say, the general implicit relation

.. math::
  :label: Cal

  \mathbf{C}_{\alpha}\left(\mathbf{U}_{\alpha},\mathbf{R}_{\alpha}\right)=\mathbf{0}
  
for a bilateral constraint with index :math:`\alpha` takes a particular shape. In order to work with components
of relative velocities and forces it is convenient to introduce the following naming convention. Let every local
frame be defined by a matrix :math:`\left\{ \mathbf{a}_{T1},\mathbf{a}_{T2},\mathbf{a}_{N}\right\}`  made of juxtaposed
column vectors: :math:`\mathbf{a}_{T1}` and :math:`\mathbf{a}_{T2}`, called *tangent*, and :math:`\mathbf{a}_{N}`, called *normal*.
We also assume, that these vectors are mutually perpendicular: :math:`\mathbf{a}_{T1}\perp\mathbf{a}_{T2}\perp\mathbf{a}_{N}`.
With this convenetion at hand, below we define particular versions of relation :eq:`Cal` for joint types available in Solfec-1.0.

.. _fixed-point:

Fixed point
-----------

Joint corresponding to the :ref:`FIX_POINT <solfec-command-FIX_POINT>` command is realized by defining

.. math::

  \mathbf{C}\left(\mathbf{U},\mathbf{R}\right)=\mathbf{U}
  
and hence

.. math::

  \mathbf{U}=\mathbf{0}
  
imposes the fixed point constraint.

.. _fixed-direction:

Fixed direction
---------------

Joint corresponding to the :ref:`FIX_DIRECTION <solfec-command-FIX_DIRECTION>` command is realized by defining

.. math::

  \mathbf{C}\left(\mathbf{U},\mathbf{R}\right)=\left[\begin{array}{c}
  R_{T1}\\
  R_{T2}\\
  U_{N}
  \end{array}\right]
  
and hence

.. math::

  \mathbf{R}_{T}=\mathbf{0},\,\,\,U_{N}=0
  
imposes the fixed direction constraint. In this case the normal direction is taken to be the fixed direction,
while the tangential plane is unused (hence zero tangential reaction,
:math:`\mathbf{R}_{T}=\left[\begin{array}{c} R_{T1}\\ R_{T2} \end{array}\right]`)

.. _prescribed-displacement:

Prescribed displacement
-----------------------

Joint corresponding to the :ref:`SET_DISPLACEMENT <solfec-command-SET_DISPLACEMENT>` command is realized by defining

.. math::

  \mathbf{C}\left(\mathbf{U},\mathbf{R}\right)=\left[\begin{array}{c}
  R_{T1}\\
  R_{T2}\\
  U_{N}-\frac{d}{dt}\text{disp}\left(t\right)
  \end{array}\right]
  
and hence

.. math::

  \mathbf{R}_{T}=\mathbf{0},\,\,\,U_{N}=\frac{d}{dt}\text{disp}\left(t\right)
  
where the displacement signal :math:`\text{disp}\left(t\right)` is provided by the user as a linear spline and
differentiated numerically to obtain velocity. The tangential plane is unused, hence zero tangential reaction.

.. _prescribed-velocity:

Prescribed velocity
-------------------

Joint corresponding to the :ref:`SET_VELOCITY <solfec-command-SET_VELOCITY>` command is realized by defining

.. math::

  \mathbf{C}\left(\mathbf{U},\mathbf{R}\right)=\left[\begin{array}{c}
  R_{T1}\\
  R_{T2}\\
  U_{N}-\text{velo}\left(t\right)
  \end{array}\right]
  
and hence

.. math::

  \mathbf{R}_{T}=\mathbf{0},\,\,\,U_{N}=\text{velo}\left(t\right)
  
where the velocity signal :math:`\text{velo}\left(t\right)` is provided by the user as a linear spline.
The tangential plane is unused, hence zero tangential reaction.

.. _prescribed-acceleration:

Prescribed acceleration
-----------------------

Joint corresponding to the :ref:`SET_ACCELERATION <solfec-command-SET_ACCELERATION>` command is realized by defining

.. math::

  \mathbf{C}\left(\mathbf{U},\mathbf{R}\right)=\left[\begin{array}{c}
  R_{T1}\\
  R_{T2}\\
  U_{N}-\int_{0}^{t}\text{acc}\left(t\right)
  \end{array}\right]

and hence

.. math::

  \mathbf{R}_{T}=\mathbf{0},\,\,\,U_{N}=\int_{0}^{t}\text{acc}\left(t\right)

where the acceleration signal :math:`\text{acc}\left(t\right)` is provided by the user as a linear spline and
integrated numerically to obtain velocity. The tangential plane is unused, hence zero tangential reaction.

.. _rigid-link:

Rigid link constraint
---------------------

Joint corresponding to the :ref:`PUT_RIGID_LINK <solfec-command-PUT_RIGID_LINK>` command is realized by defining a normal direction

.. math::

  \mathbf{a}_{N}=\frac{\mathbf{x}_{1}\left(\mathbf{X}_{1},t\right)-\mathbf{x}_{2}\left(\mathbf{X}_{2},t\right)}{\left\Vert \mathbf{x}_{1}-\mathbf{x}_{2}\right\Vert }
  
and tangential plane as orthogonal to this direction :math:`\mathbf{a}_{T1}\perp\mathbf{a}_{T2}\perp\mathbf{a}_{N}`, followed by imposing 

.. math::

  \mathbf{C}\left(\mathbf{U},\mathbf{R}\right)=\left[\begin{array}{c}
  R_{T1}\\
  R_{T2}\\
  U_{N}
  \end{array}\right]
  
and hence

.. math::

  \mathbf{R}_{T}=\mathbf{0},\,\,\,U_{N}=0
  
which fixes the relative motion of points :math:`\mathbf{x}_{1}` and :math:`\mathbf{x}_{2}` along the normal direction.
The tangential plane is unused, hence zero tangential reaction.

.. _simple-spring:

Spring constraint
-----------------

Joint corresponding to the :ref:`PUT_SPRING <solfec-command-PUT_SPRING>` command is realized by defining a stretch

.. math::

  d=\left\Vert \mathbf{x}_{1}\left(\mathbf{X}_{1},t\right)-\mathbf{x}_{2}\left(\mathbf{X}_{2},t\right)\right\Vert -\left\Vert \mathbf{X}_{1}-\mathbf{X}_{2}\right\Vert
  
a normal direction

.. math::

  \mathbf{a}_{N}=\frac{\mathbf{x}_{1}\left(\mathbf{X}_{1},t\right)-\mathbf{x}_{2}\left(\mathbf{X}_{2},t\right)}{\left\Vert \mathbf{x}_{1}-\mathbf{x}_{2}\right\Vert }
  
and tangential plane as orthogonal to this direction :math:`\mathbf{a}_{T1}\perp\mathbf{a}_{T2}\perp\mathbf{a}_{N}`, followed by imposing 

.. math::

  \mathbf{C}\left(\mathbf{U},\mathbf{R}\right)=\left[\begin{array}{c}
  R_{T1}\\
  R_{T2}\\
  R_{N}=\text{user_force}\left(d,\dot{d}\right)
  \end{array}\right]
  
and hence

.. math::

  \mathbf{R}_{T}=\mathbf{0},\,\,\,R_{N}=\text{user_force}\left(d,\dot{d}\right)
  
where the user force is prescribed as a Python subroutine.
The tangential plane is unused, hence zero tangential reaction.

Implementation
--------------

Joints are implemented as a part of constraint solvers. For example, function
`dbs.c:DIAGONAL_BLOCK_Solver <https://github.com/tkoziara/solfec/blob/master/dbs.c#L483>`_ is a driver
routine for all joint types solved within the :ref:`Gauss--Seidel <solfec-command-GAUSS_SEIDEL_SOLVER>` solver,
invoked from within `bgs.c:GAUSS_SEIDEL_Solve <https://github.com/tkoziara/solfec/blob/master/bgs.c#L901>`_.
Within the :ref:`Projected Newton <solfec-command-NEWTON_SOLVER>` solver the routine
`nts.c:solve <https://github.com/tkoziara/solfec/blob/master/nts.c#L939>`_ implements all joint types.
