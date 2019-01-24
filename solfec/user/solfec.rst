.. _solfec-user-solfec:

SOLFEC object
=============

An object of type SOLFEC represents the Solfec algorithm. One can use several SOLFEC objects to run several analyses from a single input file.

.. topic:: obj = SOLFEC (analysis, step, output)

  This routine creates a SOLFEC object.

  * obj -- created SOLFEC object

  * analysis -- 'DYNAMIC' or 'QUASI_STATIC' analysis kind

  * step -- initially assumed time step, regarded as an upper bound

  * output -- defines the output directory path (Important note: if this directory exists
    and contains valid output data SOLFEC is created in 'READ' mode,
    otherwise SOLFEC is created in 'WRITE' mode)

Some parameters can be accessed as members of a SOLFEC object, cf. :numref:`solfec-params`.

.. _solfec-params:

.. table:: SOLFEC object parameters.

  +---------------------------------------------------------------------------------------------------------+
  | **Read only members:**                                                                                  |
  +---------------------------------------------------------------------------------------------------------+
  | *obj.analysis*                                                                                          |
  +---------------------------------------------------------------------------------------------------------+
  | **obj.time** -- current time                                                                            |
  +---------------------------------------------------------------------------------------------------------+
  | **obj.mode** -- either 'READ' or 'WRITE' as described above                                             |
  +---------------------------------------------------------------------------------------------------------+
  | **obj.constraints** -- list of constraints (cf. :ref:`Constraints <solfec-user-constraints>`)           |
  +---------------------------------------------------------------------------------------------------------+
  | **obj.ncon** -- number of constraints                                                                   |
  +---------------------------------------------------------------------------------------------------------+
  | **obj.bodies** -- list of bodies (cf. :ref:`BODY object <solfec-user-body>`)                            |
  +---------------------------------------------------------------------------------------------------------+
  | **obj.nbod** -- number of bodies                                                                        |
  +---------------------------------------------------------------------------------------------------------+
  | **obj.outpath** -- output path, including the sub-directory if the “-s” command line argument           |
  | has been passed                                                                                         |
  +---------------------------------------------------------------------------------------------------------+
  | **Read/write members:**                                                                                 |
  +---------------------------------------------------------------------------------------------------------+
  | *obj.step*                                                                                              |
  +---------------------------------------------------------------------------------------------------------+
  | **obj.verbose** -- 'ON' or 'OFF' enabling or disabling writing to standard output (default: 'ON');      |
  | '%' can also be used to enable plain percentage printout per individual :ref:`RUN <solfec-command-RUN>`;|
  | '%\n' can be used for the same purpose with a newline inserted after finished calculations              |
  +---------------------------------------------------------------------------------------------------------+
  | **obj.cleanup** -- either 'ON' or 'OFF' enabling or disabling removal of the output directory in 'WRITE'|
  | mode if none results were saved (default: 'OFF' in which case the initial geometry is saved as a        |
  | sole result); *Note:* POSIX=yes must be set in Config.mak for the 'ON' functionality to work;           |
  +---------------------------------------------------------------------------------------------------------+
