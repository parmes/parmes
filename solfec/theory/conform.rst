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

The frictional contact law
--------------------------

The frictional contact law in Solfec employs Signorini--Coulomb conditions. The velocity based Signorini non-penetration condition reads

.. math::
  :label: Signorini

  \bar{U}_{N}\ge0\,\,\,R_{N}\ge0\,\,\,\bar{U}_{N}R_{N}=0
  
where :math:`\bar{U}_{N}=U_{N}^{t+h}+e\min\left(0,U_{N}^{t}\right)`, :math:`e` is the velocity restitution coefficient, :math:`U_{N}` is the the normal
relative velocity, and :math:`R_{N}` is the normal reaction. The normal direction is consistent with the positive gap velocity so that :eq:`Signorini`
states, that any violation of the non--penetration results in a reaction force or velocity driving at the penetration--free configuration. While
using :math:`\bar{U}_{N}` allows to account for the Newton impact law, for models where multiple impacts occur during one time step using :math:`e>0`
cannot be justified from a theoretical standpoint. The Coulomb's friction law reads

.. math::
  :label: Coulomb

  \left\{ \begin{array}{ll}
  \left\Vert \mathbf{R}_{T}\right\Vert \le\mu R_{N}\\
  \left\Vert \mathbf{R}_{T}\right\Vert <\mu R_{N} & \Rightarrow\mathbf{U}_{T}=\mathbf{0}\\
  \left\Vert \mathbf{R}_{T}\right\Vert =\mu R_{N} & \Rightarrow\exists_{\lambda\ge0}\mathbf{U}_{T}=-\lambda\mathbf{R}_{T}
  \end{array}\right.
  
A friction force smaller than :math:`\mu R_{N}` implies sticking, while sliding occurs with the force of value :math:`\mu R_{N}` and direction opposite
to the slip velocity. 

Projected gradient formulation
------------------------------

This is an implicit formulation based on [1]_ and it is optionally used on an individual contact point level within the
:ref:`Gauss-Seidel solver <solfec-theory-solvers-gs>`. On the point level this formulation is implemented in
`dbs.c:35 <https://github.com/tkoziara/solfec/blob/master/dbs.c#L35>`_.  The Signorini condition :eq:`Signorini` is expressed
as a projection

.. math::
  :label: RNproj

  R_{N}=\textrm{proj}_{R_{+}}\left(R_{N}-\rho\bar{U}_{N}\right)

where vector :math:`R_{N}-\rho\bar{U}_{N}` is projected onto the set :math:`R_{+}` of positive real numbers. Similarly, the Coulomb law :eq:`Coulomb` is expressed
as a projection as follows

.. math::
  :label: RTproj
  
  \mathbf{R}_{T}=\textrm{proj}_{D\left(\mu R_{N}\right)}\left(\mathbf{R}_{T}-\rho\mathbf{U}_{T}\right)
  
where :math:`D\left(F\right)` is a two-dimensional :math:`\mathbf{0}`--centred disc of radius :math:`\mu R_{N}`. In both cases above, :math:`\rho>0`.
The name “projected gradient” refers to the above as resembling a gradient projection formula for an optimization problem, where :math:`\mathbf{U}` expresses
a derivative of an objective function with respect to :math:`\mathbf{R}`.

De Saxcé and Feng formulation
-----------------------------

This is an implicit formulation based on [2]_ and it is optionally used on an individual contact point level within the
:ref:`Gauss-Seidel solver <solfec-theory-solvers-gs>`. On the point level this formulation is implemented in
`dbs.c:96 <https://github.com/tkoziara/solfec/blob/master/dbs.c#L96>`_. We express the Signorini-Coulomb law :eq:`Signorini` and :eq:`Coulomb`
as an inclusion.The friction cone :math:`K_{\alpha}` is defined as

.. math::
  :label: Kalpha

  K_{\alpha}=\left\{ \mathbf{R}_{\alpha}:\left\Vert \mathbf{R}_{\alpha T}\right\Vert \le\mu_{\alpha}R_{\alpha N},R_{\alpha N}\ge0\right\}
  
where :math:`\mu_{\alpha}` is the coefficient of friction. It has been shown by De Saxcé and Feng [2]_, that the Signorini-Coulomb law
can be expressed in a compact form

.. math::
  :label: DSF

  -\left[\begin{array}{c}
  \mathbf{U}_{\alpha T}\\
  \bar{U}_{\alpha N}+\mu_{\alpha}\left\Vert \mathbf{U}_{\alpha T}\right\Vert 
  \end{array}\right]\in N_{K_{\alpha}}\left(\mathbf{R}_{\alpha}\right)

where :math:`N_{K_{\alpha}}` stands for the normal cone of the set :math:`K_{\alpha}`. For a convex set A the normal :math:`cone N_{A}\left(\mathbf{R}\right)`
at point :math:`\mathbf{R}\in A` is defined as the set of all vectors :math:`\mathbf{V}` such that :math:`\left\langle \mathbf{V},\mathbf{S}-\mathbf{R}\right\rangle \le0`
for all :math:`\mathbf{S}\in A`. Based on inclusion :eq:`DSF`, the authors of [2]_ propose the following projection formula

.. math::
  :label: DSFproj

  \mathbf{R}_{\alpha}=\mbox{proj}_{K_{\alpha}}\left(\mathbf{R}_{\alpha}-\rho\left[\begin{array}{c}
  \mathbf{U}_{\alpha T}\\
  \bar{U}_{\alpha N}+\mu_{\alpha}\left\Vert \mathbf{U}_{\alpha T}\right\Vert 
  \end{array}\right]\right)
  
where \rho>0. Formula :eq:`DSFproj` can be used instead of the projected gradient formulas :eq:`RNproj` and :eq:`RTproj`.

Non--smooth force equation formulation
--------------------------------------

.. _solfec-theory-conform-nsveq:

Non-smooth velocity equation formulation
----------------------------------------

Semi-explicit penalty formulation
---------------------------------

.. [1] P. Alart, A. Curnier, A mixed formulation for frictional contact problems prone to Newton like solution methods,
       Computer Methods in Applied Mechanics and Engineering, 92 (3), 353-375, 1991.
.. [2] G. De Saxcé and Z. Q. Feng, The bipotential method: a constructive approach to design the complete contact law with
       friction and improved numerical algorithms, Mathematical and Computer Modelling, 28, 225-245, 1998.
.. [3] S. Hüeber, G. Stadler, and B. I. Wohlmuth, A primal--dual active set algorithm for three--dimensional contact problems
       with Coulomb friction, SIAM Journal on Scientific Computing, 30 (2), 572-596, 2007.
