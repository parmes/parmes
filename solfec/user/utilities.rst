.. _solfec-user-utilities:

Utilities
=========

Various utility routines are listed below.

VIEWER
------

This routine tests whether the viewer is enabled.

.. topic:: obj = VIEWER ()

  * obj -- True or False depending on whether the viewer (--v command line option) was enabled


SUBDIR
------

This routine returns the optional output subdirectory.

.. topic:: obj = SUBDIR ()

  * obj -- None object or subdirectory string depending on whether the --s command line option was used

BODY_CHARS
----------

This routine overwrites referential characteristics of a body.

.. topic:: BODY_CHARS (body, mass, volume, center, tensor)

  * body -- BODY object

  * mass -- body mass

  * volume -- body volume

  * center -- (x, y, z) mass center

  * tensor -- :math:`\left(t_{11},t_{21},\,...\,,t_{33}\right)` column-wise inertia tensor for a rigid body or Euler tensor otherwise

DELETE
------

This routine deletes a BODY object or a CONSTRAINT object from a SOLFEC object.

.. topic:: DELETE (solfec, object)

  * solfec -- SOLFEC object

  * object (emptied) -- BODY or CONSTRAINT object

SCALE
-----

This routine scales a geometrical object or a collection of such objects.

.. topic:: obj = SCALE (shape, coefs)

  * obj -- when shape is not (x, y, z) tuple: same as shape, returned for convenience.
    Otherwise the (x :math:`\cdot` coefs[0], y :math:`\cdot` coefs[1], z :math:`\cdot` coefs[2]) tuple.

  * shape -- object, collection of objects, or a list [a, b, c, ...] of objects of type CONVEX, MESH,
    SPHERE, ELLIP. Alternately this can be a single (x, y, z) tuple, but then one must use 
    point = SCALE (point, coefs) in order to modify the point (Python tuples are immutable --
    they cannot be modified “in place” after creation).

  * coefs -- (cx, cy, cz) tuple of scaling factors along each axis

TRANSLATE
---------

This routine translates a geometrical object or a collection of such objects.

.. topic:: obj = TRANSLATE (shape, vector)

  * obj -- when shape is not (x, y, z) tuple: same as shape, returned for convenience.
    Otherwise the (x+vector[0], y+vector[1], z+vector[2]) tuple.

  * shape -- object, collection of objects, or a list [a, b, c, ...] of objects of type CONVEX, MESH,
    SPHERE, ELLIP. Alternately this can be a single (x, y, z) tuple, but then one must use
    point = TRANSLATE (point, vector) in order to modify the point (Python tuples are immutable --
    they cannot be modified “in place” after creation).

  * vector -- (vx, vy, vz) tuple defining the translation

ROTATE
------

This routine rotates a geometrical object or a collection of such objects.

.. topic:: obj = ROTATE (shape, point, vector, angle)

  * obj -- when shape is not (x, y, z) tuple: same as shape, returned for convenience.
    Otherwise the rotated (x1, y1, z1) image of (x, y, z).

  * shape -- object, collection of objects, or a list [a, b, c, ...] of objects of type CONVEX, MESH,
    SPHERE, ELLIP. Alternately this can be a single (x, y, z) tuple, but then one must use
    point1 = ROTATE (point1, point2, vector, angle) in order to modify point1 (Python tuples are immutable --
    they cannot be modified “in place” after creation).

  * point -- (px, py, pz) tuple defining a point passed by the rotation axis

  * vector -- (vx, vy, vz) tuple defining a direction of the rotation axis

  * angle -- rotation angle in degrees

SPLIT
-----

This routine splits a geometrical object (or a collection of objects) by a plane passing by a point.
Depending on the topological properties of the body shape and plane position this may or may not
result in splitting of the body in two parts.

.. role:: red

.. topic:: (one, two) = SPLIT (shape, point, normal | surfid, topoadj, remesh) :red:`(Under development)`

  * one -- objects placed below the splitting plane (*None* if no objects were placed below the plane)

  * two -- objects placed above the splitting plane (*None* if no objects were placed above the plane, or if the initial shape has not been fragmented in two parts)

  * shape (emptied) -- object, collection of objects, or a list [a, b, c, ...] of objects of type CONVEX, SPHERE, ELLIP or MESH

  * point -- (px, py, pz) tuple defining a point passed by the splitting plane

  * normal -- (nx, ny, nz) tuple defining the splitting plane normal

  * surfid -- (surf1, surf2) tuple defining a pair of surface identifier for the two newly created
    surfaces (default: 0,0). Surface surf1 has the outward normal (nx, ny, nz).

  * topoadj -- 'ON' or 'OFF' (default: 'OFF'); when 'OFF' the splitting will always propagate across
    the whole body and result in two body fragments; when 'ON' the splitting will propagate from the
    input point through the topologically adjacent elements, which may not produce fragmentation;

  * remesh -- 'ON' or 'OFF' (default: 'ON') flag used only for MESH based shapes; when 'ON' mesh splitting
    away from inter--element boundaries will lead to tetrahedral re--meshing; when 'OFF' it will raise an error.

*WARNING:* Mesh splitting generates tetrahedral mesh in place of the input one if the splitting plane
is not aligned with element boundaries. The meshing is randomized and it may generate different results
for the same input. Use TETRAHEDRALIZE in order to refine and save the generated mesh parts. Otherwise
may encounter input/output errors.

MESH_SPLIT
----------

This routine splits a mesh object along the internal element boundaries whose nodes belong to the given node set.
Depending on the topological properties of the mesh this may or may not result in splitting of the mesh in multiple parts.

.. topic:: [out1, out2, ...] = MESH_SPLIT (mesh, nodeset | surfid) :red:`(Under development)`

  * [out1, out2, ...] -- a list of output meshes (*None* if no internal element boundaries in the input mesh were split)

  * mesh -- input MESH object (the input mesh is not modified by this routine)

  * nodeset -- a list of nodes [n0, n1, n2, ...] defining the splitting surface (zero based indexing)

  * surfid -- surface identifier for the newly created surfaces (default: 0)

COPY
----

This routine makes a copy of input objects.

.. topic:: obj = COPY (shape)

  * obj -- created collection of copied objects

  * shape -- object, collection of objects, or a list [a, b, c, ...] of objects of type CONVEX, MESH, SPHERE, ELLIP

BEND
----

This routine bends a shape around an axis. The bending is performed from the section of the shape
closest to the axis onward. The orientation of the axis direction determines the orientation of the
bending according to the right hand rule. Let :math:`\mathbf{q}` be the closest to the axis mesh node.
Then :math:`\mathbf{v}=\mathbf{d}\times\left(\mathbf{q}-\mbox{proj}\left(\mathbf{q}\right)\right)`,
where :math:`\mathbf{d}` is the axis direction and :math:`\mbox{proj\ensuremath{\left[\cdot\right]}}`
projects a point onto the axis. Bending starts from the section containing :math:`\mathbf{q}` and proceeds
in the direction of :math:`\mathbf{v}`.

.. topic:: obj = BEND (shape, point, direction, angle)

  * obj -- same as shape

  * shape -- object of type MESH

  * point -- axis point

  * direction -- axis direction

  * angle -- positive bending angle in degrees

BYLABEL
-------

This routine finds a labelled object inside of a SOLFEC object.

.. topic:: obj = BYLABEL (solfec, kind, label)

  * obj -- returned object (*None* if a labelled object was not found)

  * solfec -- SOLFEC object

  * kind -- labelled object: 'SURFACE_MATERIAL', 'BULK_MATERIAL', 'BODY', 'FIELD'

  * label -- the label string

MASS_CENTER
-----------

This routine calculates the mass center of a geometrical object or a collection of such objects.

.. topic:: obj = MASS_CENTER (shape)

  * obj -- (x, y, z) tuple storing the mass center

  * shape -- object, collection of objects, or a list [a, b, c, ...] of objects of type
    CONVEX, MESH, SPHERE, ELLIP. Alternately this can be a single BODY object.

LOCDYN_DUMP
-----------

