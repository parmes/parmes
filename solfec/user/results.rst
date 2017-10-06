.. _solfec-user-results:

Results
=======

Results can be accessed either in the 'READ' mode of a SOLFEC object, or in the 'WRITE' mode
once some analysis has been run. Routines listed in this section facilitate access to results.

DURATION
--------

This routine returns the duration of a simulation in SOLFEC's 'READ' mode, or solfec.time in the 'WRITE' mode.

.. topic:: value = DURATION (solfec)

  * value -- (t0, t1) duration limits of the simulation in 'READ' mode or current time in 'WRITE' mode

  * solfec -- SOLFEC object

.. _solfec-command-FORWARD:

FORWARD
-------

This routine steps forward within the simulation output file. Ignored in SOLFEC's 'WRITE' mode.

.. topic:: FORWARD (solfec, steps | corotated_displacements)

  * solfec -- SOLFEC object

  * steps -- numbers of steps forward

  * corotated_displacements -- optional co--rotated displacements sampling flag; if 'TRUE' and a call or multiple
    calls to :ref:`COROTATED_DISPLACEMENTS <solfec-command-COROTATED_DISPLACEMENTS>` was/were made prior to FORWARD,
    co-rotated displacements will be sampled for every time instant visited by FORWARD (the original sampling interval
    will be ignored); default: 'FALSE'

BACKWARD
--------

This routine steps backward within the simulation output file. Ignored in SOLFEC's 'WRITE' mode.

.. topic:: BACKWARD (solfec, steps)

  * solfec -- SOLFEC object

  * steps -- number of steps backward

SEEK
----

This routine to a specific time within the simulation output file. Ignored in SOLFEC's 'WRITE' mode.

.. topic:: SEEK (solfec, time)

  * solfec -- SOLFEC object

  * time -- time to start reading at

DISPLACEMENT
------------

This routine outputs the displacement of a referential point.

.. topic:: disp = DISPLACEMENT (body, point)

  * disp -- (dx, dy, dz) tuple storing the displacement

  * body -- BODY object

  * point -- (x, y, z) tuple storing the referential point

VELOCITY
--------

This routine outputs the velocity of a referential point.

.. topic:: velo = VELOCITY (body, point)

  * velo -- (vx, vy, vz) tuple storing the velocity

  * body -- BODY object

  * point -- (x, y, z) tuple storing the referential point

STRESS
------

This routine outputs the Cauchy stress of a referential point.

.. topic:: stre = STRESS (body, point)

  * stre -- (sx, sy, sz, sxy, sxz, syz, mises) tuple storing the Cauchy stress and the von Mises norm of it

  * body -- BODY object

  * point -- (x, y, z) tuple storing the referential point

ENERGY
------

The routine outputs the value of energy of a specific object.

.. topic:: ene = ENERGY (solfec | object)

  * ene -- (kinetic, internal, external, contact, friction) tuple of energy values; internal energy corresponds
    to the work of internal forces, external energy corresponds to the work of external forces (including
    constraint reactions), contact energy corresponds to the work of normal contact reactions, friction energy
    corresponds to the work of tangential contact reactions

  * solfec -- SOLFEC object

  * object -- SOLFEC object, BODY object or a list of BODY objects

TIMING
------

The routine outputs the value of a specific action timing per time step.

.. topic:: tim = TIMING (solfec, kind)

  * tim -- value of timing (or Python None object if solfec was in the 'WRITE' mode)

  * solfec -- SOLFEC object in 'READ' mode

  * kind -- this is one of: 'TIMINT' (time integration), 'CONUPD' (constraints update),
    'CONDET' (contact detection), 'LOCDYN' (local dynamics setup), 'CONSOL' (constraints solution),
    'PARBAL' (parallel load balancing). The load balancing timing is non-zero only for parallel runs.

HISTORY
-------

This routine outputs time histories of entities.

