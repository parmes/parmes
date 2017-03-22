.. _solfec-user-simulation:

Simulation
==========

Routines listed in this section control the solution process.
A simulation can be run be invoking the RUN command, documented below.

.. _solfec-user-run:

.. topic:: RUN (solfec, solver, duration)

  This routine runs a simulation.

  * solfec -- SOLFEC object

  * solver -- constraint solver object (e.g. GAUSS_SEIDEL_SOLVER, NEWTON_SOLVER, PENALTY_SOLVER)

  * duration -- duration of analysis. *Note:* this parameter is ignored when an analysis is run in the viewer mode (with --v switch).

Initialization
--------------

Prior to running, a simulation may also require initialization.
Below we list subroutines providing per--body or per--simulation initialization functionality.

.. topic:: INITIAL_VELOCITY (body, linear, angular)

  This routine applies initial (at time zero) linear and angular (in the sense of rigid motion) velocity to a body.

  * body -- BODY object

  * linear -- linear velocity :math:`(v_{x},v_{y},v_{z})`

  * angular -- angular velocity :math:`(\omega_{x},\omega_{y},\omega_{z} )`

.. topic:: INITIALIZE_STATE (solfec, path, time)

  This routine initializes the state of a Solfec object with the state red from an output
  directory at a given time. It is ignored in the 'READ' mode. *Note*: constraint reactions
  are initialized with zeros and recalculated at the next time step.

  * solfec -- Solfec object in the 'WRITE' mode

  * path -- path to the output directory containing matching analysis results (note: this cannot be the same output directory as for the solfec object)

  * time -- time at which the state should be red from the output files

.. topic:: RIGID_TO_FEM (path, time, solfec)

  This routine initializes the state of FEM bodies within the Solfec object with the state of rigid bodies
  red from an output directory at a given time. It is ignored in the 'READ' mode. *Note:* rigid displacements
  are applied to the finite element bodies; this implies that when you add boundary conditions to finite element
  bodies, after their state was updated with RIGID_TO_FEM, you still use the original referential point coordinates
  as the locations of the constraints (e.g. when using SET_DISPLACEMENT or SET_VELOCITY).

  * path -- path to the output directory containing matching rigid body analysis results;
    the number of rigid bodies in this analysis must match the number of FEM bodies in the Solfec object;
    the identifiers of rigid bodies must match the identifiers of FEM bodies;
    this is guaranteed if the input files for both analyses differ only by the prescribed body kinds;

  * time -- time at which the state should be red from the output files

  * solfec -- Solfec object in the 'WRITE' mode

Runtime utilities
-----------------

Routines below help control runtime behaviour.

.. _solfec-user-output:

.. topic:: OUTPUT (solfec, interval | compression)

  This routine specifies the frequency of writing to the output file.

  * solfec -- SOLFEC object

  * interval -- length of the time interval elapsing before consecutive output file writes

  * compression -- output compression mode: 'OFF' (default) or 'ON'.
    Compressed output files are smaller, although they might not be portable between hardware platforms.

.. topic:: EXTENTS (solfec, extents)

  This routine bounds the simulation space. Bodies falling outside of the extents are deleted from the simulation.

  * solfec -- SOLFEC object

  * extents -- (xmin, ymin, zmin, xmax, ymax, zmax) tuple

.. _solfec-user-callback:

.. topic:: CALLBACK (solfec, interval, data, callback)

  This routine defines a callback function, invoked during a run of Solfec every interval of time.
  A callback routine can interrupt the course of RUN command by returning 0.

  * solfec -- SOLFEC object

  * interval -- length of the time interval elapsing before consecutive callback calls

  * data -- data passed to the callback function

  * callback -- callback function of form: value = callback (data), where for the returned value equal zero Solfec run is stopped

.. topic:: WARNINGS (state)

  This routine disables or enables Solfec warnings. It is a good practice to have the
  warnings enabled and only switch them off after making sure, that they can be ignored.

  * state -- 'ON' or 'OFF' (default: 'ON')

Contact handling
----------------

Routines listed below affect contact detection and contact handling.

.. _geometric_epsilon:

.. topic:: GEOMETRIC_EPSILON (epsilon)

  This routine sets a numerical tolerance for geometric tests performed within Solfec.
  The tolerance is a characteristic distance between two distinct points below which they can be regarded as one.
  See also :ref:`this comment <geometric_epsilon_section>` in the :ref:`Theory Manual <solfec-theory>`.

  * epsilon -- geometrical tolerance (default: 1E-6)

