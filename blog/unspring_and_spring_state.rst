.. post:: Jan 15, 2018
   :tags: parmec, springs, failure
   :author: Tomek

.. _blog-unspring-and-spring-state:


UNSPRING and spring state in Parmec
===================================

`PARMEC <../parmec/>`_ includes a capability to model rigid body and :ref:`SPRING <parmec-command-SPRING>` systems.
As a part of it an :ref:`UNSPRING <parmec-command-UNSPRING>` command allows to deactivate selected springs
when a total force of a set of "test springs" exceeds a prescribed bound. This facilitates modelling
of simple failure scenarios. Spring states are outputted as scalar fields (in XDMF format) and can be
viewed with `ParaView <http://www.paraview.org>`_ or similar tools. The video clip below is based on `this
example <https://github.com/tkoziara/parmec/blob/master/tests/unspring.py>`_.  Spring states can be visualized
by selecting the 'SS' entity and using "Coor Map Editor" in ParaView to "Interpret Values as Cathegories"
(checkbox at the top of the editor dialog box) and then adding the discrete values used by the 'SS' field
(-3.0, -2.0, -1.0, ...) as described for the :ref:`OUTPUT command <parmec-command-OUTPUT>`. Spring states
can also be outputted as :ref:`HISTORY <parmec-command-HISTORY>` (as in the example).  (...)

  .. youtube:: https://www.youtube.com/watch?v=DlGXRKHxOv8
    :width: 640
    :height: 360
