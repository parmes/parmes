.. _solfec-examples-reduced_order:

Reduced order modeling
======================

In Solfec-1.0, in the finite element context, it is possible to reduce the size of the per--body
algebraic systems by applying `reduced order <https://en.wikipedia.org/wiki/Model_order_reduction>`_
or `modal <https://en.wikipedia.org/wiki/Modal_analysis_using_FEM>`_ simplifications. Both of these
are combined with a body--level co--rotational approach in order to incorporate large rigid body
rotations -- relevant in the multibody context. The details of this can be found in the technical
report :ref:`TR1 <tr1>` and in :ref:`this blog post <tr1-post>`. Currently available examples of
this functionality include:

.. toctree::
  :maxdepth: 1

  reduced_order/ro0
  reduced_order/ro1
  81array
