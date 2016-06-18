.. _solfec-xdmf:

Solfec XDMF export
==================

XDMF export allows Solfec results to be saved in `XDMF format <http://www.xdmf.org>`_ and viewed in `Paraview <http://www.paraview.org>`_
and other post--processors. A quick example of Python syntax is provided below:

::

  XDMF_EXPORT (solfec, (0.0, 1.0), '/tmp/sim0')

where results from the time interval :math:`[0.0, 1.0]` are exported into the '/tmp/sim0' directory. A typical Solfec workflow including XDMF export could be:

1. Prepare and run an input deck (e.g. submit a batch job onto a HPC cluster).

2. Run Solfec again and export a subset of results by calling XDMF_EXPORT from within your input deck (Solfec needs to be in the 'READ' mode).

3. Copy the exported fiels into your desktop compouter and view them using Paraview or another post--processor.

.. note:: Within a HPC environment, when processing files resulting from large parallel runs, you may need to
          use anotehr batch job, since reading from network drives may be slow.  You can also try to copy your
	  output files (temporarily) into a head node hard drive (e.g. your home directory) and export XDMF
	  from there using an interactive ssh session.

.. only:: html

  The following sections provide additional details about the XDMF export functionality:

.. toctree::

   xdmf/export
   xdmf/example
   xdmf/paraview
