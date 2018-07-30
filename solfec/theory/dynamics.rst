.. _solfec-theory-dynamics:

Dynamics
========

For a body :math:`\mathcal{B}`, the conservation of linear and angular momentum respectively read

.. math::

  \frac{d}{dt}\int_{\mathcal{B}}\rho\dot{\mathbf{x}}dv=\int_{\partial\mathcal{B}}\mathbf{t}da+\int_{\mathcal{B}}\rho\mathbf{b}dv

.. math::

  \frac{d}{dt}\int_{\mathcal{B}}\left(\mathbf{x}-\bar{\mathbf{x}}\right)\times\rho\dot{\mathbf{x}}dv=
  \int_{\partial\mathcal{B}}\left(\mathbf{x}-\bar{\mathbf{x}}\right)\times\mathbf{t}da+
  \int_{\mathcal{B}}\left(\mathbf{x}-\bar{\mathbf{x}}\right)\times\rho\mathbf{b}dv

where :math:`t` is time, :math:`\rho` is the mass density, :math:`\dot{\mathbf{x}}` is the point velocity,
:math:`\mathbf{t}` is the surface traction, :math:`\mathbf{b}` is the body force, and :math:`\bar{\mathbf{x}}`
is a selected point. All of the mentioned quantities are spatial and so is the integration domain
:math:`\mathcal{B}`, being the current configuration of the body. Sections below rephrase these balance
principles, as required, for each of the kinematic models available in Solfec.

Rigid dynamics
--------------

Linear momentum balance reads

.. math::

  m\ddot{\bar{\mathbf{x}}}=\int_{\partial\mathcal{B}}\mathbf{t}da+\int_{\mathcal{B}}\rho\mathbf{b}dv
  
The spatial angular momentum balance reads

.. math::

  \frac{d}{dt}\left(\mathbf{j}\mathbf{\omega}\right)=\mathbf{j}\dot{\mathbf{\omega}}+\mathbf{\omega}\times\mathbf{j}\mathbf{\omega}=\mathbf{m}
  
The referential angular momentum balance reads

.. math::

  \mathbf{J}\dot{\mathbf{\Omega}}+\mathbf{\Omega}\times\mathbf{J}\mathbf{\Omega}=\mathbf{\Lambda}^{T}\mathbf{m}
  
where :math:`\mathbf{m}` is the torque

.. math::

  \mathbf{m}=\int_{\partial\mathcal{B}}\left(\mathbf{x}-\bar{\mathbf{x}}\right)\times\mathbf{t}da+\int_{\mathcal{B}}\left(\mathbf{x}-\bar{\mathbf{x}}\right)\times\rho\mathbf{b}dv
  
and :math:`\mathbf{j}` and :math:`\mathbf{J}` are

.. math::

  \mathbf{j}=\mathbf{\Lambda}\mathbf{J}\mathbf{\Lambda}^{T},\,\,\,\mathbf{J}=\mbox{tr}\left(\mathbf{E}_{0}\right)\mathbf{I}-\mathbf{E}_{0}
  
the spatial and the referential inertia tensors, respectively. :math:`\mathbf{I}` is the :math:`3\times3` identity matrix. :math:`\mathbf{E}_{0}` is the referential Euler tensor

.. math::
  :label: E0

  \mathbf{E}_{0}=\int_{\mathcal{B}_{0}}\left(\mathbf{X}-\bar{\mathbf{X}}\right)\otimes\left(\mathbf{X}-\bar{\mathbf{X}}\right)\rho_{0}dV
  
where :math:`\mathcal{B}_{0}` is the reference configuration, :math:`\rho_{0}` is the referential mass density,
and the tensor product operator :math:`\otimes` makes a :math:`3\times3` matrix out of two 3-vectors, e.g.
:math:`\mathbf{a}=\mathbf{b}\otimes\mathbf{c}` means :math:`a_{ij}=b_{i}c_{j}`.

In matrix notation these balance principles read

.. math::

  \mathbf{M}\dot{\mathbf{u}}=\mathbf{f}
  
where

.. math::
  :label: mrig

  \mathbf{M}=\left[\begin{array}{cc}
  \mathbf{J}\\
   & m\mathbf{I}
   \end{array}\right]
   
and

