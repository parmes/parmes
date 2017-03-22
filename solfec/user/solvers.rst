.. _solfec-user-solvers:

Solvers
=======

Solver objects represent a constraint solution scheme applied at every time step
of a simulation in order to resolve the equality and inequality constraints. User defined
constraints and contact constraints are handled together as one nonlinear root finding problem.

.. _gauss-seidel:

Gauss--Seidel
-------------

An object of type GAUSS_SEIDEL_SOLVER represents a nonlinear block Gauss--Seidel solver,
employed for the calculation of constraint reactions.

.. topic:: obj = GAUSS_SEIDEL_SOLVER (epsilon, maxiter | meritval, failure, diagepsilon, diagmaxiter, diagsolver, data, callback)

  This routine creates a GAUSS_SEIDEL_SOLVER object.

  * obj -- created GAUSS_SEIDEL_SOLVER object

  * epsilon -- relative accuracy of constraint reactions sufficient for termination

  * maxiter -- maximal number of iterations before termination

  * meritval -- constraints satisfaction merit function value sufficient for termination (default: 1, unused)

  * failure -- failure (lack of convergence) action (default: 'CONTINUE'). Available failure actions are:
    'CONTINUE' (simulation is continued), 'EXIT' (simulation is stopped and Solfec exits),
    'CALLBACK' (a callback function is called if it was set or otherwise the 'EXIT' scenario is executed).
    In all cases *obj.error* variable is set up, cf. :numref:`gauss-seidel-error`.

  * diagepsilon -- diagonal block solver relative accuracy of constraint reactions (default: min (epsilon, meritval, 1E-4) / 100)

  * diagmaxiter -- diagonal block solver maximal number of iterations (default: max (100, maxiter / 100))

  * diagsolver -- diagonal block solver kind (default: 'SEMISMOOTH_NEWTON'). Available diagonal solvers are:
    'SEMISMOOTH_NEWTON', 'PROJECTED_GRADIENT', 'DE_SAXCE_FENG', 'PROJECTED_NEWTON'.

  * data -- data passed to the failure callback function (if this is a tuple it will
    accordingly expand the parameter list of the callback routine)

  * callback -- failure callback function of form: **value = callback (obj, data)**,
    where for the returned value equal zero Solfec run is stopped

Some parameters can also be accessed as members of a GAUSS_SEIDEL_SOLVER object, cf. :numref:`gauss-seidel-params`.

.. _gauss-seidel-params:

.. table:: GAUSS_SEIDEL_SOLVER object parameters.

  +---------------------------------------------------------------------------------------------------------+
  | **Read only members:**                                                                                  |
  +---------------------------------------------------------------------------------------------------------+
  | *obj.failure*                                                                                           |
  +---------------------------------------------------------------------------------------------------------+
  | **obj.error** -- current error code, cf. :numref:`gauss-seidel-error`                                   |
  +---------------------------------------------------------------------------------------------------------+
  | **obj.iters** -- number of iterations during a last run of solver                                       |
  +---------------------------------------------------------------------------------------------------------+
  | **obj.rerhist** -- a list of relative error values for each iteration of the last run                   |
  +---------------------------------------------------------------------------------------------------------+
  | **obj.merhist** -- a list of merit function values for each iteration of the last run                   |
  +---------------------------------------------------------------------------------------------------------+
  | **Read/write members:**                                                                                 |
  +---------------------------------------------------------------------------------------------------------+
  | *obj.epsilon, obj.maxiter, obj.meritval, obj.diagepsilon, obj.diagmaxiter, obj.diagsolver*              |
  +---------------------------------------------------------------------------------------------------------+
  | **obj.reverse** -- 'ON' or 'OFF' flag switching iteration reversion modes (whether to alternate         |
  | backward and forward or not, default is 'OFF')                                                          |
  +---------------------------------------------------------------------------------------------------------+
  | **obj.variant** -- variant of parallel Gauss--Seidel update (default: 'FULL'),                          |
  | cf. :numref:`gauss-seidel-variant`. Ignored in sequential mode.                                         |
  +---------------------------------------------------------------------------------------------------------+
  | **obj.innerloops** -- number of inner Gauss--Seidel loops per one global step during a parallel run     |
  | (default: 1). Ignored in sequential mode.                                                               |
  +---------------------------------------------------------------------------------------------------------+

|

.. _gauss-seidel-error:

.. table:: Error codes of GAUSS_SEIDEL_SOLVER object.

  +--------------------------+------------------------------------------------------------------------------+
  | 'OK'	             | No error has occurred                                                        |
  +--------------------------+------------------------------------------------------------------------------+
  | 'DIVERGED'	             | Global iteration loop divergence                                             |
  +--------------------------+------------------------------------------------------------------------------+
  | 'DIAGONAL_DIVERGED'	     | Diagonal solver iteration loop divergence                                    |
  +--------------------------+------------------------------------------------------------------------------+
  | 'DIAGONAL_FAILED'	     | Failure of a diagonal solver (e.g. singularity)                              |
  +--------------------------+------------------------------------------------------------------------------+

|

.. _gauss-seidel-variant:

.. table:: Variants of parallel Gauss--Seidel update.

  +--------------------------+------------------------------------------------------------------------------+
  | 'FULL'	             | Full Gauss--Seidel update as in sequential case. Although the slowest, it    |
  |                          | works in all cases. It should be noted, that all of the below variants will  |
  |                          | usually fail for all--rigid--body models.                                    |
  +--------------------------+------------------------------------------------------------------------------+
  | 'MIDDLE_JACOBI'	     | Jacobi update for off--processor data of :math:`\mathbf{W}` matrix blocks    |
  |                          | communicating with processors of higher and lower colors. Of use for         |
  |                          | deformable kinematics, where off--diagonal interactions are weaker. The      |
  |                          | Gauss--Seidel runtime should be halved for large numbers of processors.      |
  +--------------------------+------------------------------------------------------------------------------+
  | 'BOUNDARY_JACOBI'	     | Use Jacobi update for all off--processor data. This approach will fail in    |
  |                          | most cases. It servers as illustration.                                      |
  +--------------------------+------------------------------------------------------------------------------+

.. _projected-newton:

Projected Newton
----------------

Object of type NEWTON_SOLVER represents a projected quasi--Newton constraints solver.
If local dynamics is enabled (locdyn = 'ON') and iterations fail to converge,
the Gauss--Seidel solver will be invoked, starting from the previous time step solution.
*WARNING:* NEWTON_SOLVER may not work well for friction > 1.0.

.. topic:: obj = NEWTON_SOLVER (| meritval, maxiter, locdyn, linver, linmaxiter, maxmatvec, epsilon, delta, theta, omega, gsflag)

  This routine creates a NEWTON_SOLVER object.

  * obj -- created NEWTON_SOLVER object

  * meritval -- value of merit function sufficient for termination (default: 1E-8)

  * maxiter -- iterations bound (default: 1000)

  * locdyn -- 'ON' or 'OFF' deciding whether to fully assemble local dynamics (default: 'ON');
    using the 'OFF' value may be more efficient for implicitly integrated FEM bodies with large meshes

  * linver -- 'GMRES' or 'DIAG' being the linear solver kind (default: 'GMRES')

  * limaxiter -- GMRES iterations bound (ignored for linver = 'DIAG', default: 10)

  * maxmatvec -- GMRES matrix-vector products bound (default: linmaxiter * maxiter)

  * epsilon -- relative GMRES accuracy (default: 0.25)

  * delta -- non--negative amount of diagonal regularization (used only for linver = 'GMRES', default: 0.0);
    this parameter has a decisive influence on global convergence; for well--conditioned problems it can be
    very small or zero; for ill--conditioned problems one should pick a value that delivers an overall best
    convergence behavior; large values will slow down convergence, but stabilize it; small values may destabilize
    convergence for ill--conditioned problems; delta (typically :math:`\ll` 1) should be tuned together with epsilon
    and linmaxiter, so that the linear sub-problems are solved only roughly; since rigorous analysis is still missing
    for these parameters, please experiment before settling on specific values for a specific problem;

  * theta -- relaxation parameter greater than 0 and not greater than 1 (used only for linver = 'DIAG',
    default: 0.25); smaller initial theta may improve overall convergence behavior

  * omega -- positive equation smoothing omega (default: \mbox{\textbf{meritval}}\cdot0.01)

  * gsflag -- 'ON' or 'OFF' deciding whether to us Gauss-Seidel iterations in case of failure (default: 'ON')

Some parameters can also be accessed as members of a NEWTON_SOLVER object, cf. :numref:`newton-params`.

.. _newton-params:

.. table:: NEWTON_SOLVER object parameters.

  +---------------------------------------------------------------------------------------------------------+
  | **Read only members:**                                                                                  |
  +---------------------------------------------------------------------------------------------------------+
  | *obj.failure*                                                                                           |
  +---------------------------------------------------------------------------------------------------------+
  | **obj.iters** -- number of iterations during a last run of solver                                       |
  +---------------------------------------------------------------------------------------------------------+
  | **obj.merhist** -- a list of merit function values for each iteration of the last run                   |
  +---------------------------------------------------------------------------------------------------------+
  | **obj.mvhist** -- a list of matrix--vector products for each iteration of the last run                  |
  +---------------------------------------------------------------------------------------------------------+
  | **Read/write members:**                                                                                 |
  +---------------------------------------------------------------------------------------------------------+
  | *obj.meritval, obj.maxiter, obj.locdyn, obj.linver, obj.linmaxiter, obj.maxmatvec, obj.epsilon,*        |
  | *obj.delta, obj.theta, obj.omega, obj.gsflag*                                                           |
  +---------------------------------------------------------------------------------------------------------+

Penalty based
-------------

An object of type PENALTY_SOLVER represents a penalty based constraint solver.
When in use, all 'SIGNORONI_COULOMB' type contact interfaces are regarded as 'SPRING_DASHPOT' ones.
One should then remember about specifying the spring value for those constraints.

.. topic:: obj = PENALTY_SOLVER ( | variant)

  This routine creates a PENALTY_SOLVER object.

  * obj -- created PENALTY_SOLVER object

  * variant -- 'IMPLICIT' or 'EXPLICIT' normal force computation variant (default: 'IMPLICIT')

Siconos solver
--------------

Object of type SICONOS_SOLVER represents an interface to `Siconos <http://siconos.gforge.inria.fr>`_ contact solvers library.
Currently only the the nonlinear Gauss--Seidel solver is enabled, making the SICONOS_SOLVER equivalent to the GAUSS_SEIDEL_SOLVER.
*WARNING1:* only contact constraints are supported at this stage. *WARNING2:* velocity restitution is ignored at the moment.
*WARNING3:* only the serial version is available. *WARNING4:* Solfec needs to be compiled with Sicons support for this solver to work.

.. topic:: obj = SICONOS_SOLVER (| epsilon, maxiter, verbose)

  This routine creates a SICONOS_SOLVER object.

  * obj -- created SICONOS_SOLVER object

  * epsilon -- relative accuracy of constraint reactions sufficient for termination (default: 1E-4)

  * maxiter -- iterations bound (default: 1000)

  * verbose -- verbosity flag: 'ON' or 'OFF' (default: 'OFF')

Some parameters can also be accessed as members of a SICONOS_SOLVER object, cf. :numref:`siconos-params`.

.. _siconos-params:

.. table:: SICONOS_SOLVER object parameters.

  +---------------------------------------------------------------------------------------------------------+
  | **Read/write members:**                                                                                 |
  +---------------------------------------------------------------------------------------------------------+
  | *obj.epsilon, obj.maxiter*                                                                              |
  +---------------------------------------------------------------------------------------------------------+

.. _hybrid-solver:

Hybrid solver
-------------

.. role:: red

Hybrid solver allows to combine smooth rigid body nonlinear spring based :ref:`PARMEC <parmec-index>` models with non--smooth SOLFEC models.
The solver is supported both in the serial and MPI version of Solfec. The Parmec library is shared memory parallel and in the MPI mode this
part of modeling is executed on MPI rank 0 process, employing maximum available shared memory parallelism.

.. topic:: obj = HYBRID_SOLVER (parmec_file, parmec_step, parmec2solfec, solfec_solver) :red:`(Under development)`

  * obj -- created HYBRID_SOLVER object

  * parmec_step -- an upper bound of the PARMEC time step

  * parmec2solfec -- Python dictionary based mapping of PARMEC particle numbers to SOLFEC body identifiers

  * solfec_solver -- SOLFEC constraint solver (e.g. NEWTON_SOLVER) 

Some parameters can also be accessed as members of a HYBRID_SOLVER object, cf. :numref:`hybrid-params`.

.. _hybrid-params:

.. table:: HYBRID_SOLVER object parameters.

  +---------------------------------------------------------------------------------------------------------+
  | **Read/write members:**                                                                                 |
  +---------------------------------------------------------------------------------------------------------+
  | *obj.parmec_interval* -- PARMEC output interval specification (as in :ref:`parmec’s DEM command         |
  | <parmec-command-DEM>`); when not specified PARMEC will not write output files; the read value is        |
  | [(d,d), (O,O), (i, i)], where the first tuple contains floating point intervals, the second tuple       |
  | contains Python callbacks, the third tuple contains TSERIES numbers                                     |
  +---------------------------------------------------------------------------------------------------------+
  | *obj.parmec_prefix* -- PARMEC output file name prefix (as in :ref:`parmec’s DEM command                 |
  | <parmec-command-DEM>`)                                                                                  |
  +---------------------------------------------------------------------------------------------------------+


