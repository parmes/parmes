.. _solfec-theory-kinematics:

Kinematics
==========

A kinematic model defines an allowed type of deformation for an individual body. Solfec-1.0 includes three kinematic models:

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

The velocity of the spatial point reads

.. math::
  :label: rigvel
  
  \dot{\mathbf{x}}\left(\mathbf{X},t\right)=\mathbf{\Lambda}\left(t\right)\hat{\mathbf{\Omega}}\left(t\right)
  \left(\mathbf{X}-\bar{\mathbf{X}}\right)+\dot{\bar{\mathbf{x}}}\left(t\right)=\hat{\mathbf{\omega}}\left(t\right)
  \mathbf{\Lambda}\left(t\right)\left(\mathbf{X}-\bar{\mathbf{X}}\right)+\dot{\bar{\mathbf{x}}}\left(t\right)
  
where :math:`\mathbf{\omega}` is the spatial angular velocity vector, :math:`\mathbf{\Omega}` is the referential
angular velocity vector, and :math:`\dot{\bar{\mathbf{x}}}` is the velocity of the spatial image of :math:`\bar{\mathbf{X}}`.
W note that

.. math::

  \mathbf{\omega}=\mathbf{\Lambda}\mathbf{\Omega}

The hat operator :math:`\hat{\mathbf{y}}` creates an anti--symmetric :math:`3\times3` matrix out of a 3--vector as follows

.. _hat:

.. math::

  \hat{\mathbf{y}}=\left[\begin{array}{ccc}
  0 & -y_{3} & y_{2}\\
  y_{3} & 0 & -y_{1}\\
  -y_{2} & y_{1} & 0
  \end{array}\right]
  
In vector notation the configuration :math:`\mathbf{q}` and the velocity :math:`\mathbf{u}` can be expressed as

.. _qurig:

.. math::
  :label: qurig

  \mathbf{q}=\left[\begin{array}{c}
  \Lambda_{11}\\
  \Lambda_{21}\\
  ...\\
  \bar{x}_{1}\\
  \bar{x}_{2}\\
  \bar{x}_{3}
  \end{array}\right],\,\,\,\mathbf{u}=\left[\begin{array}{c}
  \Omega_{1}\\
  \Omega_{2}\\
  \Omega_{3}\\
  \dot{\bar{x}}_{1}\\
  \dot{\bar{x}}_{2}\\
  \dot{\bar{x}}_{3}
  \end{array}\right]

The configuration :math:`\mathbf{q}` has 12 components and the velocity :math:`\mathbf{u}` has 6 components.

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

The velocity of the spatial point reads

.. math::
  :label: prbvel

  \dot{\mathbf{x}}\left(t\right)=\dot{\mathbf{F}}\left(t\right)\left(\mathbf{X}-\bar{\mathbf{X}}\right)+\dot{\bar{\mathbf{x}}}\left(t\right)
  
where :math:`\dot{\mathbf{F}}` is the velocity of the deformation gradient and :math:`\dot{\bar{\mathbf{x}}}` is the velocity of the spatial
image of :math:`\bar{\mathbf{X}}`.

.. _pseudo-rigid-vectors:

In vector notation the configuration :math:`\mathbf{q}` and the velocity :math:`\mathbf{u}` can be expressed as

.. _quprb:

.. math::
  :label: quprb

  \mathbf{q}=\left[\begin{array}{c}
  F_{11}\\
  F_{12}\\
  ...\\
  \bar{x}_{1}\\
  \bar{x}_{2}\\
  \bar{x}_{3}
  \end{array}\right],\,\,\,\mathbf{u}=\left[\begin{array}{c}
  \dot{F}_{11}\\
  \dot{F}_{12}\\
  ...\\
  \dot{\bar{x}}_{1}\\
  \dot{\bar{x}}_{2}\\
  \dot{\bar{x}}_{3}
  \end{array}\right]

Both, the configuration :math:`\mathbf{q}` and the velocity :math:`\mathbf{u}` are 12--component vectors.

Finite--element body
--------------------

The finite--element motion reads

.. math::
  :label: femmot

  \mathbf{x}\left(\mathbf{X},t\right)=\mathbf{X}+\mathbf{N}\left(\mathbf{X}\right)\mathbf{q}\left(t\right)
  
