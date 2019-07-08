.. _solfec-1.0-user-constraints:

Constraints
===========

An object of type CONSTRAINT represents a constraint and its associated data (e.g. constraint reaction).
Both, user prescribed constraints (routines below) and contact constraints (detected automatically) are
represented by an object of the same type. See also, the :ref:`Joints section <solfec-1.0-theory-joints>`.

.. _solfec-1.0-command-FIX_POINT:

FIX_POINT
---------

This routine creates a :ref:`fixed point constraint <fixed-point>`.

.. topic:: obj = FIX_POINT (body, point | strength)

  * obj -- created CONSTRAINT object

  * body -- BODY object whose motion is constrained

  * point -- (x, y, z) tuple with referential point coordinates

  * strength - optionally an ultimate magnitude of the reaction force, beyond which the constraint will be deleted (default: infinity)

.. _solfec-1.0-command-FIX_DIRECTION:

FIX_DIRECTION 
-------------

This routine fixes the motion of a referential point along a specified spatial direction.
If body2 is given the motion of point2 along the direction convected with the first body is fixed.
See also, formulation of the :ref:`fixed direction constraint <fixed-direction>`.

.. topic:: obj = FIX_DIRECTION (body, point, direction | body2, point2)

  * obj -- created CONSTRAINT object

  * body -- BODY object whose motion is constrained

  * point -- (x, y, z) tuple with referential point coordinates

  * direction -- (vx, vy, vz) tuple with spatial direction components 

  * body2 -- BODY object whose motion is constrained with respect to the motion of the first body (in this case body and body2 can only be either rigid or pseudo-rigid)

  * point2 -- (x, y, z) tuple with referential point on body2

.. _solfec-1.0-command-SET_DISPLACEMENT: 

SET_DISPLACEMENT 
----------------

This routine prescribes a displacement history of a referential point along a specified spacial direction.
See also, formulation of the :ref:`prescribed displacement constraint <prescribed-displacement>`.

.. topic:: obj = SET_DISPLACEMENT (body, point, direction, tms)

  * obj -- created CONSTRAINT object

  * body -- BODY object whose motion is constrained

  * point -- (x, y, z) tuple with referential point coordinates

  * direction -- (vx, vy, vz) tuple with spatial direction components

  * tms -- TIME_SERIES object with the displacement history

.. _solfec-1.0-command-SET_VELOCITY: 

SET_VELOCITY 
------------

This routine prescribes a velocity history of a referential point along a specified spacial direction.
See also, formulation of the :ref:`prescribed velocity constraint <prescribed-velocity>`.

.. topic:: obj = SET_VELOCITY (body, point, direction, value)

  * obj -- created CONSTRAINT object

  * body -- BODY object whose motion is constrained

  * point -- (x, y, z) tuple with referential point coordinates

  * direction -- (vx, vy, vz) tuple with spatial direction components

  * value -- a constant value or a TIME_SERIES object with the velocity history

.. _solfec-1.0-command-SET_ACCELERATION: 

SET_ACCELERATION 
----------------

This routine prescribes an acceleration history of a referential point along a specified spacial direction.
See also, formulation of the :ref:`prescribed acceleration constraint <prescribed-acceleration>`.

.. topic:: obj = SET_ACCELERATION (body, point, direction, tms)

  * obj -- created CONSTRAINT object

  * body -- BODY object whose motion is constrained

  * point -- (x, y, z) tuple with referential point coordinates

  * direction -- (vx, vy, vz) tuple with spatial direction components

  * tms -- TIME_SERIES object with the acceleration history

.. _solfec-1.0-command-PUT_RIGID_LINK: 

PUT_RIGID_LINK 
--------------

This routine creates a rigid link constraints between two referential points of two distinct bodies.
See also, formulation of the :ref:`rigid link constraint <rigid-link>`.

.. topic:: obj = PUT_RIGID_LINK (body1, body2, point1, point2 | strength)

  • obj -- created CONSTRAINT object

  • body1 -- BODY object one whose motion is constrained (could be *None* when body2 is not *None* -- then one of the points is fixed “in the air”)

  • body2 -- BODY object two whose motion is constrained (could be *None* when body1 is not *None*)

  • point1 -- (x1, y1, z1) tuple with the first referential point coordinates

  • point2 -- (x2, y2, z2) tuple with the second referential point coordinates

  • strength -- optionally an ultimate tensile strength if point1 != point2,
    beyond which the link will be deleted (default: infinity); or ultimate reaction magnitude (point1 == point2)

.. role:: red

.. _solfec-1.0-command-PUT_SPRING:

PUT_SPRING 
----------

This routine creates an arbitrary spring between two referential points of two distinct bodies.
See also, formulation of the :ref:`spring constraint <simple-spring>`.