.. topic:: hist = HISTORY (solfec, list, t0, t1 | skip, progress)

  * hist -- a tuple of list objects storing the histories: (times, values1, values2, ..., valuesN)

  * solfec -- SOLFEC object

  * list -- list of objects [object1, object2, ..., objectN] indicating requested values. The valid objects are: 

    * a tuple (body, point, entity) where body is a BODY object or a body label string, point is a (x, y, z) tuple storing the
      referential point, and entity is one of: 'CX', 'CY', 'CZ' (current coordinate), 'DX', 'DY', 'DZ' (displacement), 'VX', 'VY',
      'VZ' (velocity), 'SX', 'SY', 'SZ', 'SXY', 'SXZ', 'SYZ' (stress), 'MISES' (von Mises norm of stress); **Note:** if body label
      is used and the body initially did not exist (e.g. it was inserted during simulation or produced as a result of fragmentation)
      corresponding values for times when it did not exit are NaN;

    * a tuple (object, kind) where object is a SOLFEC object, a BODY object or a list of BODY objects,
      and kind is a string 'KINETIC', 'INTERNAL', 'EXTERNAL', 'CONTACT' (included in external),
      'FRICTION' (included in external) and it corresponds to the energy kind;
      if the list of BODY objects is used, their energies are summed up

    * a string 'TIMINT', 'CONUPD', 'CONDET', 'LOCDYN', 'CONSOL', 'PARBAL' for timing histories

    * a string 'STEP' for time step history

    * a string 'CONS', 'BODS' for constraint and body number histories

    * a string 'DELBODS', 'NEWBODS' for deleted and inserted (after time 0) body number histories (nonzero only for uncompressed outputs)

    * a string 'GSITERS' (Gauss-Seidel iterations count), 'GSCOLORS' (Gauss-Seidel processor colors count),
      'GSBOT', 'GSMID', 'GSTOP', 'GSINN' (Gauss-Seidel bottom, middle, top and inner set sizes),
      'GSINIT' (Gauss-Seidel setup time), 'GSRUN' (Gauss-Seidel computations time),
      'GSCOM' (Gauss-Seidel communication time, except the middle set), 'GSMCOM' (Gauss-Seidel middle set communication time);
      values other than 'GSITERS' are non-zero only for parallel runs

    * a string 'MERIT' for the time history of the constraints satisfaction merit function

    * a string 'NTITERS' for the NEWTON_SOLVER iterations count

    * a tuple (object, entity) or (object, direction, pair, entity) where object is a SOLFEC object,
      a BODY object or a list of BODY objects, direction is a tuple :math:`\left(d_{x},d_{y},d_{z}\right)`
      storing a direction (use None if the normal direction is preferred), pair is a tuple (surf1, surf2)
      defining a surface pair (use None if no surface pair is preferred), and entity is:

      - 'GAP' for the time history of the minimal contact gap among constraints attached to given bodies (negative gap corresponds to the penetration depth)

      - 'R' for the time history of the resultant (and average over time step :math:`\left[t,t+h\right]`) constraint reactions along the directions: normal or given by the direction

      - 'U' for the time history of the average constraint velocities along the directions: normal or given by the direction

      - 'CR' for time histories like in the 'R' case, but for contact constraints only

      - 'CU' for time histories like in the 'U' case, but for contact constraints only

  * t0 -- time interval start

  * t1 -- time interval end

  * skip -- number of steps to skip between two time instants

  * progress -- 'ON' or 'OFF'; print out a percentage based progress bar (default: 'OFF'); useful for large output files and slow hard disks

XDMF_EXPORT
-----------

Export results in XDMF format. In 'WRITE' mode only the geometry at time :math:`t=0` is saved,
while arguments *time* and *attributes* are ignored. See also :ref:`XDMF export manual <solfec-xdmf>`.

.. topic:: XDMF_EXPORT (solfec, time, path | subset, attributes)
	
 * solfec -- SOLFEC object;

 * time -- time instant, e.g. t0, a collection of time instants,
   e.g. [t0, t1, t2, ..., tN], or a time interval, e.g. (t0, t1);

 * path -- output path to the directory that will contain the XDMF markup file(s) and a HDF5 data file;
   e.g. '/tmp/sim0' will possibly result in a /tmp/sim0/sim0_grids.xmf, /tmp/sim0/sim0_constraints.xmf,
   /tmp/sim0/sim0_spheres.xmf markup files and a /tmp/sim0/sim0.h5 data file output;

 * subset -- specification of a subset of exported bodies; a string can be used to define a POSIX regular
   expression [1]_ that will be matched against body labels; a list of body objects or integer body identifiers
   can be used [body1, body2, id3, id4, body5, ...] mixed up in an arbitrary manner; or a tuple specifying
   extents of a bounding box can be used (xlow, ylow, zlow, xhigh, yhigh, zhigh), which the bounding boxes of
   exported bodies overlapped at time t=0; also a list of an arbitrary combination of those can be used,
   e.g. ['BOD*A', 123, body1, body2, 256, (0, 0, 0, 1, 1, 1), 'KEY??7', (3, 3, 3, 4, 4, 4)] defines two labels,
   two integer body ids, two body objects, and two bounding boxes, that together define a subset of bodies
   that will be used during export;

 * attributes -- list of export attributes; default ['DISP', 'VELO', 'REAC', 'GAP'];
   available attributes are 'DISP' (body displacement), 'VELO' (body velocity), 'STRESS' (body stress),
   'REAC' (constraint reactions), 'RELV' (relative constraint velocities), 'GAP' (contact gaps);
   a non-optional scalar attribute 'BID' (body identifier) is always included with exported geometry;

.. [1] `POSIX regular expressions <https://en.wikibooks.org/wiki/Regular_Expressions/POSIX_Basic_Regular_Expressions>`_