where :math:`\mathbf{x}` is the current image of the referential point :math:`\mathbf{X}`, :math:`\mathbf{N}\left(\mathbf{X}\right)`
is a matrix of shape functions, and :math:`\mathbf{q}\left(t\right)` is a vector of nodal displacements.

The velocity of the spatial point reads

.. math::
  :label: femvel
  
  \dot{\mathbf{x}}\left(\mathbf{X},t\right)=\mathbf{N}\left(\mathbf{X}\right)\dot{\mathbf{q}}\left(t\right)
  
where :math:`\dot{\mathbf{q}}` is the vector of nodal :math:`x,y,z` velocities.

In vector notation, the configuration :math:`\mathbf{q}` and the velocity :math:`\mathbf{u}` can be expressed as

.. _qufem:

.. math::
  :label: qufem

  \mathbf{q}=\left[\begin{array}{c}
  q_{1x}\\
  q_{1y}\\
  q_{1z}\\
  ...\\
  q_{nx}\\
  q_{ny}\\
  q_{nz}
  \end{array}\right],\,\,\,\mathbf{u}=\dot{\mathbf{q}}
  
Both, the configuration :math:`\mathbf{q}` and the velocity :math:`\mathbf{u}` have size :math:`3\times n`, where :math:`n` is the number of nodes in a finite--element mesh.

The matrix :math:`\mathbf{N}` in :eq:`femmot` and :eq:`femvel` has the following form

.. math::

  \mathbf{N}=\left[\begin{array}{ccccccc}
  N_{1} &  &  & ... & N_{n}\\
   & N_{1} &  & ... &  & N_{n}\\
    &  & N_{1} & ... &  &  & N_{n}
    \end{array}\right]
    
where :math:`N_{i}` are nodal shape functions, juxtaposed from element shape functions meeting at coincident mesh nodes.

Shape functions
_______________

.. _element-types:

.. figure:: ../figures/elements.png
   :width: 60%
   :align: center

   Element types in Solfec-1.0: tetrahedron, pyramid, wedge, hexahedron.

Finite--element types available in Solfec-1.0 are depicted in :numref:`element-types`. Shape functions for those
elements are summarised in :numref:`element-shapes`.

Isoparametric mapping is used to go back and forth between the natural element coordinates :math:`\xi_{1}`,
:math:`\xi_{2}`, :math:`\xi_{3}`, local to individual element domains, and the referential mesh coordinates
:math:`\mathbf{Y}`

.. math::

  \mathbf{Y}\left(\xi_{1},\xi_{2},\xi_{3}\right)=\mathbf{N}\left(\xi_{1},\xi_{2},\xi_{3}\right)\left[\begin{array}{c}
  \mathbf{Y}_{1}\\
  ...\\
  \mathbf{Y}_{n}
  \end{array}\right]

where :math:`\mathbf{Y}_{i}` are referential coordinates of mesh nodes. The function :math:`\mathbf{N}\left(\mathbf{X}\right)`
in :eq:`femmot` and :eq:`femvel` has the following form

.. math::

  \mathbf{N}\left(\mathbf{X}\right)=\mathbf{N}\left(\mathbf{Y}^{-1}\left(\mathbf{X}\right)\right)
  
Newton iterations are required to solve :math:`\mathbf{X}=\mathbf{Y}\left(\xi_{1},\xi_{2},\xi_{3}\right)`
and find :math:`\xi_{1}`, :math:`\xi_{2}`, :math:`\xi_{3}` for a given referential point :math:`\mathbf{X}`.

.. |br| raw:: html

  <br />

.. _element-shapes:

.. table:: Finite--element shape functions.

  +---------------------------------------------------------------------------------------------------------+
  | **Tetrahedron**                                                                                         |
  +---------------------------------------------------------------------------------------------------------+
  | :math:`N_{1}=1-\left(\xi_{1}+\xi_{2}+\xi_{3}\right)` |br|                                               | 
  | :math:`N_{2}=\xi_{1}` |br|                                                                              |
  | :math:`N_{3}=\xi_{2}` |br|                                                                              |
  | :math:`N_{4}=\xi_{3}` |br|                                                                              |
  +---------------------------------------------------------------------------------------------------------+
  | **Pyramid**                                                                                             |
  +---------------------------------------------------------------------------------------------------------+
  | :math:`r=                                                                                               |
  | \xi_{1}\xi_{2}\xi_{3}/\left(1-\xi_{3}\right)\text{ if }\xi_{3}\ne1\text{ or }0\text{ otherwise}` |br|   |
  | :math:`N_{1}=0.25\left(\left(1+\xi_{1}\right)\left(1+\xi_{2}\right)-\xi_{3}+r\right)` |br|              |
  | :math:`N_{2}=0.25\left(\left(1-\xi_{1}\right)\left(1+\xi_{2}\right)-\xi_{3}-r\right)` |br|              |
  | :math:`N_{3}=0.25\left(\left(1-\xi_{1}\right)\left(1-\xi_{2}\right)-\xi_{3}+r\right)` |br|              |
  | :math:`N_{4}=0.25\left(\left(1+\xi_{1}\right)\left(1-\xi_{2}\right)-\xi_{3}-r\right)` |br|              |
  | :math:`N_{5}=\xi_{3}` |br|                                                                              |
  +---------------------------------------------------------------------------------------------------------+
  | **Wedge**                                                                                               |
  +---------------------------------------------------------------------------------------------------------+
  | :math:`N_{1}=0.5\left(1-\xi_{1}-\xi_{2}\right)\left(1-\xi_{3}\right)` |br|                              |
  | :math:`N_{2}=0.5\xi_{1}\left(1-\xi_{3}\right)` |br|                                                     |
  | :math:`N_{3}=0.5\xi_{2}\left(1-\xi_{3}\right)` |br|                                                     |
  | :math:`N_{4}=0.5\left(1-\xi_{1}-\xi_{2}\right)\left(1+\xi_{3}\right)` |br|                              |
  | :math:`N_{5}=0.5\xi_{1}\left(1+\xi_{3}\right)` |br|                                                     |
  | :math:`N_{6}=0.5\xi_{2}\left(1+\xi_{3}\right)` |br|                                                     |
  +---------------------------------------------------------------------------------------------------------+
  | **Hexahedron**                                                                                          |
  +---------------------------------------------------------------------------------------------------------+
  | :math:`N_{1}=0.125\left(1-\xi_{1}\right)\left(1-\xi_{2}\right)\left(1-\xi_{3}\right)` |br|              |
  | :math:`N_{2}=0.125\left(1+\xi_{1}\right)\left(1-\xi_{2}\right)\left(1-\xi_{3}\right)` |br|              |
  | :math:`N_{3}=0.125\left(1+\xi_{1}\right)\left(1+\xi_{2}\right)\left(1-\xi_{3}\right)` |br|              |
  | :math:`N_{4}=0.125\left(1-\xi_{1}\right)\left(1+\xi_{2}\right)\left(1-\xi_{3}\right)` |br|              |
  | :math:`N_{5}=0.125\left(1-\xi_{1}\right)\left(1-\xi_{2}\right)\left(1+\xi_{3}\right)` |br|              |
  | :math:`N_{6}=0.125\left(1+\xi_{1}\right)\left(1-\xi_{2}\right)\left(1+\xi_{3}\right)` |br|              |
  | :math:`N_{7}=0.125\left(1+\xi_{1}\right)\left(1+\xi_{2}\right)\left(1+\xi_{3}\right)` |br|              |
  | :math:`N_{8}=0.125\left(1-\xi_{1}\right)\left(1+\xi_{2}\right)\left(1+\xi_{3}\right)` |br|              |
  +---------------------------------------------------------------------------------------------------------+
 
Implementation
--------------

Kinematic models are implement in `bod.c <https://github.com/tkoziara/solfec/blob/master/bod.c>`_ (rigid, pseudo--rigid)
and `fem.c <https://github.com/tkoziara/solfec/blob/master/bod.c>`_ (finite--element) files. Configuration and velocity
vectors are declared in `bod.h <https://github.com/tkoziara/solfec/blob/master/bod.h#L150>`_ as follows:

.. code-block:: c

  struct general_body
  {
    enum {OBS, RIG, PRB, FEM} kind; /* obstacle, rigid, pseudo-rigid, finite element */

    /* ... */

    double *conf,    /* configuration */
	   *velo;    /* velocity */

    /* ... */
  }