.. topic:: UNPHYSICAL_PENETRATION (solfec, depth)

  This routine sets a depth of allowed an unphysical interpenetration.
  Once it is exceeded, the simulation is stopped and a suitable error message printed out.

  * solfec -- SOLFEC object

  * depth -- interpenetration depth bound (default: :math:`\infty`)

.. topic:: CONTACT_EXCLUDE_BODIES (body1, body2)

  This routine disables contact detection for a specific pair of bodies. By default contact detection
  is enabled for all possible body pairs. *Note:* must be invoked on all processors during a parallel
  run (do not use from within a callback).

  * body1 -- first BODY object

  * body2 -- second BODY object

.. topic:: CONTACT_EXCLUDE_SURFACES (solfec, surf1, surf2)

  This routine disables contact detection for a specific pair of surfaces. By default contact detection
  is enabled for all possible surface pairs. *Note:* must be invoked on all processors during a parallel
  run (do not use from within a callback).

  * solfec -- SOLFEC object

  * surf1 -- first BODY object

  * surf2 -- second BODY object

.. _contact_sparsify:

.. topic:: CONTACT_SPARSIFY (solfec, threshold | minarea, mindist)

  This routine modifies contact filtering (sparsification) behaviour. Generally speaking, some contact points
  are filtered out in order to avoid unnecessary dense contact point clusters. If a pair of bodies is connected
  by two or more contact points, one of the points generated by topologically adjacent entities (elements,
  convices) will be removed (sparsified) if the ratio of contact areas of is smaller than the prescribed threshold.
  See also :ref:`contact sparsification <contact_sparsification>`.

  * solfec -- SOLFEC object

  * threshold -- sparsification threshold (default: 0.01) from within the interval [0, 1]. Zero corresponds to the lack of sparsification.

  * minarea -- minimal contact area (default: 0.0). Contact points with area smaller then minarea are dropped.

  * mindist -- minimal distance between distinct contact points (default: GEOMETRIC_EPSILON).

Parallel runtime
----------------

Routines listed below are related to prallel runtime and performance.

.. topic:: IMBALANCE_TOLERANCE (solfec, tolerance | weightfactor, updatefreq)

  This routine sets the imbalance tolerance for parallel balancing of Solfec data. A ratio of maximal to minimal
  per processor count of objects used. Hence, 1.0 indicates perfect balance, while any ratio > 1.0 indicates an
  imbalance. Initially imbalance tolerance is set to 1.1. This routine is ignored during sequential runs.

  * solfec -- SOLFEC object

  * tolerance -- data imbalance tolerance (default: 1.1)

  • weightfactor -- a local dynamics weight factor between 0.0 and 1.0 (default: 1.0). Computational load of
    local dynamics assembling is best balanced when weightfactor equals 1.0. This however can sometimes result
    in a poor load balance for contact detection or time integration. Making it smaller than 1.0 can improve
    the overall balance in such cases.
    *Note:* This parameter is ignored if DYNLB load balancer is used; in this case, on a per-rank basis, body
    centroids are used to guide load balancing if there is more bodies than constrains on a given rank at
    given time; otherwise contact/constraint points are used to guide load balancing.

  * updatefreq -- geometrical domain partitioning is updated every updatefreq time steps (default: 10)

.. topic:: num = RANK ()

  This routine returns the rank of the CPU that runs the current copy of Solfec.

  * num -- the CPU rank

.. topic:: BARRIER ()

  This routine sets up a parallel barrier in the MPI mode (all processes need to
  meet at it before they can continue). It is ignored in the serial mode.

.. topic:: num = NCPU (solfec)

  This routine returns the number CPUs used in the analysis.

  * num -- the number of CPUs

  * solfec -- SOLFEC object

.. topic:: ret = HERE (solfec, object)

  This routine tests whether an object is located on the current processor. During parallel runs
  objects migrate between processors. When calling a function (or a member) for an object not present
  on the current processor, the call will usually return None or be ignored. Hence, it is convenient
  to check whether an object resides on the current processor.

  * ret -- True or False

  * solfec -- SOLFEC object

  * object -- BODY or CONSTRAINT object
