.. _solfec-theory-timeint:

Time integration
================

Solfec implements three variants of time integration of rigid body kinematics:

* RIG_POS -- a semi--explicit scheme with a positive energy drift, cf. NEW1 in [1]_

* RIG_NEG -- a semi--explicit scheme with a negative energy drift, cf. NEW2 in [1]_

* RIG_IMP -- a semi--implicit without energy drift (but rather, oscillation), cf. NEW3 in [1]_

And two variants of time integration for pseudo–rigid and finite–element kinematics:

* DEF_EXP -- an explicit leap--frog scheme, cf. Section 5.1 in [2]_

* DEF_LIM -- a linearly implicit leap--frog scheme, [3]_

A time integration scheme is selected by modifying the *scheme* parameter of the :ref:`BODY object <solfec-user-body>`.

Rigid integration
-----------------

Linear motion is integrated like :ref:`deformable motion <deformable-integration>`. Rigid rotations are integrated as follows

.. math::
  :label: R(t+h/2)

  \mathbf{\Lambda}^{t+\frac{h}{2}}=\mathbf{\Lambda}^{t}\exp\left[\frac{h}{2}\mathbf{\Omega}^{t}\right]

.. math::
  :label: T(t+h/2)

  \mathbf{T}^{t+\frac{h}{2}}=\left(\mathbf{\Lambda}^{t+\frac{h}{2}}\right)^{T}\mathbf{t}^{t+\frac{h}{2}}

.. math::
  :label: W(t+h/2)

  \mathbf{\Omega}^{t+\frac{h}{2}}=\mathbf{J}^{-1}\left[\exp\left[-\frac{h}{2}\mathbf{\Omega}^{t}\right]\mathbf{J}\mathbf{\Omega}^{t}+\frac{h}{2}\mathbf{T}^{t+\frac{h}{2}}\right]

.. math::
  :label: W1(t+h)

  \mathbf{\Omega}_{1}^{t+h}=\mathbf{\Omega}^{t}+\mathbf{J}^{-1}h\left[\mathbf{T}^{t+\frac{h}{2}}-\mathbf{\Omega}^{t+\frac{h}{2}}\times\mathbf{J}\mathbf{\Omega}^{t+\frac{h}{2}}\right]

If explicit

.. math::
  :label: R1(t+h)

  \mathbf{\Lambda}^{t+h}=\mathbf{\Lambda}^{t+\frac{h}{2}}\exp\left[\frac{h}{2}\mathbf{\Omega}_{1}^{t+h}\right]

.. math::
  :label: W2(t+h)

  \mathbf{\Omega}_{2}^{t+h}=\mathbf{J}^{-1}\exp\left[-\frac{h}{2}\mathbf{\Omega}_{1}^{t+h}\right]\left[\exp\left
  [-\frac{h}{2}\mathbf{\Omega}^{t}\right]\mathbf{J}\mathbf{\Omega}^{t}+h\mathbf{T}^{t+\frac{h}{2}}\right]

otherwise

.. math::
  :label: W3(t+h)

  \mbox{\textbf{solve} }\left(\exp\left[\frac{h}{2}\mathbf{\Omega}_{3}^{t+h}\right]\mathbf{J}\mathbf{\Omega}_{3}^{t+h}=
  \exp\left[-\frac{h}{2}\mathbf{\Omega}^{t}\right]\mathbf{J}\mathbf{\Omega}^{t}+h\mathbf{T}^{t+\frac{h}{2}}\right)

.. math::
  :label: R2(t+h)

  \mathbf{\Lambda}^{t+h}=\mathbf{\Lambda}^{t+\frac{h}{2}}\exp\left[\frac{h}{2}\mathbf{\Omega}_{3}^{t+h}\right]

The scheme ending at :eq:`R1(t+h)` is DEF_POS, ending at :eq:`W2(t+h)` is DEF_NEG, and using instead :eq:`W3(t+h)` and :eq:`R2(t+h)` is DEF_IMP.
Above, :math:`\exp\left[\cdot\right]` is the exponential map defined by the Rodrigues formula

.. math::

  \exp\left[\mathbf{\Psi}\right]=\mathbf{I}+\frac{\sin\left\Vert \mathbf{\Psi}\right\Vert }{\left\Vert \mathbf{\Psi}\right\Vert }
  \hat{\mathbf{\Psi}}+\frac{1-\cos\left\Vert \mathbf{\Psi}\right\Vert }{\left\Vert \mathbf{\Psi}\right\Vert ^{2}}\hat{\mathbf{\Psi}}^{2}

