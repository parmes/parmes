.. post:: Jan 9, 2019
   :tags: solfec-1.0
   :author: Tomek

.. _blog-solfec_export:

SOLFEC_EXPORT command
=====================

In analogy to Solfec's :ref:`XDMF_EXPORT <solfec-xdmf>` command, a new :ref:`SOLFEC_EXPORT <solfec-command-SOLFEC_EXPORT>`
command has been added. This allows to save a subset of results into a separate directory and view them using Solfec's
viewer. Within Solfec sources example `inp/devel/solfec-export.py <https://github.com/parmes/solfec/blob/master/inp/devel/solfec-export.py>`_
depicts an application of this idea. (...)

Assuming we are inside of Solfec source directory, this example can be executed as follows:

::
  
  ./solfec inp/devel/solfec-export.py --geom0

to first demonstrate the export of initial geometry in 'WRITE' mode, followed by

::
  
  ./solfec -v out/sxptest0/

to view the initial state using Solfec's viewer. To test the results export in the 'READ' mode run **twice**:

::
  
  ./solfec inp/devel/solfec-export.py

and then view any of the output files:

::
  
  ./solfec -v out/sxptest1
  ./solfec -v out/sxptest2
  ./solfec -v out/sxptest3
  ./solfec -v out/sxptest4
  ./solfec -v out/sxptest5

Listing of the input file, below, may help to associate those directories with a particular kind
of exported subset.

.. literalinclude:: ../../solfec-1.0/inp/devel/solfec-export.py
   :linenos:
