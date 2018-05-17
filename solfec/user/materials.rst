.. _solfec-user-materials:

Materials
=========

Routines and objects described below allow to define bulk and surface materials.

FIELD
-----

An object of type FIELD represents a three--dimensional, scalar, time dependent field.

.. topic:: obj = FIELD (solfec, field_callback | label, data)

  This routine creates a FIELD object.

  * obj -- created FIELD object

  * solfec -- obj is created for this SOLFEC object

  * field_callback -- the Python function defining the scalar field:

    **value = field_callback (data, x, y, z, t)**

    where *data* is the optional user data passed to FIELD routine (if data is a tuple it will expand
    the list of parameters to the callback), *x, y, z* are the point coordinates, and *t* is time.
    The function should return a numeric value of the scalar field at given point and instant of time.

  * label -- label string (default: 'FIELD_i', where i is incremented for each call)

  * data -- callback routine user data

Some parameters can also be accessed as members of a FIELD object, cf. :numref:`field-params`.

.. _field-params:

.. table:: FIELD object parameters.

  +---------------------------------------------------------------------------------------------------------+
  | **Read only members:**                                                                                  |
  +---------------------------------------------------------------------------------------------------------+
  | *obj.label*                                                                                             |
  +---------------------------------------------------------------------------------------------------------+

.. _solfec-command-BULK_MATERIAL:

BULK_MATERIAL
-------------

An object of type BULK_MATERIAL represents material properties of a volume.

.. topic:: obj = BULK_MATERIAL (solfec| model, label, young, poisson, density, tensile, fields, fracene)

  This routine creates a BULK_MATERIAL object.

  * obj -- created BULK_MATERIAL object

  * solfec -- obj is created for this SOLFEC object

  * model -- material model name (default: 'KIRCHHOFF'), see :numref:`bulk-materials`

  * label -- label string (default: 'BULK_MATERIAL_i', where i is incremented for each call)

  * young -- Young's modulus (default: 1E9)

  * poisson -- Poisson's coefficient (default: 0.25)

  * density -- material density (default: 1E3)

  * tensile -- tensile strength for fracture check (default: :math:`\infty`)

  * fields -- list [field1, field1, ..., fieldN] of FIELD objects (or FIELD object labels) needed by the material model

  * fracene -- fracture energy threshold (default: :math:`\infty`)

Some parameters can also be accessed as members of a BULK_MATERIAL object, cf. :numref:`bulk-params`.

.. _bulk-params:

.. table:: BULK_MATERIAL object parameters.

  +---------------------------------------------------------------------------------------------------------+
  | **Read only members:**                                                                                  |
  +---------------------------------------------------------------------------------------------------------+
  | *obj.model, obj.label*                                                                                  |
  +---------------------------------------------------------------------------------------------------------+
  | **Read/write members:**                                                                                 |
  +---------------------------------------------------------------------------------------------------------+
  | *obj.young, obj.poisson, obj.density*                                                                   |
  +---------------------------------------------------------------------------------------------------------+

|

.. _bulk-materials:

.. table:: Bulk material models.

  +--------------------------------+------------------------------------------------------------------------+
  | Model name                     | Employs variables                                                      |
  +--------------------------------+------------------------------------------------------------------------+
  | 'KIRCHHOFF'                    | young, poisson, density                                                |
  +--------------------------------+------------------------------------------------------------------------+

APPLY_BULKMAT
-------------

This routine applies bulk material to a subset of geometric objects with the given volume identifier.

.. topic:: APPLY_BULKMAT (solfec, body, volid, material)

  * solfec -- SOLFEC object

  * body -- BODY object

  * volid -- volume identifier

  * material -- MATERIAL object or material label

.. _solfec-command-SURFACE_MATERIAL:

SURFACE_MATERIAL
----------------

An object of type SURFACE_MATERIAL represents material properties on the interface between two surfaces.
Surfaces identifiers are included in definitions of all geometric objects.

.. topic:: obj = SURFACE_MATERIAL (solfec | surf1, surf2, model, label, friction, cohesion, restitution, spring, dashpot, hpow)

  This routine creates a SURFACE_MATERIAL object.

  * obj -- created SURFACE_MATERIAL object

  * solfec -- obj is created for this SOLFEC object

  * surf1 -- first surface identifier

  * surf2 -- second surface identifier; If only surf1 is specified,
    the surface material is used for all contacts with the specified surface;
    If neither surf1 or surf2 are specified, the surface material is used for
    any contacts where a more-specific pairing cannot be found.

  * model -- material model name (default: 'SIGNORINI_COULOMB'), see :numref:`surf-materials`

  * label -- label string (default: 'SURFACE_MATERIAL_i', where i is incremented for each call)

  * friction -- friction coefficient (default: 0.0)

  * cohesion -- cohesion per unit area (default: 0.0)

  * restitution -- velocity restitution (default: 0.0)

  * spring -- spring stiffness (default: 0.0)

  * dashpot -- dashpot stiffness (default: 0.0); any negative value indicates critical damping

  * hpow -- Hertz's law power (default: 1.0)

Some parameters can also be accessed as members of a SURFACE_MATERIAL object, cf. :numref:`surf-params`.

.. _surf-params:

.. table:: SURFACE_MATERIAL object parameters.

  +---------------------------------------------------------------------------------------------------------+
  | **Read only members:**                                                                                  |
  +---------------------------------------------------------------------------------------------------------+
  | *obj.surf1, obj.surf2, obj.label*                                                                       |
  +---------------------------------------------------------------------------------------------------------+
  | **Read/write members:**                                                                                 |
  +---------------------------------------------------------------------------------------------------------+
  | *obj.model,obj.friction, obj.cohesion, obj.restitution, obj.spring, obj.dashpot, obj.hpow*              |
  +---------------------------------------------------------------------------------------------------------+

|

.. _surf-materials:

.. table:: Surface material models.

  +--------------------------------+------------------------------------------------------------------------+
  | Model name                     | Employs variables                                                      |
  +--------------------------------+------------------------------------------------------------------------+
  | 'SIGNORINI_COULOMB'            | friction, cohesion, restitution                                        |
  +--------------------------------+------------------------------------------------------------------------+
  | 'SPRING_DASHPOT'               | spring, dashpot, friction, cohesion, hpow                              |
  +--------------------------------+------------------------------------------------------------------------+