.. math::
  :label: frig

  \mathbf{f}=\left[\begin{array}{c}
  \mathbf{\Lambda}^{T}\int_{\partial\mathcal{B}}\left(\mathbf{x}-\bar{\mathbf{x}}\right)\times\mathbf{t}da+
  \mathbf{\Lambda}^{T}\int_{\mathcal{B}}\left(\mathbf{x}-\bar{\mathbf{x}}\right)\times\rho\mathbf{b}dv-\mathbf{\Omega}\times\mathbf{J}\mathbf{\Omega}\\
  \int_{\partial\mathcal{B}}\mathbf{t}da+\int_{\mathcal{B}}\rho\mathbf{b}dv
  \end{array}\right]

Pseudo--rigid dynamics
----------------------

Linear momentum balance reads

.. math::

  m\ddot{\bar{\mathbf{x}}}=\int_{\partial\mathcal{B}}\mathbf{t}da+\int_{\mathcal{B}}\rho\mathbf{b}dv
  
The referential angular momentum balance reads

.. math::

  \ddot{\mathbf{F}}\mathbf{E}_{0}+V\bar{\mathbf{P}}=\int_{\partial\mathcal{B}_{0}}\mathbf{t}\otimes
  \left(\mathbf{X}-\bar{\mathbf{X}}\right)dA+\int_{\mathcal{B}_{0}}\rho_{o}\mathbf{b}\otimes\left(
  \mathbf{X}-\bar{\mathbf{X}}\right)dV
  
where :math:`\mathbf{E}_{0}` is defined in :eq:`E0`, :math:`V` is the volume of the domain, and :math:`\bar{\mathbf{P}}` is the average referential first Piola stress, defined as

.. math::

  \bar{\mathbf{P}}=\partial_{\mathbf{F}}\Psi\left(\mathbf{F}\right)

.. math::

  \Psi=\frac{1}{4}\left[\mathbf{F}^{T}\mathbf{F}-\mathbf{I}\right]:\mathbf{C}:\left[\mathbf{F}^{T}\mathbf{F}-\mathbf{I}\right]

.. math::

  C_{ijkl}=\lambda\delta_{ij}\delta_{kl}+\mu\left[\delta_{ik}\delta_{jl}+\delta_{il}\delta_{jk}\right]
  
where the hyperelastic Saint Venant -- Kirchhoff material is adopted. In the above :math:`\lambda` and :math:`\mu` are Lam\'e constants, while :math:`\delta_{ij}` is the Kronecker delta.
The Lam\'e constants can be expressed in terms of the Young modulus :math:`E` and the Poisson ratio :math:`\nu` as

.. math::

  \lambda=\frac{E\nu}{\left(1+\nu\right)\left(1-2\nu\right)}

.. math::

  \mu=\frac{E}{2+2\nu}
  
In matrix notation these balance principles read

.. math::

  \mathbf{M}\dot{\mathbf{u}}=\mathbf{f}
  
where

.. math::
  :label: mprb

  \mathbf{M}=\left[\begin{array}{cccc}
  \mathbf{E}_{0}\\
  & \mathbf{E}_{0}\\
  &  & \mathbf{E}_{0}\\
  &  &  & m\mathbf{I}
  \end{array}\right]

and

.. math::
  :label: fprb

  \mathbf{f}=\left[\begin{array}{c}
  \int_{\partial\mathcal{B}_{0}}\mathbf{t}\otimes\left(\mathbf{X}-\bar{\mathbf{X}}\right)dA+\int_{\mathcal{B}_{0}}\rho_{o}\mathbf{b}\otimes\left(\mathbf{X}-\bar{\mathbf{X}}\right)dV-V\bar{\mathbf{P}}\\
  \int_{\partial\mathcal{B}}\mathbf{t}da+\int_{\mathcal{B}}\rho\mathbf{b}dv
  \end{array}\right]
   
It should be noted, that it is the row--wise composition of :math:`\dot{\mathbf{F}}` in :math:`\mathbf{u}` (cf. :ref:`Kinematics <pseudo-rigid-vectors>`),
which allows us to use the computationally convenient block--diagonal form of :math:`\mathbf{M}` for pseudo--rigid bodies.

Finite--element dynamics
------------------------

The linear momentum balance reads

.. math::

  \mathbf{M}\dot{\mathbf{u}}+\mathbf{f}_{\text{int}}\left(\mathbf{q}\right)+
  \mathbf{f}_{\text{damp}}\left(\mathbf{q},\mathbf{u}\right)=\mathbf{f}_{\text{ext}}\left(\mathbf{q}\right)
  
