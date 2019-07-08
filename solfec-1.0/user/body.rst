.. _solfec-1.0-user-body:

BODY object
===========

An object of type BODY represents a solid body.

.. topic:: obj = BODY (solfec, kind, shape, material | label, form, mesh, base)

  This routine creates a body.

  * obj -- created BODY object

  * solfec -- obj is created for this SOLFEC object

  * kind -- a string: 'RIGID', 'PSEUDO_RIGID', 'FINITE_ELEMENT' or
    'OBSTACLE' describing the kinematic model. See :numref:`body-kind`
    and the :ref:`Kinematics manual page <solfec-1.0-theory-kinematics>`.

  * shape (emptied) - this is can be a CONVEX/MESH/SPHERE/ELLIP object, or a list [obj1, obj2, ...],
    where each object is of type CONVEX/MESH/SPHERE/ELLIP. If the kind is 'FINITE_ELEMENT',
    then two cases are possible:

    * shape is a single MESH object: the mesh describes both
      the shape and the discretisation of the motion of a body

    * shape is solely composed of CONVEX objects: here a separate mesh must
      be given to discretise motion of a body (see the mesh argument below) 

  * material -- a :ref:`BULK_MATERIAL <solfec-1.0-command-BULK_MATERIAL>` object or a label of a bulk material;
    specifies an initial body--wise material, see also :ref:`APPLY_BULKMAT <solfec-1.0-command-APPLY_BULKMAT>`

  * label -- a label string (no label is assigned by default)

  * form -- valid when kind equals 'FINITE_ELEMENT', ignored otherwise (default: 'TL').
    This argument specifies a formulation of the finite element method. See :numref:`fem-form`.

  * mesh -- optional when kind equals 'FINITE_ELEMENT', ignored otherwise. This variable must be a MESH object
    describing a finite element mesh properly containing the shape composed solely of CONVEX objects. This way
    the 'FINITE_ELEMENT' model allows to handle complicated shapes with less finite elements,
    e.g. an arbitrary shape could be contained in just one hexahedron.

  * base -- optional reduced order or modal base definition, or a string label of a :ref:`registered base <solfec-1.0-command-REGISTER_BASE>`;
    when **form** = 'BC--MODAL', results of :ref:`the MODAL_ANALYSIS command <solfec-1.0-command-MODAL_ANALYSIS>`, or equivalent user data,
    can be used; the same format is used for the 'BC--RO' formulation; This argument must be passed if **form** = 'BC--MODAL' or 'BC--RO',
    see Table :numref:`fem-form`.

Some parameters can also be accessed as members of a BODY object, cf. :numref:`body-params`.

.. role:: red

.. _body-params:

