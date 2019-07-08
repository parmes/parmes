.. _solfec-theory-basics:

Basics
======

We introduce basic notions here. Let us have a look at :numref:`intro`.

.. _intro:

.. figure:: ../figures/intro.png
   :width: 60%
   :align: center

   A multi--body domain.

There are four bodies in the figure. Placement of each point of every body is determined by a configuration :math:`\mathbf{q}_{i}`.
Velocity of each point of every body is determined by a velocity :math:`\mathbf{u}_{i}`. Let :math:`\mathbf{q}` and :math:`\mathbf{u}`
collect configurations and velocities of all bodies. If the time history of velocity is known, the configuration time history can be
computed as

.. math::
  :label: q-update

  \mathbf{q}\left(t\right)=\mathbf{q}\left(0\right)+\int_{0}^{t}\mathbf{u}dt

The velocity is determined by integrating Newton's law

.. math::
  :label: u-update

  \mathbf{u}\left(t\right)=\mathbf{u}\left(0\right)+\mathbf{M}^{-1}\int_{0}^{t}\left(\mathbf{f}+\mathbf{H}^{T}\mathbf{R}\right)dt

where :math:`\mathbf{M}` is an inertia operator (assumed constant here), :math:`\mathbf{f}` is an out of balance force,
:math:`\mathbf{H}` is a linear operator, and :math:`\mathbf{R}` collects some point forces :math:`\mathbf{R}_{\alpha}`.
While integrating the motion of bodies, we keep track of a number of local coordinate systems (local frames). There are
four of them in the above figure. Each local frame is related to a pair of points, usually belonging to two distinct bodies.
An observer embedded at a local frame calculates the local relative velocity :math:`\mathbf{U}_{\alpha}` of one of the points,
viewed from the perspective of the other point. Let :math:`\mathbf{U}` collect all local velocities. Then, we can find
a linear transformation :math:`\mathbf{H}`, such that

.. math::
  :label: UHu

  \mathbf{U}=\mathbf{H}\mathbf{u}

In our case local frames correspond to constraints. We influence the local relative velocities by applying local forces
:math:`\mathbf{R}_{\alpha}`. This can be collectively described by an implicit relation

.. math::
  :label: CUR

  \mathbf{C}\left(\mathbf{U},\mathbf{R}\right)=\mathbf{0}

Hence, in order to integrate equations :eq:`q-update` and :eq:`u-update`, at every instant of time we need to solve the
implicit relation :eq:`CUR`. Here is an example of a numerical approximation of such procedure

.. math::
  :label: q(t+h/2)

  \mathbf{q}^{t+\frac{h}{2}}=\mathbf{q}^{t}+\frac{h}{2}\mathbf{u}^{t}

.. math::
  :label: u(t+h)

  \mathbf{u}^{t+h}=\mathbf{u}^{t}+\mathbf{M}^{-1}h\mathbf{f}^{t+\frac{h}{2}}+\mathbf{M}^{-1}\mathbf{H}^{T}\mathbf{R}

.. math::
  :label: q(t+h)

  \mathbf{q}^{t+h}=\mathbf{q}^{t+\frac{h}{2}}+\frac{h}{2}\mathbf{u}^{t+h}

where :math:`h` is a discrete time step. As the time step h does not appear by :math:`\mathbf{M}^{-1}\mathbf{H}^{T}\mathbf{R}`,
:math:`\mathbf{R}` should now be interpreted as an impulse (an integral of reactions over :math:`\left[t,t+h\right]`). At a start we have

.. math::
  :label: ini

  \mathbf{q}^{0}\mbox{ and }\mathbf{u}^{0}\mbox{ as prescribed initial conditions.}

The out of balance force

.. math::

  \mathbf{f}^{t+\frac{h}{2}}=\mathbf{f}\left(\mathbf{q}^{t+\frac{h}{2}},t+\frac{h}{2}\right)

incorporates both internal and external forces. The symmetric and positive-definite inertia operator

.. math::

  \mathbf{M}=\mathbf{M}\left(\mathbf{q}^{0}\right)

is computed once. The linear operator

.. math::

  \mathbf{H}=\mathbf{H}\left(\mathbf{q}^{t+\frac{h}{2}}\right)

is computed at every time step. The number of rows of :math:`\mathbf{H}` depends on the number of constraints,
while its rank is related to their linear independence. We then compute

.. math::

  \mathbf{B}=\mathbf{H}\left(\mathbf{u}^{t}+\mathbf{M}^{-1}h\mathbf{f}^{t+\frac{h}{2}}\right)

and

.. math::
  :label: W

  \mathbf{W}=\mathbf{H}\mathbf{M}^{-1}\mathbf{H}^{T}

which is symmetric and semi-positive definite. The linear transformation

.. math::
  :label: locdyn

  \mathbf{U}=\mathbf{B}+\mathbf{W}\mathbf{R}

maps constraint reactions :math:`\mathbf{R}` into local relative velocities :math:`\mathbf{U}=\mathbf{H}\mathbf{u}^{t+h}` at time :math:`t+h`.
Relation :eq:`locdyn` will be here referred to as the *local dynamics*. Finally

.. math::
  :label: constraints

  \mathbf{R}\mbox{ is such that }\mathbf{C}\left(\mathbf{U},\mathbf{R}\right)=
  \mathbf{C}\left(\mathbf{B}+\mathbf{W}\mathbf{R},\mathbf{R}\right)=
  \mathbf{C}\left(\mathbf{R}\right)=\mathbf{0}

where :math:`\mathbf{C}` is a nonlinear and usually nonsmooth operator. A basic Contact Dynamics algorithm can be summarised as follows:

1. Perform first half--step :math:`\mathbf{q}^{t+\frac{h}{2}}=\mathbf{q}^{t}+\frac{h}{2}\mathbf{u}^{t}`.
2. Update existing constraints and detect new contact points.
3. Compute :math:`\mathbf{W}`, :math:`\mathbf{B}`.
4. Solve :math:`\mathbf{C}\left(\mathbf{R}\right)=\mathbf{0}`.
5. Update velocity :math:`\mathbf{u}^{t+h}=\mathbf{u}^{t}+\mathbf{M}^{-1}h\mathbf{f}^{t+\frac{h}{2}}+\mathbf{M}^{-1}\mathbf{H}^{T}\mathbf{R}`.
6. Perform second half--step :math:`\mathbf{q}^{t+h}=\mathbf{q}^{t+\frac{h}{2}}+\frac{h}{2}\mathbf{u}^{t+h}`.

It should be emphasized that the above presentation exemplifies only a particular
instance among many available variants of `Contact Dynamics <https://en.wikipedia.org/wiki/Contact_dynamics>`_.