.. topic:: obj = PUT_SPRING (body1, point1, body2, point2, function, limits | direction, update) :red:`(Experimental)`

  * obj -- created CONSTRAINT object

  * body1 -- BODY object one whose motion is constrained

  * point1 -- (x1, y1, z1) tuple with the first referential point coordinates

  * body2 -- BODY object two whose motion is constrained

  * point2 -- (x2, y2, z2) tuple with the second referential point coordinates

  * function -- Python function callback returning the value of force as the function of stroke:
  
    **force = function (stroke, velocity)**

    where :math:`\text{stroke=}\mathbf{n}\cdot\text{current}\left(\text{point2}-\text{point1}\right)-\text{initial}\left(\left|\text{point2}-\text{point1}\right|\right)`
    and *velocity* is the current relative velocity along the spring direction :math:`\mathbf{n}` (positive if stroke increases).
    See also: :ref:`REGISTER_CALLBACK <solfec-1.0-command-REGISTER_CALLBACK>`.

  * limits -- (smin, smax) tuple defining stroke limits (smin :math:`\le` 0 and smax :math:`\ge` 0)

  * direction -- (nx, ny, nz) tuple storing spring direction :math:`\mathbf{n}`.
    Default: :math:`\mathbf{n}=\text{normalized}\left(\text{current}\left(\text{point2}-\text{point1}\right)\right)` resulting in a follower type spring.
    When specified, :math:`\mathbf{n}` will be updated according to the value of update.

  * update -- direction update kind (default: 'FIXED'); one of: 'FIXED' where :math:`\mathbf{n}` is kept fixed,
    or 'CONV1' where :math:`\mathbf{n}` is convected with body1, or 'CONV2' where :math:`\mathbf{n}` is convected with body2.

Some parameters can also be accessed as members of a CONSTRAINT object, cf. :numref:`constraint-params`.

.. _constraint-params:

.. table:: CONSTRAINT object parameters.

  +---------------------------------------------------------------------------------------------------------+
  | **Read only members:**                                                                                  |
  +---------------------------------------------------------------------------------------------------------+
  | **obj.kind** -- kind of constraint: 'CONTACT', 'FIXPNT' (fixed point), 'FIXDIR' (fixed direction),      |
  | 'VELODIR' (prescribed velocity; note that prescribed displacement and acceleration are converted into   |
  | this case), 'RIGLNK' (rigid link)                                                                       |
  +---------------------------------------------------------------------------------------------------------+
  | **obj.R** -- current average (over time step :math:`\left[t,t+h\right]`) constraint reaction in a form  |
  | of a tuple: (RT1, RT2, RN) given with respect to a local base stored at *obj.base*                      |
  +---------------------------------------------------------------------------------------------------------+
  | **obj.U** -- constraint output relative velocity tuple: (UT1, UT2, UN) given with respect to a local    |
  | base stored at *obj.base*                                                                               |
  +---------------------------------------------------------------------------------------------------------+
  | **obj.V** -- contact input relative velocity tuple: (VT1, VT2, VN) given with respect to a local base   |
  | stored at *obj.base*                                                                                    |
  +---------------------------------------------------------------------------------------------------------+
  | **obj.base** -- current spatial coordinate system in a form of a tuple: (eT1x, eT2x, eNx, eT1y, eT2y,   |
  | eNy, eT1z, eT2z, eNz) where x, y, z components are global                                               |
  +---------------------------------------------------------------------------------------------------------+
  | **obj.point** -- current spatial point where the constraint force acts. This is a (x, y, z) tuple for   |
  | all constraint types, but 'RIGLNK' for which this is a (x1, y1, z1, x2, y2, z2) tuple.                  |
  +---------------------------------------------------------------------------------------------------------+
  | **obj.area** -- current area for contact constraints or zero otherwise                                  |
  +---------------------------------------------------------------------------------------------------------+
  | **obj.gap** -- current gap for contact constraints or zero otherwise                                    |
  +---------------------------------------------------------------------------------------------------------+
  | **obj.merit** -- current value of the per--constraint merit function                                    |
  +---------------------------------------------------------------------------------------------------------+
  | **obj.adjbod** -- adjacent bodies. This is a tuple (body1, body2) of BODY objects for 'CONTACT' and     |
  | 'RIGLNK' or a single BODY object otherwise.                                                             |
  +---------------------------------------------------------------------------------------------------------+
  | **obj.matlab** - surface material label for constraints of kind 'CONTACT', or a *None* object otherwise.|
  +---------------------------------------------------------------------------------------------------------+
  | **obj.spair** - pairing of surfaces (surf1, surf2) for contact constraints or *None* object otherwise.  |
  | The tuple (surf1, surf2) corresponds to the surface identifiers for the (body1, body2) body pairing     |
  | returned by *obj.adjbod*                                                                                |
  +---------------------------------------------------------------------------------------------------------+