This routine dumps into a file the most recent state of local dynamics.
It is meant for debugging and test purposes, e.g. comparing local dynamics
between runs on various processor counts.

.. topic:: LOCDYN_DUMP (solfec, path)

  * solfec -- SOLFEC object

  * path -- file path

OVERLAPPING
-----------

This routine looks for shapes (not) overlapping the obstacles.

.. topic:: obj = OVERLAPPING (obstacles, shapes | not, gap)

  * obj -- list of shapes (not) ovrelapping the obstacles

  * obstacles -- object, collection of objects, or a list [a, b, c, ...] of objects of type CONVEX, MESH, SPHERE, ELLIP

  * shapes (emptied) -- object, collection of objects, or a list [a, b, c, ...] of objects of type CONVEX, MESH, SPHERE, ELLIP

  * not -- 'NOT' string

  * gap -- maximal negative gap

MBFCP_EXPORT
------------

This routine exports Solfec model into the MBFCP problem definition format. See `this link <http://code.google.com/p/mbfcp/>`_ for details.

.. topic:: MBFCP_EXPORT (solfec, path)

  * solfec -- SOLFEC object

  * path -- output path

NON_SOLFEC_ARGV
---------------

This routine returns all command line arguments (in the form of a list of strings)
that have been passed to 'solfec' or 'solfec--mpi' application and has not been identified
as valid Solfec arguments. This way the user can pass some arguments to the input scripts.

.. topic:: argv = NON_SOLFEC_ARGV ()

  * argv -- list of non--solfec specific arguments passed to 'solfec' or 'solfec--mpi' command

MODAL_ANALYSIS
--------------

This routine performs modal analysis of FEM bodies.
The modal analysis results are stored with bodies and can be viewed.

.. topic:: obj = MODAL_ANALYSIS (body, num, path | abstol, maxiter, verbose)

  * obj = (val, vec) -- the returned tuple of: val = obj[0] eigenvalues and
    vec = obj[1] eigen vectors (stored contiguously one after another)

  * body -- input FEM body; the model analysis results are stored with this body

  * num -- number of lowest modes to extract

  * path -- path to file where the results will be stored (to avoid recomputing if possible).
    Note, that if previous modal analysis results are found they are used rather then recomputed
    if the number of modes and num are the same. If num is different from the previous modes count,
    then new num modes is computed from scratch.

  * abstol -- residual tolerance for the eigenvalue solver (default: 1E-11)

  * maxiter -- iterations bound for the eigenvalue solver (default: 100)

  * verbose -- 'ON' or 'OFF' verbosity flag for the eigenvalue solver (default: 'OFF')

BODY_MM_EXPORT
--------------

Export body matrices in the MatrixMarket sparse format.

.. topic:: BODY_MM_EXPORT (body, pathM, pathK | spdM, spdK)

  * body -- BODY object of 'FINITE_ELEMENT' kind

  * pathM -- output path for mass matrix M

  * pathK -- output path for stiffness matrix K

  * spdM -- symmetric positive definite flag M; 'ON' or 'OFF' (default: 'ON'); only lower triangle is exported when 'ON'

  * spdK -- symmetric positive definite flag K; 'ON' or 'OFF' (default: 'ON'); only lower triangle is exported when 'ON'

DISPLAY_POINT
-------------

Attach a display point to a body. Display points are defined in reference
configuration and convected with bodies. Display points can be visualised by
selecting 'display points on/off' in the 'tools' viewer menu. They serve purely
auxiliary purpose, for example allowing to make sure that the results are read
from correct locations.

.. topic:: DISPLAY_POINT (body, point | label)

  * body -- BODY object

  * point -- referential (x, y, z) point

  * label -- optional label

RENDER
------

Render selected bodies in the Viewer. *Note:* This *cannot* be used from within a normal analysis script,
but only from a Viewer script by selecting 'run python script' in the 'tools' viewer menu.

.. topic:: RENDER(solfec, object) :red:`(Under development)`

  * solfec -- SOLFEC object

  * object -- BODY object or a list of BODY objects

