.. _solfec-examples-hybrid_modelling-hs3_scaling:

3--dimensional cube array parallel scaling
==========================================

This is a 3--dimensional case, `solfec/examples/hybrid--solver3 <https://github.com/tkoziara/solfec/tree/master/examples/hybrid-solver3>`_,
of the family of :ref:`1,2 and 3--dismenional examples <solfec-examples-hybrid_modelling-hs123>`, demonstrating applications of
the :ref:`HYBRID_SOLVER <hybrid-solver>` to hybrid, :ref:`Parmec <parmec-index>`--:ref:`Solfec <solfec-index>` based, arrays of cubes
subject to an acceleration sine dwell signal. The specifcation of geomery and material data are exactly generalized from
:ref:`the 2--dimensional counterpart <solfec-examples-hybrid_modelling-hs123>`.
The `solfec/examples/hybrid--solver3 <https://github.com/tkoziara/solfec/tree/master/examples/hybrid-solver3>`_ directory contains:

- `README <https://github.com/tkoziara/solfec/blob/master/examples/hybrid-solver3/README>`_ -- a text based specification of the problem

- `hs2--parmec.py <https://github.com/tkoziara/solfec/blob/master/examples/hybrid-solver3/hs3-parmec.py>`_ -- including the :ref:`Parmec <parmec-index>` input code

- `hs2--solfec.py <https://github.com/tkoziara/solfec/blob/master/examples/hybrid-solver3/hs3-solfec.py>`_ -- including the :ref:`Solfec <solfec-index>` input code

- `hs2--state--1.pvsm <https://github.com/tkoziara/solfec/blob/master/examples/hybrid-solver3/hs3-state-1.pvsm>`_ -- `ParaView <http://www.paraview.org>`_ state for animation [1]_

- `hs2--state--2.pvsm <https://github.com/tkoziara/solfec/blob/master/examples/hybrid-solver3/hs3-state-2.pvsm>`_ -- `ParaView <http://www.paraview.org>`_ state for animation [2]_

.. _hybrid-solver3: https://github.com/tkoziara/solfec/tree/master/examples/hybrid-solver3

.. [1] `ParaView <http://www.paraview.org>`_ animation based on the state file 
  `hs3--state--1.pvsm <https://github.com/tkoziara/solfec/blob/master/examples/hybrid-solver3/hs3-state-1.pvsm>`_.
  The see--through array is modeled in Parmec: rotations are restrained and spring--dashpot elements, emulating contact,
  are insered at the centres of faces of neighbouring cubes. The solid 3x3 inner arrays is modeled in Solfec: hexahedral
  finite elements are used and contact interactions are modelled via :ref:`a non--smooth Signorini--Coulomb law <solfec-theory-conform>`

.. youtube:: https://www.youtube.com/watch?v=L4ylaXQTQsY
  :width: 648
  :height: 364

.. [2] `ParaView <http://www.paraview.org>`_ animation based on the state file 
  `hs3--state--3.pvsm <https://github.com/tkoziara/solfec/blob/master/examples/hybrid-solver3/hs3-state-2.pvsm>`_.
  Parmec spring forces are visualised on the left hand side. On the right hand side, in the Solfec model,
  the spheres symbolizse detected contact points, while their colors depict the magnitudes of the contact forces.

.. youtube:: https://www.youtube.com/watch?v=FfPGKxlr5kQ
  :width: 648
  :height: 364

Animations [1]_ and [2]_ are based on :math:`(M+N+M)\times(M+N+M)\times(M+N+M)` arrays, where :math:`M = 5` and :math:`N = 3`.
To test parallel scaling, a large model, with :math:`M = 5` and :math:`N = 20`, was used. This resulted in the total number of
27000 bodies, of which the inner 8000 was modeled using :math:`2\times2\times2` finite element meshes in Solfec. None of the
remaining parameters of the model were changed. Animation [3]_ depicts this larger model.

.. [3] `ParaView <http://www.paraview.org>`_ animation of the 30x30x30 model with N=20. A part of the Parmec model
  is hidden so that the inner 20x20x20 Solfec array can be seen; this also helps to visualize interaction between
  the Parmec and Solfec submodels.

.. youtube:: https://www.youtube.com/watch?v=7eR4iCSTG44
  :width: 648
  :height: 364

