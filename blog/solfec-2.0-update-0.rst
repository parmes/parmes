.. post:: Sep 9, 2019
   :tags: solfec-2.0
   :author: Tomek

.. _blog-solver-2.0-update-0:

Solfec-2.0 update 0
===================

Just a little note to say that work on `Solfec-2.0 <https://github.com/parmes/solfec-2.0/>`_ is underway:)
Currently the code cannot do much: I am ironing out a basic parallel data layout. I am using a simple global
array based approach, utilising MPI-3.0 RDMA (remote direct memory access). It's based on the implementation
suggested in the book `"Using Advanced MPI" <https://mitpress.mit.edu/books/using-advanced-mpi>`_. The current
version of the array code is here: `ga.hpp <https://github.com/parmes/solfec-2.0/blob/1fe5e2c2364db1909877192a0c8ed409a631677f/cpp/ga.hpp#L38>`_
and `ga.cpp <https://github.com/parmes/solfec-2.0/blob/1fe5e2c2364db1909877192a0c8ed409a631677f/cpp/ga.cpp#L37>`_.
The way the arrays are used to store computational data can be viewed in `compute.hpp
<https://github.com/parmes/solfec-2.0/blob/1fe5e2c2364db1909877192a0c8ed409a631677f/cpp/compute.hpp#L37>`_.
Since the arrays are of fixed size -- there is a little bit of book keeping that needs to be implemented -- in
order to allow for arbitrary sequences of insertions and deletions of computational data. This is the aspect
of the code, which I am currently implementing and smoothing out. Only MPI rank-0 process is interpreting the
input Python file -- the remaining processes join in during the computation loop -- which can be invoked multiple
times from the input file -- with insertions and deletions of computational data in between. (...)

So the basic idea is to use the global arrays as the sole mechanism of distributed memory access (with exceptions
-- e.g. when using linear solvers). And then locally, on each MPI rank, use tasks that pull data from arrays
and compute what needed using SIMD-accelerated kernels. I am using `cpp-taskflow <https://github.com/cpp-taskflow/cpp-taskflow>`_
and `ISPC <https://ispc.github.io>`_ as the supporting tools for these aspects. The results will also be stored
back into the arrays in a concurrent way. And I will try to use a single-task graph to represent the entire
computational step. So the computational loop will simply invoke this task graph multiple times:) Initially,
I am intending to transfer :ref:`Solfec-1.0's <solfec-1.0-index>` functionality into this framework: copy the
existing finite elements and other aspects of the code, while readjusting them for SIMD parallelism. Only after
this basic functionality is transferred and sufficiently tested, I will begin to look into updating the FE
technology itself. That's the overall idea a this moment:)
