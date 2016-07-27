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

Pseudo--rigid dynamics
----------------------

Finite--element dynamics
------------------------

Implementation
--------------
