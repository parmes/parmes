.. _solfec-1.0-xdmf-export:

XDMF_EXPORT command
===================

Python syntax for XDMF export reads:

.. topic:: XDMF_EXPORT (solfec, time, path | subset, attributes)
	
 Export results in XDMF format. In 'WRITE' mode only the geometry at time :math:`t=0` is saved,
 while arguments *time* and *attributes* are ignored.

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

Currently implemented features:

* Export of MESH and CONVEX shape based bodies into a <path>_grids.xmf file.

* Export of constraints into a <path>_constraints.xmf file.

* Expot of SPHERE shape based bodies into a <path>_spheres.xmf file.

Currently missing features:

* Export of ELLIP shape based bodies.

In the :ref:`following section <solfec-1.0-xdmf-example>` we give an example of an application of the above command.

.. [1] `POSIX regular expressions <https://en.wikibooks.org/wiki/Regular_Expressions/POSIX_Basic_Regular_Expressions>`_
