.. _solfec-theory-conform:

Contact formulations
====================

Contact formulations are used in Solfec to facilitate solution of the constraints equation

.. math::

  \mathbf{C}\left(\mathbf{U},\mathbf{R}\right)=\mathbf{0}

once contact points are detected between bodies and included into the :ref:`constraints <solfec-theory-constraints>`.
Depending on a solver type a contact formulation can be either used locally (on a single contact point level) or globally
(on the level of a all contact points simultaneously). This however does not affect the mathematics of a contact formulation
itself. Sections below describe the formulations employed by Solfec and point to references, source code sections, and
descriptions of solvers that utilize them.

The frictional contact law
--------------------------

The frictional contact law in Solfec employs the so called Signorini--Coulomb conditions. The velocity based Signorini non--penetration condition reads

.. math::
  :label: Signorini

  \bar{U}_{N}\ge0\,\,\,R_{N}\ge0\,\,\,\bar{U}_{N}R_{N}=0
  
where :math:`\bar{U}_{N}=U_{N}^{t+h}+e\min\left(0,U_{N}^{t}\right)`, :math:`e` is the velocity restitution coefficient, :math:`U_{N}` is the the normal
relative velocity, and :math:`R_{N}` is the normal reaction. The normal direction is consistent with the positive gap velocity so that :eq:`Signorini`
states, that any violation of the non--penetration results in a reaction force or velocity driving at the penetration--free configuration. While
using :math:`\bar{U}_{N}` allows to account for the Newton impact law, for models where multiple impacts occur during one time step, using :math:`e>0`
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
:ref:`Gauss--Seidel solver <solfec-theory-solvers-gs>`. On the point level this formulation is implemented in
`dbs.c:35 <https://github.com/tkoziara/solfec/blob/master/dbs.c#L35>`_.  The Signorini condition :eq:`Signorini` is expressed
as a projection

.. math::
  :label: RNproj

  R_{N}=\textrm{proj}_{R_{+}}\left(R_{N}-\rho\bar{U}_{N}\right)

where vector :math:`R_{N}-\rho\bar{U}_{N}` is projected onto the set of positive real numbers :math:`R_{+}`. Similarly, the Coulomb law :eq:`Coulomb` is expressed
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
:ref:`Gauss--Seidel solver <solfec-theory-solvers-gs>`. On the point level this formulation is implemented in
`dbs.c:96 <https://github.com/tkoziara/solfec/blob/master/dbs.c#L96>`_. We express the Signorini--Coulomb law :eq:`Signorini` and :eq:`Coulomb`
as an inclusion. The friction cone :math:`K_{\alpha}` is defined as

.. math::
  :label: Kalpha

  K_{\alpha}=\left\{ \mathbf{R}_{\alpha}:\left\Vert \mathbf{R}_{\alpha T}\right\Vert \le\mu_{\alpha}R_{\alpha N},R_{\alpha N}\ge0\right\}
  
where :math:`\mu_{\alpha}` is the coefficient of friction. It has been shown by De Saxcé and Feng [2]_, that the Signorini--Coulomb law
can be expressed in a compact form

.. math::
  :label: DSF

  -\left[\begin{array}{c}
  \mathbf{U}_{\alpha T}\\
  \bar{U}_{\alpha N}+\mu_{\alpha}\left\Vert \mathbf{U}_{\alpha T}\right\Vert 
  \end{array}\right]\in N_{K_{\alpha}}\left(\mathbf{R}_{\alpha}\right)

where :math:`N_{K_{\alpha}}` stands for the normal cone of the set :math:`K_{\alpha}`. For a convex set A the normal cone :math:`N_{A}\left(\mathbf{R}\right)`
at point :math:`\mathbf{R}\in A` is defined as the set of all vectors :math:`\mathbf{V}` such that :math:`\left\langle \mathbf{V},\mathbf{S}-\mathbf{R}\right\rangle \le0`
for all :math:`\mathbf{S}\in A`. Based on inclusion :eq:`DSF`, the authors of [2]_ propose the following projection formula

.. math::
  :label: DSFproj

  \mathbf{R}_{\alpha}=\mbox{proj}_{K_{\alpha}}\left(\mathbf{R}_{\alpha}-\rho\left[\begin{array}{c}
  \mathbf{U}_{\alpha T}\\
  \bar{U}_{\alpha N}+\mu_{\alpha}\left\Vert \mathbf{U}_{\alpha T}\right\Vert 
  \end{array}\right]\right)
  
