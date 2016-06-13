.. _solfec-xdmf:

Solfec XDMF export
==================

XDMF export allows Solfec results to be saved in `XDMF format <http://www.xdmf.org>`_ and viewed in `Paraview <http://www.paraview.org>`_
and other post--processors. A quick example of an export is provided below:

::

  XDMF_EXPORT (solfec, (0.0, 1.0), '/tmp/sim0')

where solfec results from time interval :math:`[0.0, 1.0]` are exported into the '/tmp/sim0' directory.
The following sections provide more details about the export functionality:

.. toctree::

   xdmf/export
   xdmf/example
   xdmf/paraview
