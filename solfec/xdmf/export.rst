.. _solfec-xdmf-export:

XDMF_EXPORT command
===================

The Solfec Python command for XDMF export reads:

.. topic:: XDMF_EXPORT (solfec, time, path | subset, attributes)
	
 Export results in XDMF format. Ignored in 'WRITE' mode.

 * solfec -- SOLFEC object;

 * time -- time instant, e.g. t0, a collection of time instants,
   e.g. [t0, t1, t2, ..., tN], or a time interval, e.g. (t0, t1);

 * path -- output path to the directory that will contain the XDMF markup file(s) and a HDF5 data file;
   e.g. '/tmp/sim0' will possibly result in a /tmp/sim0/sim0_grids.xmf, /tmp/sim0/sim0_constraints.xmf,
   /tmp/sim0/sim0_spheres.xmf markup files and a /tmp/sim0/sim0.h5 data file output;

 * subset -- specification of a subset of exported bodies; a string can be used to define a POSIX regular
   expression [*]_ that will be matched against body labels; a list of body objects or integer body identifiers
   can be used [body1, body2, id3, id4, body5, ...] mixed up in an arbitrary manner; or a tuple specifying
   extents of a bounding box can be used (xlow, ylow, zlow, xhigh, yhigh, zhigh), which the bounding boxes of
   exported bodies will overlapped at time t=0; also a list of an arbitrary combination of those can be used,
   e.g. ['BOD*A', 123, body1, body2, 256, (0, 0, 0, 1, 1, 1), 'KEY??7', (3, 3, 3, 4, 4, 4)] defines two labels,
   two integer body ids, two body objects, and two bounding boxes, that together define a subset of bodies
   that will be used during export;

 * attributes -- list of export attributes; default ['DISP', 'VELO', 'REAC', 'GAP'];
   available attributes are 'DISP' (body displacement), 'VELO' (body velocity), 'STRESS' (body stress),
   'REAC' (constraint reactions), 'RELV' (relative constraint velocities), 'GAP' (contact gaps);


Currently implemented features:

* Grids

* Constraints

* Spheres

Currently missing features:

* Ellipsoids

.. [*] `POSIX regular expressions <http://www.boost.org/doc/libs/1_61_0/libs/regex/doc/html/boost_regex/syntax/basic_syntax.html>`_