where :math:`\rho>0`. Formula :eq:`DSFproj` can be used instead of the projected gradient formulas :eq:`RNproj` and :eq:`RTproj`. The appeal of this approach is in
the separation of velocities on the left hand side of the inclusion :eq:`DSF` from forces on the right hand side, as well as in the constancy of the friction cone
:math:`K_{\alpha}`, which together make this formulation seem even more like a statement of optimality for a constrained optimization problem. This may be helpful
in formulating solution strategies based on already existing approaches.

Non--smooth force equation formulation
--------------------------------------

This is an implicit formulation based on [3]_ and it is used by default on an individual contact point level within the
:ref:`Gauss--Seidel solver <solfec-theory-solvers-gs>`. On the point level this formulation is implemented in
`dbs.c:142 <https://github.com/tkoziara/solfec/blob/master/dbs.c#L142>`_. The authors of [3]_ propose to express the Signorini and Coulomb
conditions :eq:`Signorini` and :eq:`Coulomb` as a non--smooth equation :math:`\mathbf{C}\left(\mathbf{U},\mathbf{R}\right)=\mathbf{0}`, where

.. math::
  :label: NSFEQ

  \mathbf{C}\left(\mathbf{U},\mathbf{R}\right)=\left[\begin{array}{c}
  \max\left(\mu d_{N},\left\Vert \mathbf{d}_{T}\right\Vert \right)\mathbf{R}_{T}-\mu\max\left(0,d_{N}\right)\mathbf{d}_{T}\\
  R_{N}-\max\left(0,d_{N}\right)
  \end{array}\right]
  
and

.. math::
  :label: dN

  d_{N}=R_{N}-\rho\bar{U}_{N}

.. math::
  :label: dT

  \mathbf{d}_{T}=\mathbf{R}_{T}-\rho\mathbf{U}_{T}

while :math:`\rho>0`. Equation :eq:`NSFEQ` encapsulates the projection formulas :eq:`RNproj` and :eq:`RTproj` and it has been shown to work well
as a basis for Newton type solution schemes in the finite--element context.

.. _solfec-theory-conform-nsveq:

Non--smooth velocity equation formulation
-----------------------------------------

This is an implicit formulation developed specifically for Solfec based on formula :eq:`DSF` from [2]_. It is optionally used on an individual
contact point level within the :ref:`Gauss--Seidel solver <solfec-theory-solvers-gs>`. It is also the basis of contact linearization within the
:ref:`projected Newton solver <solfec-theory-solvers-pqn>`. On the point level this formulation is implemented in
`scf.c <https://github.com/tkoziara/solfec/blob/master/scf.c#L28>`_. Using the :ref:`local dynamics <solfec-theory-locdyn>` relationship 

.. math::
  :label: locdyn

  \mathbf{U_{\alpha}}=\mathbf{B_{\alpha}}+\sum_{\beta}\mathbf{W}_{\alpha\beta}\mathbf{R}_{\beta}

let us define a function

.. math::
  :label: F

  \mathbf{F}\left(\mathbf{R}\right)=\left[\begin{array}{c}
  ...\\
  \mathbf{U}_{\alpha T}\left(\mathbf{R}\right)\\
  \bar{U}_{\alpha N}\left(\mathbf{R}\right)+\mu_{\alpha}\left\Vert \mathbf{U}_{\alpha T}\left(\mathbf{R}\right)\right\Vert \\
  ...
  \end{array}\right]
  
and a total cone

.. math::
  
  K=\bigcup_{\alpha}K_{\alpha}
  
where :math:`\mu_{\alpha}` is the coefficient of friction at a contact point :math:`\alpha`, :math:`K_{\alpha}` is the corresponding friction cone
:eq:`Kalpha`, while the dependence :math:`\mathbf{U}_{\alpha}\left(\mathbf{R}\right)` is given by :eq:`locdyn`. Formula :eq:`DSF` states, that the
frictional contact constraints are satisfied if :math:`-\mathbf{F}\left(\mathbf{R}\right)` belongs to the normal cone of the friction cone at
:math:`\mathbf{R}`. Hence

.. math::

  -\mathbf{F}\left(\mathbf{R}\right)=\mathbf{R}-\mathbf{F}\left(\mathbf{R}\right)-
  \mbox{proj}_{K}\left(\mathbf{R}-\mathbf{F}\left(\mathbf{R}\right)\right)
  
which can be reduced to the usual projection formula :math:`\mathbf{R}=\mbox{proj}_{K}\left(\mathbf{R}-\mathbf{F}\left(\mathbf{R}\right)\right)` or
:eq:`DSFproj` with :math:`\rho=1`. Let us not do it though, but rather define a vector field

