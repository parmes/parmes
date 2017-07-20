.. _solfec-user-fragmentation:

Fragmentation
=============

Routines listed in this section control fragmentation of bodies.

.. role:: red

RT_SPLIT
--------

This routine splits a meshed BODY object along a surface aligned with internal element boundaries. It can be invoked from within a callback function
-- see the :ref:`CALLBACK command <solfec-command-CALLBACK>` -- and hence “RT” stands for “runtime”.

.. topic:: (body2, lst1, lst2) = RT_SPLIT (body1, surf | sid1, sid2, label1, label2) :red:`(Under development)`

  * body2 -- created BODY object or *None* if the split does not create another body

  * lst1, lst2 -- lists mapping original mesh node numbers to new mesh node numbers in **body1** and **body2**. Only **lst1**
    is valid in case of a split which does not create two separate bodies -- in this case **lst2** = *None*

  * body1 -- a MESH based BODY which is split

  * surf -- surface definition of the split plane on **body1**: a list of lists of face nodes *[[n0, n1, n2], [n3, n4, n5, n6], ...]*
    defining the splitting surface (zero based indexing)

  * sid1 -- optional identifier for the newly created surface on **body1**; default: 0

  * sid2 -- optional identifier for the newly created surface on **body2**; default: 0

  * label1 -- optional label of **body1**; default: *None* (split in two bodies) or no change (a partial split of **body1**)

  * label2 -- optional label of **body2**; default: *None*

Properties:

1. **surf** normals are calculated so that the face nodes are counter clockwise oriented when looking from the positive normal direction.

2. **body2** is on the positive side of **surf**, i.e. the normals of **surf** points towards the newly created body.

3. **body1** maintains its ID as long as **body2** == *None*.

4. ID of **body1** changes when **body2** != *None* (when two fragments are created).

5. All constraints attached to **body1** are deleted during splitting.

6. All forces applied to **body1** are deleted during splitting.

7. RT_SPLIT terminates with an error message in case none or more then two mesh fragments were created.
