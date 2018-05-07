.. _parmec-output_files:

.. role:: red

Output files
============

Currently Parmec supports the following output file formats:

* For spherical particles:

  - `LAMMPS <http://lammps.sandia.gov/doc/dump.html>`_ \*.dump files :red:`(under development)`;
    can be viewed with `OVITO <https://ovito.org/>`_

* For mesh based particles, for rigid bodies, for contact points, and for springs:

  - `*.vtk <http://www.vtk.org/wp-content/uploads/2015/04/file-formats.pdf>`_ text files;
    can be viewed with `ParaView <https://www.paraview.org/>`_, `OVITO <https://ovito.org/>`_

  - `*.xmf <http://www.xdmf.org/index.php/XDMF_Model_and_Format>`_ binary files;
    can be viewed with `ParaView <https://www.paraview.org/>`_

  - `*.med <http://www.salome-platform.org/user-section/about/med>`_ binary files :red:`(under development)`;
    can be viewed with `Gmsh <http://gmsh.info/>`_, `SALOME <http://www.salome-platform.org/>`_

See also the :ref:`OUTPUT <parmec-command-OUTPUT>` command for details on outputted entities and file kinds. 

|

.. topic:: Status (as of commit `5ab402d <https://github.com/tkoziara/parmec/tree/5ab402de99d7970abdb53c27b07d8c0bb4bd56d1>`_)

   The \*.dump file format is not fully supported at this point: it can be used to view animated results for spheres,
   without any output entities. The \*.vtk and \*.xmf file formats are fairly complete and can be used to view motion
   of particles as well as time histories of all output fields and entities. The \*.med file format currently supports
   only mesh data (it does not include output for rigid bodies, contact points, and springs).