.. math::

  \mathbf{m}\left(\mathbf{S}\right)=\mathbf{S}-\mbox{proj}_{K}\left(\mathbf{S}\right)=
  \mathbf{n}\left(\mathbf{S}\right)\left\langle \mathbf{n}\left(\mathbf{S}\right),\mathbf{S}\right\rangle
  
where

.. math::
  :label: n

  \mathbf{n}_{\alpha}\left(\mathbf{S}_{\alpha}\right)=\left\{ \begin{array}{lll}
  \mathbf{0} & \mbox{if} & \left\Vert \mathbf{S}_{\alpha T}\right\Vert -\mu_{\alpha}S_{\alpha N}\le0\\
  \mathbf{S}_{\alpha}/\left\Vert \mathbf{S}_{\alpha}\right\Vert  & \mbox{if} &
  \mu_{\alpha}\left\Vert \mathbf{S}_{\alpha T}\right\Vert +S_{\alpha N}<0\\
  \frac{1}{\sqrt{1+\mu_{\alpha}^{2}}}\left[\begin{array}{c}
  \mathbf{S}_{\alpha T}/\left\Vert \mathbf{S}_{\alpha T}\right\Vert \\
  -\mu_{\alpha}
  \end{array}\right] & \mbox{} & \mbox{otherwise}
  \end{array}\right.
  
We can rewrite :eq:`DSF` as

.. math::
  :label: NSVEQ

  \mathbf{C}\left(\mathbf{R}\right)=\mathbf{F}\left(\mathbf{R}\right)+\mathbf{m}\left(\mathbf{R}-\mathbf{F}\left(\mathbf{R}\right)\right)=\mathbf{0}\mbox{ and }\mathbf{R}\in K
  
Note, that :math:`\mathbf{F}\left(\mathbf{R}\right)` is expressed in terms of velocity, and so is :math:`\mathbf{C}\left(\mathbf{R}\right)`.
Equation :eq:`NSVEQ` expresses, in velocity form, the projection formula :eq:`DSFproj`.

Semi--explicit penalty formulation
----------------------------------

This is a simple penalty based formulation developed specifically for Solfec and used within the
:ref:`penalty solver <solfec-theory-solvers-penalty>`. On the point level this formulation is implemented
in `pes.c <https://github.com/tkoziara/solfec/blob/master/pes.c#L33>`_. Let

.. math::

  s=spring\mbox{ and }d=dashpot\mbox{ and }g=gap\mbox{ and }m=hpow
  
where :math:`hpow` stands for the “Hertz power”. The normal reaction is computed as follows

.. math::
  :label: spring-dashpot-1

  R_{N}=-s\cdot\frac{g^{t+h}+g^{t}}{2}-d\cdot\frac{U_{N}^{t+h}+U_{N}^{t}}{2}

where :math:`U_{N}` is the normal relative velocity. :ref:`Recall <solfec-theory-basics>`, that the gap function is computed for the configuration
:math:`\mathbf{q}^{t}+\frac{h}{2}\mathbf{u}^{t}`, so that the gap function value computed during geometrical contact detection reads

.. math::

  g=g^{t}+\frac{h}{2}U_{N}^{t}
  
We then have

.. math::

  g^{t+h}=g^{t}+\frac{h}{2}\left(U_{N}^{t+h}+U_{N}^{t}\right)=g+\frac{h}{2}U_{N}^{t+h}
  
and since :math:`g^{t}=g-\frac{h}{2}U_{N}^{t}` we can estimate

.. math::
  :label: spring-dashpot-2

  R_{N}=-s\cdot\left(g+\frac{h}{4}\left(U_{N}^{t+h}-U_{N}^{t}\right)\right)-\frac{d}{2}\cdot\left(U_{N}^{t+h}+U_{N}^{t}\right)
  
We then use the diagonal block of local dynamics

.. math::

  \mathbf{U}^{t+h}=\mathbf{B}+\mathbf{W}\mathbf{R}
  
in order to estimate :math:`U_{N}^{t+h}` as follows

.. math::

  U_{N}^{t+h}=B_{N}+\mathbf{W}_{NT}\mathbf{R}_{T}+W_{NN}R_{N}
  
where a previous tangential reaction :math:`\mathbf{R}_{T}` is employed. Inserting this it into :eq:`spring-dashpot-2` results in

.. math::

  \bar{B}_{N}=B_{N}+\mathbf{W}_{NT}\mathbf{R}_{T}


.. math::
  :label: spring-dashpot-3

  R_{N}=\left[-s\cdot\left(g+\frac{h}{4}\left(\bar{B}_{N}-U_{N}^{t}\right)\right)-\frac{d}{2}\cdot\left(
  \bar{B}_{N}+U_{N}^{t}\right)\right]/\left[1+\left(s\cdot\frac{h}{4}+\frac{d}{2}\right)\cdot W_{NN}\right]
  
The reason for using the above, rather than the classical :math:`R_{N}=-s\cdot g-d\cdot U_{N}^{t}` is in an increased stability of
the this approach. Since we aim at simplicity and want to avoid any nonlinear solve only at this stage we include the “Hertz power”

.. math::

  g_{1}=\mbox{min}\left(g+\frac{h}{4}\left(\bar{B}_{N}-U_{N}^{t}\right),0\right)

.. math::

  s_{1}=sm\left(-g_{1}\right)^{m-1}

.. math::

  R_{N}=\left[s\cdot\left(-g_{1}\right)^{m}-\frac{d}{2}\cdot\left(\bar{B}_{N}+U_{N}^{t}\right)\right]
  /\left[1+\left(s_{1}\cdot\frac{h}{4}+\frac{d}{2}\right)\cdot W_{NN}\right]
  
Again aiming at maximum simplicity and assuming :math:`\mathbf{U}_{T}^{t+h}=0` we then estimate the tangential stick reaction

.. math::

  \mathbf{R}_{T}=-\mathbf{W}_{TT}^{-1}\left(\mathbf{B}_{T}+\mathbf{W}_{TN}R_{N}\right)
  
The complete interface law is expressed the below algorithm (where :math:`h` is the time step, :math:`g` is the contact gap,
:math:`s` is the spring constant, :math:`d` is the damper constant, :math:`\mu` refers there to the coefficient of friction,
and :math:`m` is the “Hertz power”). 

.. |br| raw:: html

  <br />

**SPRING_DASHPOT_CONTACT** :math:`\left(h,g,s,d,\mu,cohesion,cohesive\right)` |br|
1  :math:`\,\,` :math:`\bar{B}_{N}=B_{N}+\mathbf{W}_{NT}\mathbf{R}_{T}` |br|
2  :math:`\,\,` if semi--explicit then |br|
3  :math:`\,\,\,\,\,\,` :math:`g_{1}=\mbox{min}\left(g+\frac{h}{4}\left(\bar{B}_{N}-U_{N}^{t}\right),0\right)` |br|
4  :math:`\,\,\,\,\,\,` :math:`s_{1}=sm\left(-g_{1}\right)^{m-1}` |br|
5  :math:`\,\,\,\,\,\,` :math:`R_{N}=\left[s\cdot\left(-g_{1}\right)^{m}-\frac{d}{2}\cdot\left(\bar{B}_{N}+U_{N}^{t}\right)\right]/\left[1+\left(s_{1}\cdot\frac{h}{4}+\frac{d}{2}\right)\cdot W_{NN}\right]` |br|
6  :math:`\,\,` else :math:`R_{N}=s\cdot\left(-\min\left(g,0\right)\right)^{m}-d\cdot U_{N}^{t}` |br|
7  :math:`\,\,` if not :math:`cohesive` and :math:`R_{N}<0` then :math:`\mathbf{R}=0` return |br|
8  :math:`\,\,` :math:`\mathbf{R}_{T}=-\mathbf{W}_{TT}^{-1}\left(\mathbf{B}_{T}+\mathbf{W}_{TN}R_{N}\right)` |br|
9  :math:`\,\,` if :math:`cohesive` and :math:`R_{N}<-cohesion` then :math:`cohesive=false` and :math:`R_{N}=-cohesion` |br|
10 :math:`\,`   if :math:`\left\Vert \mathbf{R}_{T}\right\Vert >\mu\left|R_{N}\right|` then |br|
11 :math:`\,\,\,\,\,` :math:`\mathbf{R}_{T}=\mu R_{N}\mathbf{R}_{T}/\left\Vert \mathbf{R}_{T}\right\Vert` |br|
12 :math:`\,\,\,\,\,` if :math:`cohesive` then :math:`cohesive=false` |br|

.. [1] P. Alart, A. Curnier, A mixed formulation for frictional contact problems prone to Newton like solution methods,
       Computer Methods in Applied Mechanics and Engineering, 92 (3), 353-375, 1991.
.. [2] G. De Saxcé and Z. Q. Feng, The bipotential method: a constructive approach to design the complete contact law with
       friction and improved numerical algorithms, Mathematical and Computer Modelling, 28, 225-245, 1998.
.. [3] S. Hüeber, G. Stadler, and B. I. Wohlmuth, A primal--dual active set algorithm for three--dimensional contact problems
       with Coulomb friction, SIAM Journal on Scientific Computing, 30 (2), 572-596, 2007.
