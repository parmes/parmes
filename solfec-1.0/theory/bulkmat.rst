.. _solfec-1.0-theory-bulkmat:

Bulk materials
==============

A bulk material model is assigned to a volume and defines its deformable characteristic. Available materials are summarized
in the sections below. See also the :ref:`BULK_MATERIAL input command <solfec-1.0-command-BULK_MATERIAL>`.

Kirchhoff -- Saint Venant
-------------------------

This is a simple extension of the linearly elastic material to the large deformation regime. Suitable for large rotation,
small strain problems. The strain energy function :math:`\Psi` of the Kirchhoff -- Saint Venant materials reads

.. math::

  \Psi=\frac{1}{4}\left[\mathbf{F}^{T}\mathbf{F}-\mathbf{I}\right]:\mathbf{C}:\left[\mathbf{F}^{T}\mathbf{F}-\mathbf{I}\right]
  
where

.. math::

  C_{ijkl}=\lambda\delta_{ij}\delta_{kl}+\mu\left[\delta_{ik}\delta_{jl}+\delta_{il}\delta_{jk}\right]
  
In the above :math:`\lambda` and :math:`\mu` are Lamé constants, while :math:`\delta_{ij}` is the Kronecker delta.
The Lamé constants can be expressed in terms of the Young modulus :math:`E` and the Poisson ratio :math:`\nu` as

.. math::

  \lambda=\frac{E\nu}{\left(1+\nu\right)\left(1-2\nu\right)}

.. math::

  \mu=\frac{E}{2+2\nu}
  
The first Piola stress tensor is computed as a gradient of the hyperelastic potential :math:`\Psi`

.. math::

  \mathbf{P}=\partial_{\mathbf{F}}\Psi\left(\mathbf{F}\right)

where :math:`\mathbf{F}` is the deformation gradient.
