.. _solfec-examples-hybrid_modelling-hs0:

A two--body impact problem
==========================

This is a simplest application of the :ref:`HYBRID_SOLVER <hybrid-solver>`. The input files for this example are
located in the `solfec/examples/hybrid--solver0 <https://github.com/tkoziara/solfec/tree/master/examples/hybrid-solver0>`_ directory.
These are:

- `README <https://github.com/tkoziara/solfec/blob/master/examples/hybrid-solver0/README>`_ -- a text based specification of the problem

- `hs0--parmec.py <https://github.com/tkoziara/solfec/blob/master/examples/hybrid-solver0/hs0-parmec.py>`_ -- including the :ref:`Parmec <parmec-index>` input code

- `hs0--solfec--1.py <https://github.com/tkoziara/solfec/blob/master/examples/hybrid-solver0/hs0-solfec-1.py>`_ -- including the simpler version of the :ref:`Solfec <solfec-index>` input code

- `hs0--solfec--2.py <https://github.com/tkoziara/solfec/blob/master/examples/hybrid-solver0/hs0-solfec-2.py>`_ -- Solfec input file demonstrating a more elaborate usage of Parmec and Solfec features

.. _hs0-fig1:

.. figure:: hs0.png
   :width: 80%
   :align: center

   Example `hybrid--solver0 <https://github.com/tkoziara/solfec/tree/master/examples/hybrid-solver0>`_: a two body impact problem

:numref:`hs0-fig1` states the problem. Both, the upper "Solfec" body and the lower "Parmec" body are modelled as rigid.
The upper body falls under gravity and hits the lower body, initiating vibrations. There is no impact restitution between
the two bodies, hence the two bodies stay and vibrate togther, following the initial impact. We use this simple example
to illustrate the methodology of creating a hybrid model.

:numref:`hs0-lst1` includes the Parmec file `hs0--parmec.py <https://github.com/tkoziara/solfec/blob/master/examples/hybrid-solver0/hs0-parmec.py>`_.
The :ref:`material <parmec-command-MATERIAL>` is created in line 1 and the :ref:`meshed <parmec-command-MESH>` lower cube is created in line 16.
The cube's motion is :ref:`restrained <parmec-command-CONSTRAIN>` along x, y translations and x, y, z rotations in line 18. The :ref:`elastic spring
<parmec-command-SPRING>` is created in line 20. We note, that no damping is applied and that the spring direction is fixed along z.
:ref:`Gravity <parmec-command-GRAVITY>` is applied in line 23. This concludes the input file.

.. literalinclude:: ../../../../solfec/examples/hybrid-solver0/hs0-parmec.py
   :linenos:
   :caption: Listing of hs0--parmec.py
   :name: hs0-lst1


The "DEM" command in line 25 can be uncommented to run parmec standalone and test this example:

::

  parmec4 examples/hybrid-solver0/hs0-parmec.py

This is useful at a stage of creating and testing of an input file: the output files generated into the hybrid--solver0
directory and be viewed using `ParaView <http://www.paraview.org>`_. 

.. note:: For the sake of using hs0--parmec.py as Parmec input in Solfec's :ref:`HYBRID_SOLVER <hybrid-solver>`,
          the "DEM" command in line 25 should remain commented out.


:numref:`hs0-lst2` includes the Solfec file `hs0--solfec--1.py <https://github.com/tkoziara/solfec/blob/master/examples/hybrid-solver0/hs0-solfec-1.py>`_.
:ref:`SOLFEC object <solfec-user-solfec>` is created in line 3, specifying the output directory as 'out/hybrid--solver0' (relative where *solfec* is run from).

.. literalinclude:: ../../../../solfec/examples/hybrid-solver0/hs0-solfec-1.py
   :linenos:
   :caption: Listing of hs0--solfec--1.py
   :name: hs0-lst2