.. table:: BODY object parameters.

  +---------------------------------------------------------------------------------------------------------+
  | **Read only members:**                                                                                  |
  +---------------------------------------------------------------------------------------------------------+
  | *obj.kind, obj.label, obj.material*                                                                     |
  +---------------------------------------------------------------------------------------------------------+
  | **obj.mass** -- referential mass of the body                                                            |
  +---------------------------------------------------------------------------------------------------------+
  | **obj.volume** -- referential volume of the body                                                        |
  +---------------------------------------------------------------------------------------------------------+
  | **obj.center** -- referential mass center of the body                                                   |
  +---------------------------------------------------------------------------------------------------------+
  | **obj.tensor** -- referential Euler (pseudo-rigid, finite element kinematics)                           |
  | or inertia tensor (rigid kinematics) of the body                                                        |
  +---------------------------------------------------------------------------------------------------------+
  | **obj.constraints** -- list of constraints attached to the body                                         |
  | (cf. :ref:`Constraints <solfec-1.0-user-constraints>`)                                                  |
  +---------------------------------------------------------------------------------------------------------+
  | **obj.ncon** -- number of constraints attached to the body                                              |
  +---------------------------------------------------------------------------------------------------------+
  | **obj.id** -- unique identifier                                                                         |
  +---------------------------------------------------------------------------------------------------------+
  | **obj.display_points** -- list of tuples of display point labels and coordinates:                       |
  | [('label', (x, y, z)), ('label', (x, y, z)), ...]                                                       |
  +---------------------------------------------------------------------------------------------------------+
  | **obj.mesh** -- returns computational MESH associated with a 'FINITE_ELEMENT' body; for other body      |
  | kinds a MESH or a list of MESH objects is returned if such are present as components of the body shape  |
  +---------------------------------------------------------------------------------------------------------+
  | **Read/write members:**                                                                                 |
  +---------------------------------------------------------------------------------------------------------+
  | **obj.conf** -- tuple (q1, q2, ..., qN) storing configuration of the body. See :numref:`body-conf`.     |
  +---------------------------------------------------------------------------------------------------------+
  | **obj.velo** -- tuple (u1, u2, ..., uN) storing velocity of the body. See :numref:`body-velo`.          |
  +---------------------------------------------------------------------------------------------------------+
  | **obj.selfcontact** -- self-contact detection flag (default: 'OFF”) taking values 'ON' or 'OFF'         |
  +---------------------------------------------------------------------------------------------------------+
  | **obj.scheme** -- time integration scheme (default: 'DEFAULT') used to integrate motion. See            |
  | :numref:`solfec-1.0-body-scheme` and the                                                                |
  | :ref:`Time integration manual page <solfec-1.0-theory-timeint>`.                                        |
  +---------------------------------------------------------------------------------------------------------+
  | **obj.damping** -- stiffness proportional damping coefficient (default: 0.0) for the dynamic case       |
  | (ignored for rigid bodies).                                                                             |
  +---------------------------------------------------------------------------------------------------------+
  | **obj.fracturecheck** -- check fracture criterion for FEM bodies ('ON', or default: 'OFF').             |
  | :red:`(Under development)`                                                                              |
  +---------------------------------------------------------------------------------------------------------+
  | **obj.disable_rotation** -- for rigid bodies disable integration of rotation ('ON', or default: 'OFF')  |
  +---------------------------------------------------------------------------------------------------------+

|

.. _body-kind:

.. table:: Body kinds. See also the :ref:`Kinematics manual page <solfec-1.0-theory-kinematics>`.

  +-------------------+-------------------------------------------------------------------------------------+
  | Body kind         | Remarks                                                                             |
  +-------------------+-------------------------------------------------------------------------------------+
  | 'OBSTACLE'        | A rigid body ignoring external loads and not contributing to contact constraints.   |
  |                   | Motion of an obstacle can be controlled through single-body constraints.            |
  |                   | An obstacle--to--obstacle contact is ignored. Moving obstacles will not correctly   |
  |                   | work in the quasi--static case (use rigid bodies instead). Obstacle bodies do       |
  |                   | generate contact constraints with other non-obstacle bodies.                        |
  +-------------------+-------------------------------------------------------------------------------------+
  | 'RIGID'           | A rigid body                                                                        |
  +-------------------+-------------------------------------------------------------------------------------+
  | 'PSEUDO_RIGID'    | A body with global linear deformation state                                         |
  +-------------------+-------------------------------------------------------------------------------------+
  | 'FINITE_ELEMENT'  | A body discretised with finite elements.                                            |
  |                   | Only first order elements are supported at present.                                 |
  +-------------------+-------------------------------------------------------------------------------------+

|

.. _fem-form:

.. table:: Finite element formulations.

  +------------------------+-------------------------------------------------------------------------------------+
  | Formulation            | Remarks                                                                             |
  +------------------------+-------------------------------------------------------------------------------------+
  | 'TL'                   | Total Lagrangian (default)                                                          |
  +------------------------+-------------------------------------------------------------------------------------+
  | 'BC'                   | Body co--rotational (one co--rotated frame per body, suitable for stiff bodies);    |
  |                        | See :ref:`TR1 <tr1>` for technical details                                          |
  +------------------------+-------------------------------------------------------------------------------------+
  | 'BC--MODAL'            | Body co--rotational, modal approach; 'DEF_LIM' integration scheme is always used for|
  |                        | this formulation (there is no computational advantage in using 'DEF_EXP' since all  |
  |                        | system matrices are diagonal); *Note:* the **base** argument must be passed;        |
  |                        | See :ref:`TR1 <tr1>` for technical details; :red:`(Experimental)`                   | 
  +------------------------+-------------------------------------------------------------------------------------+
  | 'BC--RO '              | Body co--rotational, reduced order approach; 'DEF_LIM' integration scheme is always |
  |                        | used for this formulation (there is no computational advantage in using 'DEF_EXP'   |
  |                        | since all system matrices are dense); *Note:** the **base** argument must be        |
  |                        | passed; See :ref:`TR1 <tr1>` for technical details; :red:`(Experimental)`           |
  +------------------------+-------------------------------------------------------------------------------------+
 
|

.. _body-conf:

.. table:: Types of configurations.

  +-------------------+-------------------------------------------------------------------------------------+
  | Body kind         | Configuration description                                                           |
  +-------------------+-------------------------------------------------------------------------------------+
  | 'OBSTACLE'        | Column--wise rotation matrix followed by the current mass center                    |
  +-------------------+-------------------------------------------------------------------------------------+
  | 'RIGID'           | Column--wise rotation matrix followed by the current mass center                    |
  +-------------------+-------------------------------------------------------------------------------------+
  | 'PSEUDO_RIGID'    | Column--wise deformation gradient followed by the current mass center               |
  +-------------------+-------------------------------------------------------------------------------------+
  | 'FINITE_ELEMENT'  | Current coordinates x, y, z of mesh nodes                                           |
  +-------------------+-------------------------------------------------------------------------------------+

|

.. _body-velo:

.. table:: Types of velocities.

  +-------------------+-------------------------------------------------------------------------------------+
  | Body kind         | Velocity description                                                                |
  +-------------------+-------------------------------------------------------------------------------------+
  | 'OBSTACLE'        | Referential angular velocity followed by the spatial velocity of mass center        |
  +-------------------+-------------------------------------------------------------------------------------+
  | 'RIGID'           | Referential angular velocity followed by the spatial velocity of mass center        |
  +-------------------+-------------------------------------------------------------------------------------+
  | 'PSEUDO_RIGID'    | Deformation gradient velocity followed by the spatial velocity of mass center       |
  +-------------------+-------------------------------------------------------------------------------------+
  | 'FINITE_ELEMENT'  | Components x, y, z of spatial velocities of mesh nodes                              |
  +-------------------+-------------------------------------------------------------------------------------+

|

.. _solfec-1.0-body-scheme:

.. table:: Time integration schema. See also the :ref:`Time integration manual page <solfec-1.0-theory-timeint>`.

  +-----------+----------------+----------------------------------------------------------------------------+
  | Scheme    | Kinematics     | Remarks                                                                    |
  +-----------+----------------+----------------------------------------------------------------------------+
  | 'DEFAULT' | all            | Use a default time integrator regardless of underlying kinematics          |
  +-----------+----------------+----------------------------------------------------------------------------+
  | 'RIG_POS' | rigid          | NEW1 in [1]_: explicit, positive energy drift, no momentum conservation    |
  +-----------+----------------+----------------------------------------------------------------------------+
  | 'RIG_NEG' | rigid          | NEW2 in [1]_: explicit, negative energy drift, exact momentum conservation;|
  |           |                | **default** for rigid kinematics                                           |
  +-----------+----------------+----------------------------------------------------------------------------+
  | 'RIG_IMP' | rigid          | NEW3 in [1]_: semi-explicit, no energy drift and exact momentum            |
  |           |                | conservation                                                               |
  +-----------+----------------+----------------------------------------------------------------------------+
  | 'DEF_EXP' | pseudo--rigid, | Explicit scheme described in Chapter 5 of [2]_; **default** for deformable |
  |           | finite element | kinematics, energy and momentum conserving, conditionally stable           |
  +-----------+----------------+----------------------------------------------------------------------------+
  | 'DEF_LIM' | pseudo--rigid, | Linearly implicit scheme similar to [3]_; energy and momentum conserving,  |
  |           | finite element | stable for moderate to large steps; See :ref:`TR1 <tr1>` for technical     |
  |           |                | details                                                                    |
  +-----------+----------------+----------------------------------------------------------------------------+

References:

.. [1] `IJNME, 81(9):1073--1092, 2010. <http://onlinelibrary.wiley.com/doi/10.1002/nme.2711/full>`_
.. [2] `Koziara, PhD thesis, 2008. <http://theses.gla.ac.uk/429/>`_
.. [3] `ANM, 25(2--3): 297--302, 1997. <http://www.sciencedirect.com/science/article/pii/S0168927497000664>`_