:numref:`hs3-runtimes` summarises the parallel runtimes. Total speedup of 4.45 was achieved using 192 CPU cores,
versus the baseline single cluster node run on 24 CPU cores. Intel Xeon E5--2600 CPU based nodes were used,
with 24 cores per node and InfiniBand 1 x 56 Gb/s FDR interconnect. We note, that only the inner :math:`20\times20\times20`
Solfec array was parallelized using MPI; the entire Parmec model (the remaining 19000 bodies) was run on MPI rank 0 process,
utilising task based parallelism (in all cases all 24 cores of the single node were used).

.. _hs3-runtimes:

.. table:: Example hybrid-solver3_ (M=5,N=20): runtime scaling.

  +---------------+-------------+--------------+--------------+--------------+
  | CPU cores     | 24          |  48          |  96          |  192         | 
  +---------------+-------------+--------------+--------------+--------------+
  | Runtime [h]   | 11.56       | 6.62         | 3.99         | 2.60         |
  +---------------+-------------+--------------+--------------+--------------+

Animation [4]_ depicts load balancing of contact points within Solfec submodel. The inner :math:`20\times20\times20`
array generates about 68000 contact points on average. :numref:`hs3-stats-1` summarises the minimum, average and maximum
numbers of bodies and contact points for 24--192 MPI ranks (CPU cores). Solfec utilizes a single geometrical
partitioning in order to balance together the bodies and the contact points. Contact points are favoured in the load
balancing (hence their better overall balance) due to the higher computational work related to their processing.
:numref:`hs3-stats-2` shows that contact update, detection, solution and assembling of the :ref:`local dynamics <solfec-theory-locdyn>`
take up the majority of the computational time.

.. [4] :ref:`Solfec viewer <solfec-running>` based animation of load balancing for the 30x30x30 model with N=20.
  Contact points are colored according to processor rank for the 24 CPU cores based parallel run. Solfec utilizes
  :ref:`dynamic load balancing <dynlb-index>` in order maintain parallel balance.

.. youtube:: https://www.youtube.com/watch?v=rO5Qw4HG6sw
  :width: 648
  :height: 364

.. _hs3-stats-1:

.. table:: Example hybrid-solver3_ (M=5,N=20): body and contact point count statistics.

  +---------------+-------------+--------------+--------------+--------------+
  | CPU cores     | 24          |  48          |  96          |  192         | 
  +---------------+-------------+--------------+--------------+--------------+
  | Body min      | 297         | 134          | 63           | 22           |
  +---------------+-------------+--------------+--------------+--------------+
  | Body avg      | 433         | 216          | 108          | 54           |
  +---------------+-------------+--------------+--------------+--------------+
  | Body max      | 620         | 340          | 190          | 116          |
  +---------------+-------------+--------------+--------------+--------------+
  | Contact min   | 2655        | 1310         | 639          | 294          |
  +---------------+-------------+--------------+--------------+--------------+
  | Contact avg   | 2835        | 1435         | 735          | 368          |
  +---------------+-------------+--------------+--------------+--------------+
  | Contact max   | 3031        | 1578         | 846          | 457          |
  +---------------+-------------+--------------+--------------+--------------+

|

.. _hs3-stats-2:

.. table:: Example hybrid-solver3_ (M=5,N=20): average computational task share percentage (%).

  +-------------------+-------------+--------------+--------------+--------------+
  | CPU cores         | 24          |  48          |  96          | 192          | 
  +-------------------+-------------+--------------+--------------+--------------+
  | Time integration  | 10.1        | 8.8          | 7.4          | 7.4          |
  +-------------------+-------------+--------------+--------------+--------------+
  | Contact update    | 8.8         | 9.8          | 10.7         | 11.5         |
  +-------------------+-------------+--------------+--------------+--------------+
  | Contact detection | 13.0        | 12.2         | 11.0         | 8.9          |
  +-------------------+-------------+--------------+--------------+--------------+
  | Local dynamics    | 22.2        | 21.6         | 20.8         | 20.4         |
  +-------------------+-------------+--------------+--------------+--------------+
  | Contact solution  | 27.8        | 25.0         | 22.8         | 18.2         |
  +-------------------+-------------+--------------+--------------+--------------+
  | Load balancing    | 18.0        | 22.5         | 27.3         | 33.7         |
  +-------------------+-------------+--------------+--------------+--------------+
