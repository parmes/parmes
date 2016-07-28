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
  
where \mathbf{m} is the torque

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

  \mathbf{M}=\left[\begin{array}{cc}
  \mathbf{J}\\
   & m\mathbf{I}
   \end{array}\right]
   
and

.. math::

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
  
where :math:`\mathbf{E}_{0}` is defined in :eq:`E0`, :math:`V` is the volume of the domain, and :math:`\bar{\mathbf{P}}` is the average referential stress, defined as

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

  \mathbf{M}=\left[\begin{array}{cccc}
  \mathbf{E}_{0}\\
  & \mathbf{E}_{0}\\
  &  & \mathbf{E}_{0}\\
  &  &  & m\mathbf{I}
  \end{array}\right]

and

.. math::

  \mathbf{f}=\left[\begin{array}{c}
  \int_{\partial\mathcal{B}_{0}}\mathbf{t}\otimes\left(\mathbf{X}-\bar{\mathbf{X}}\right)dA+\int_{\mathcal{B}_{0}}\rho_{o}\mathbf{b}\otimes\left(\mathbf{X}-\bar{\mathbf{X}}\right)dV-V\bar{\mathbf{P}}\\
  \int_{\partial\mathcal{B}}\mathbf{t}da+\int_{\mathcal{B}}\rho\mathbf{b}dv
  \end{array}\right]
   
It should be noted, that it is the row--wise composition of :math:`\dot{\mathbf{F}}` in :math:`\mathbf{u}` (cf. :ref:`Kinematics <pseudo-rigid-vectors>`),
which allows us to use the computationally convenient block--diagonal form of :math:`\mathbf{M}` for pseudo--rigid bodies.

Finite--element dynamics
------------------------

Implementation
--------------