where :math:`\mathbf{M}` is the mass matrix, :math:`\mathbf{f}_{\text{int}}` is a vector of internal forces,
:math:`\mathbf{f}_{\text{damp}}` is a vector of damping forces, and :math:`\mathbf{f}_{\text{ext}}` is a vector
of external forces. These matrices and vectors are defined as follows

.. math::
  :label: mfem

  \mathbf{M}=\int_{\mathcal{B}_{0}}\rho_{0}\mathbf{N}^{T}\mathbf{N}dV

.. math::
  :label: fint

  \mathbf{f}_{\text{int}}=\int_{\mathcal{B}_{0}}\left\{ \partial\mathbf{N}/\partial\mathbf{X}\right\} ^{T}\colon\mathbf{P}dV

.. math::
  :label: kfem

  \mathbf{K}=\partial\mathbf{f}_{\text{int}}/\partial\mathbf{q}

.. math::

  \mathbf{f}_{\text{damp}}=\eta\mathbf{K}

.. math::
  :label: fext

  \mathbf{f}_{\text{ext}}=\int_{\mathcal{B}}\rho\mathbf{N}^{T}\mathbf{b}dv+\int_{\partial\mathcal{B}}\mathbf{N}^{T}\mathbf{t}da
  
where, except for :math:`\mathbf{f}_{\text{ext}}`, the so called total Lagrangian notation was used. The contraction of the strain matrix
:math:`\mathbf{B}=\left\{ \partial\mathbf{N}/\partial\mathbf{X}\right\}^{T}` with the first Piola stress tensor, :math:`\mathbf{B}:\mathbf{P}=\sum_{ij}B_{ij}P_{ij}`,
creates the nodal components of the internal force vector. The derivative of the internal force with respect to displacements,
:math:`\partial\mathbf{f}_{\text{int}}/\partial\mathbf{q}`, is customarily called the stiffness matrix, :math:`\mathbf{K}`. Stiffness proportional damping
is used in Solfec, hence :math:`\mathbf{f}_{\text{damp}}=\eta\mathbf{K}`, where :math:`\eta\ge0`.

In matrix notation we simply have

.. math::

  \mathbf{M}\dot{\mathbf{u}}=\mathbf{f}
  
where

.. math::

  \mathbf{f}=\mathbf{f}_{\text{ext}}-\mathbf{f}_{\text{int}}-\mathbf{f}_{\text{damp}} 

Implementation
--------------

Dynamics is implement in `bod.c <https://github.com/tkoziara/solfec/blob/master/bod.c>`_ (rigid, pseudo--rigid)
and `fem.c <https://github.com/tkoziara/solfec/blob/master/bod.c>`_ (finite--element) files. Mass and stiffness
matrices :math:`\mathbf{M}` and :math:`\mathbf{K}`, and the damping factor :math:`\eta`, are declared in
`bod.h <https://github.com/tkoziara/solfec/blob/master/bod.h#L193>`_ as follows:

.. code-block:: c

  struct general_body
  {
    /* ... */

    MX *M;            /* inertia operator */

    MX *K;            /* stiffness operator */

    double damping;   /* stiffness proportional damping */

    /* ... */
  }

.. |br| raw:: html

  <br />

Assembling of :eq:`mrig` is in `bod.c:rig_dynamic_inverse <https://github.com/tkoziara/solfec/blob/master/bod.c#L232>`_. |br|
Evaluation of :eq:`frig` is in `bod.c:rig_static_force <https://github.com/tkoziara/solfec/blob/master/bod.c#L345>`_. |br|
Assembling of :eq:`mprb` is in `bod.c:prb_dynamic_explicit_inverse <https://github.com/tkoziara/solfec/blob/master/bod.c#L479>`_. |br|
Evaluation of :eq:`fprb` is in `bod.c:prb_dynamic_force <https://github.com/tkoziara/solfec/blob/master/bod.c#L647>`_. |br|
Assembling of diagonalized :eq:`mfem` is in `fem.c:diagonal_inertia <https://github.com/tkoziara/solfec/blob/master/fem.c#L1697>`_. |br|
Evaluation of :eq:`fint` is in `fem.c:internal_force <https://github.com/tkoziara/solfec/blob/master/fem.c#L1398>`_. |br|
Assembling of :eq:`kfem` is in `fem.c:tangent_stiffness <https://github.com/tkoziara/solfec/blob/master/fem.c#L1577>`_. |br|
Evaluation of :eq:`fext` is in `fem.c:external_force <https://github.com/tkoziara/solfec/blob/master/fem.c#L1506>`_. |br|
