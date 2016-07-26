.. _solfec-theory-kinematics:

Kinematics
==========

A kinematic model defines an allowed type of deformation for an individual body. Solfec includes three kinematic models:

* rigid body
* pseudo--rigid body
* finite--element body

A kinematic model is selected by specifying the *kind* paramter of the :ref:`BODY command <solfec-user-body>`.

.. role:: red

Rigid body
----------

The motion of a rigid body reads

.. math::
  :label: rigmot

  \mathbf{x}\left(\mathbf{X},t\right)=\mathbf{\Lambda}\left(t\right)\left(\mathbf{X}-\bar{\mathbf{X}}\right)+\bar{\mathbf{x}}\left(t\right)

where :math:`\mathbf{\Lambda}\left(t\right)` is a :math:`3\times3` rotation matrix, :math:`\bar{\mathbf{X}}` is a selected referential point,
and :math:`\bar{\mathbf{x}}\left(t\right)` is a spatial point. Hence :math:`\bar{\mathbf{x}}\left(t\right)=\mathbf{x}\left(\bar{\mathbf{X}},t\right)`
is the motion of the selected point :math:`\bar{\mathbf{X}}`. The term :math:`\mathbf{\Lambda}\left(t\right)\left(\mathbf{X}-\bar{\mathbf{X}}\right)`
represents the rotation of :math:`\mathbf{X}` about the point :math:`\bar{\mathbf{X}}`. Representing rotations, :math:`\mathbf{\Lambda}`
must be orthogonal: :math:`\mathbf{\Lambda}^{T}\mathbf{\Lambda}=\mathbf{I}`, where :math:`\mathbf{I}` is the :math:`3\times3` identity matrix.
Thus, the rigidity condition follows :math:`\left\Vert \mathbf{x}-\bar{\mathbf{x}}\right\Vert =\left\Vert \mathbf{X}-\bar{\mathbf{X}}\right\Vert`,
that is the length of a line segment before and after rotation is preserved.

:red:`TODO`: talk about velocity and present vector notation.

Pseudo--rigid body
------------------

The motion of a pseudo--rigid body reads

.. math::
  :label: prbmot

  \mathbf{x}\left(t\right)=\mathbf{F}\left(t\right)\left(\mathbf{X}-\bar{\mathbf{X}}\right)+\bar{\mathbf{x}}\left(t\right)
  
where :math:`\mathbf{x}` is the current image of a referential point :math:`\mathbf{X}`, :math:`\mathbf{F}` is a spatially homogeneous
deformation gradient :math:`\left(\mathbf{F}=\partial\mathbf{x}/\partial\mathbf{X}\right), \bar{\mathbf{X}}` is a selected referential point
and :math:`\bar{\mathbf{x}}=\bar{\mathbf{x}}\left(t\right)` is the current image of :math:`\bar{\mathbf{X}}`. Deformation gradient 
:math:`\mathbf{F}` is an invertible and orientation preserving :math:`\left(\det\left(\mathbf{F}\right)>0\right)` :math:`3\times3` matrix.

:red:`TODO`: talk about velocity and present vector notation.

Finite--element body
--------------------

The finite--element motion reads

.. math::
  :label: femmot

  \mathbf{x}\left(\mathbf{X},t\right)=\mathbf{X}+\mathbf{N}\left(\mathbf{X}\right)\mathbf{q}\left(t\right)
  
where :math:`\mathbf{x}` is the current image of the referential point :math:`\mathbf{X}`, :math:`\mathbf{N}\left(\mathbf{X}\right)`
is a matrix of shape functions, and :math:`\mathbf{q}\left(t\right)` is a vector of nodal displacements.

:red:`TODO`: talk about velocity and present vector notation.

Implementation
--------------

Kinematic models are implement in `bod.c <https://github.com/tkoziara/solfec/blob/master/bod.c>`_ (rigid, pseudo--rigid)
and `fem.c <https://github.com/tkoziara/solfec/blob/master/bod.c>`_ (finite--element) files. Configuration and velocity
vectors are declared in `bod.h <https://github.com/tkoziara/solfec/blob/master/bod.h#L153>`_ as follows:

.. literalinclude:: ../../../solfec/bod.h
   :lines: 139-140
   :lineno-start: 139
   :linenos:

.. literalinclude:: ../../../solfec/bod.h
   :lines: 153-154
   :lineno-start: 153
   :linenos:

.. literalinclude:: ../../../solfec/bod.h
   :lines: 214
   :lineno-start: 214
   :linenos:
