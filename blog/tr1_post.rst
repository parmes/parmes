.. post:: May 20, 2017
   :tags: reports
   :author: Tomek

.. _tr1-post:

TR1: Co-rotated and reduced order time integrators
==================================================

:ref:`Technical Report 1 <tr1>` describes a linearly implicit time integration method
combined with a family of finite element formulations: (...)

* Total Lagrangian (TL)
* body co--rotational full mesh (BC)
* body co--rotational reduced order (BC--RO)
* body co--rotational modal (BC--MODAL)

as they are implemented in :ref:`solfec-1-index`. These formulations allow to vary the amount of deformation 
expressed by a finite element mesh and facilitate saving computational time and storage. They may be helpful in the context
of multibody modeling.

The methods described in :ref:`TR1 <tr1>` can be accessed by creating a :ref:`BODY object <solfec-user-body>` as follows

::

  bdTL = BODY (solfec, 'FINITE_ELEMENT', shape, material, form = 'TL')
  bdTL.scheme = 'DEF_LIM'

  bdBC = BODY (solfec, 'FINITE_ELEMENT', shape, material, form = 'BC')
  bdBC.scheme = 'DEF_LIM'

  bdRO = BODY (solfec, 'FINITE_ELEMENT', shape, material,
               form = 'BC-RO', base = pod_base)

  dbMD = BODY (solfec, 'FINITE_ELEMENT', shape, material,
               form = 'BC-MODAL', base = modal_base)

In case of the 'BC--RO' and 'BC--MODAL' the linearly implicit integrator is default.
For 'TL' and 'BC' the default time integration scheme is 'DEF_EXP' (:numref:`solfec-body-scheme`);
we change it to 'DEF_LIM' after body creation.

The *base* format is a tuple of two lists

::

  base = ([eval1, eval2, ..., evaln],
          [evec11, evec12, ..., evec1m,
	   evec21, evec22, ..., evec2m,
	   ..., evecnm])

where we assumed *n* base vectors of size *m*. The first list stores eigenvalues and the second list stores
eigenvectors. :ref:`COROTATED_DISPLACEMENTS <solfec-command-COROTATED_DISPLACEMENTS>` and
:ref:`RIGID_DISPLACEMENTS <solfec-command-RIGID_DISPLACEMENTS>` commands can be used together to sample
displacements and generate a reduced base using `Python's modred package <https://pypi.python.org/pypi/modred>`_.
:ref:`MODAL_ANALYSIS <solfec-command-MODAL_ANALYSIS>` command can be used to generate a modal base.

Input decks for the rotating bar, pipe impact, and array excitation examples from :ref:`TR1 <tr1>`
can be respectively found in

* `solfec/examples/reduced--ordero0 <https://github.com/tkoziara/solfec/tree/master/examples/reduced-order0>`_
* `solfec/example/reduced--order1 <https://github.com/tkoziara/solfec/tree/master/examples/reduced-order1>`_
* `solfec/example/81array <https://github.com/tkoziara/solfec/tree/master/examples/81array>`_

directories. See also :ref:`the online version of these examples <solfec-examples-reduced_order>`.