where :math:`\mathbf{I}` is the :math:`3\times3` identity operator, :math:`\hat{\mathbf{\Psi}}` creates the skew symmetric matrix
out of a 3-vector :math:`\mathbf{\Psi}`, and :math:`\left\Vert \cdot\right\Vert` stands for the Euclidean norm. The time step is denoted as :math:`h`.

.. _deformable-integration:

Deformable integration
----------------------

Deformable time integrator reads

.. math::
  :label: q(t+h/2)

  \mathbf{q}^{t+\frac{h}{2}}=\mathbf{q}^{t}+\frac{h}{2}\mathbf{u}^{t}

.. math::
  :label: u(t+h)

  \mathbf{u}^{t+h}=\mathbf{u}^{t}+\mathbf{A}^{-1}h\mathbf{f}\left(\mathbf{q}^{t+\frac{h}{2}},\mathbf{u}^{t}\right)

.. math::
  :label: q(t+h)

  \mathbf{q}^{t+h}=\mathbf{q}^{t+\frac{h}{2}}+\frac{h}{2}\mathbf{u}^{t+h}

where in the explicit case

.. math::
  :label: Aexp

  \mathbf{A}=\mathbf{M}\text{ for DEF_EXP}

and in the linearly implicit case

.. math::
  :label: Aimp

  \mathbf{A}=\mathbf{M}+\left(\frac{\eta h}{2}+\frac{h^{2}}{4}\right)\mathbf{K}\left(\mathbf{q}^{t+h/2}\right)\text{ for DEF_LIM}

The time step is denoted as :math:`h`.

Implementation
--------------

Time integration is implement in `bod.c <https://github.com/tkoziara/solfec/blob/master/bod.c>`_ (rigid, pseudo--rigid)
and `fem.c <https://github.com/tkoziara/solfec/blob/master/bod.c>`_ (finite--element) files. Inverse generalized
inertia matrix :math:`\mathbf{A}^{-1}` is declared in `bod.h <https://github.com/tkoziara/solfec/blob/master/bod.h#L176>`_ as follows:

.. literalinclude:: ../../../solfec/bod.h
   :lines: 139-140
   :lineno-start: 139
   :linenos:

.. literalinclude:: ../../../solfec/bod.h
   :lines: 176-176
   :lineno-start: 176
   :linenos:

.. literalinclude:: ../../../solfec/bod.h
   :lines: 214
   :lineno-start: 214
   :linenos:

.. |br| raw:: html

  <br />

Rigid integration formulae :eq:`R(t+h/2)`-:eq:`W1(t+h)` are in
`bod.c:BODY_Dynamic_Step_Begin <https://github.com/tkoziara/solfec/blob/master/bod.c#L1296>`_. |br|
Rigid integration formulae :eq:`R1(t+h)`-:eq:`R2(t+h)` are in
`bod.c:BODY_Dynamic_Step_End <https://github.com/tkoziara/solfec/blob/master/bod.c#L1403>`_. |br|
Pseudo--rigid integration is included in the same routines:
`first half--step <https://github.com/tkoziara/solfec/blob/master/bod.c#L1353>`_ and
`second half--step <https://github.com/tkoziara/solfec/blob/master/bod.c#L1467>`_. |br|
Finite--element, total Lagrangian formulation based, integration formulae :eq:`q(t+h/2)` and :eq:`u(t+h)`
are in `fem.c:TL_dynamic_step_begin <https://github.com/tkoziara/solfec/blob/master/fem.c#L1879>`_. |br|
Finite--element, total Lagrangian formulation based, integration formula :eq:`q(t+h)`
is in `fem.c:TL_dynamic_step_end <https://github.com/tkoziara/solfec/blob/master/fem.c#L1930>`_. |br|

.. [1] `IJNME, 81(9):1073--1092, 2010. <http://onlinelibrary.wiley.com/doi/10.1002/nme.2711/full>`_ 
.. [2] `Koziara, PhD thesis, 2008. <http://theses.gla.ac.uk/429/>`_ 
.. [3] `ANM, 25(2--3): 297--302, 1997. <http://www.sciencedirect.com/science/article/pii/S0168927497000664>`_
