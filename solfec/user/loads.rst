.. _solfec-user-loads:

Loads
=====

Routines listed in this section apply loads.

.. _solfec-user-gravity:

GRAVITY
-------

This routine sets up the gravitational acceleration.

.. topic:: GRAVITY (solfec, vector)

  * solfec -- SOLFEC object for which the acceleration is set up

  * vector -- (vx, vy, vz) tuple defining the gravity acceleration.
    Each entry is a number or a TIME_SERIES object defining the value of the acceleration component.

FORCE
-----

This routine applies a point force to a body.

.. topic:: FORCE (body, kind, point, direction, value | data)

  * body -- BODY object to which the force is applied

  * kind -- either 'SPATIAL' or 'CONVECTED'; the spatial direction remains fixed, while the convected one follows deformation

  * point -- (x, y, z) tuple with the referential point where the force is applied

  * direction -- (vx, vy, vz) tuple defining the direction of force

  * value -- a number, a TIME_SERIES object or a callback routine defining the value of
    the applied force. In case of a callback routine, the following format is assumed: 

    **force = value_callback (data, q, u, time, step)**

    where data is the optional user data passed to FORCE routine (if data is a tuple it will expand
    the list of parameters to the callback), q is the configuration of the body passed to the callback,
    u is the velocity of the body passed to the callback, time is the current time passed to the callback
    and step is the current time step passed to the callback. The callback returns a force tuple.
    For rigid body the force reads (spatial force, spatial torque, referential torque), while for other
    kinds of bodies this is a generalized force of the same dimension as the velocity u (power conjugate to it).

  * data -- callback routine user data

TORQUE
------

This routine applies a torque to a rigid body.

.. topic:: TORQUE (body, kind, direction, value)

  * body -- BODY object of kind 'RIGID' to which the torque is applied

  * kind -- either 'SPATIAL' or 'CONVECTED'; the spatial direction remains fixed, while the convected one follows deformation

  * direction -- (vx, vy, vz) tuple defining the direction of torque

  * value -- a number or a TIME_SERIES object defining the value of the applied torque

PRESSURE
--------

This routine applies a constant surface pressure to MESH based bodies.

.. topic:: PRESSURE (body, surfid, value)

  * body -- BODY object to which the pressure is applied (the shape has to be composed of a single MESH)

  * surfid -- the integer surface identifier

  * value -- a number or a TIME_SERIES object defining the value of the applied load
