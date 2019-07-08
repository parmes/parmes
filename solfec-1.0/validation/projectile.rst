.. _solfec-validation-projectile:

Projectile in a ballistic motion
================================

.. |br| raw:: html

  <br />

+---------------------------------------------------------------------------------------------------------------------------------+
| **Reference:** `J. B. Marion, S. T. Thornton, Classical Dynamics of Particles & Systems, 3rd Edition, Reference: Saunders       |
| College Publishing, 1988, pp. 60-63. <https://archive.org/details/ClassicalDynamicsOfParticlesAndSystemsMarionThornton>`_       |
| |br|                                                                                                                            |
| **Analysis:** Explicit dynamics, unconstrained linear motion.                                                                   |
| |br|                                                                                                                            |
| **Purpose:** Examine the accuracy of integration of the linear motion.                                                          |
| |br|                                                                                                                            |
| **Summary:** A projectile is subjected to gravity and air resistance loading. The total travel time and travel distance are     |
| calculated for an assumed initial velocity and air resistance proportionality constant, :math:`k`.                              |
+---------------------------------------------------------------------------------------------------------------------------------+

The air resistance force reads

.. math::

  \mathbf{f}_{air}=-km\mathbf{v}
  
where :math:`k` is the resistance proportionality constant, :math:`m` is the mass, and :math:`\mathbf{v}`
is the point mass velocity (nonzero in the :math:`x-z` plane). The exact solution is

.. math::

  \mathbf{x}\left(t\right)=\left[\begin{array}{c}
  \frac{v_{1}\left(0\right)}{k}\left(1-\exp\left(-kt\right)\right)\\
  0\\
  \frac{-g_{3}t}{k}+\frac{kv_{3}\left(0\right)+g_{3}}{k^{2}}\left(1-\exp\left(-kt\right)\right)
  \end{array}\right]
  
where :math:`g_{3}` is the vertical component of the gravity acceleration vector :math:`\mathbf{g}`.
The travel time from the ground level :math:`x_{3}\left(0\right)=0` until :math:`x_{3}\left(T\right)=0` is given by

.. math::
  :label: T

  T=\frac{hv_{3}\left(0\right)+g_{3}}{g_{3}k}\left(1-\exp\left(-kT\right)\right)

Input parameters
----------------

+---------------------------------------------------+-----------------------------------------------+
| Mass :math:`\left(kg\right)`                      | :math:`m=0.45359237`                          |
+---------------------------------------------------+-----------------------------------------------+
| Initial linear velocity :math:`\left(m/s\right)`  | :math:`\mathbf{v}=\left[2.54,0,12.7\right]`   |
+---------------------------------------------------+-----------------------------------------------+
| Gravity acceleration :math:`\left(m/s^{2}\right)` | :math:`\mathbf{g}=\left[0,0,-9.81456\right]`  |
+---------------------------------------------------+-----------------------------------------------+
| Proportionality constant                          | :math:`k=1`                                   |
+---------------------------------------------------+-----------------------------------------------+

Results
-------

The solution of equation :eq:`T` is :math:`T=1.976` seconds. The time step used in the analysis was :math:`h=T/1024`.
The table below and :numref:`projectile` summarise the results.

+-------------------------------------------------------------+-----------+--------------+---------+
|                                                             | Target    | Solfec-1.0   | Ratio   |
+-------------------------------------------------------------+-----------+--------------+---------+
| Travel time for projectile :math:`\left(s\right)`           | 1.9760    | 1.9760       | 1.000   |
+-------------------------------------------------------------+-----------+--------------+---------+
| :math:`x`-direction travel distance :math:`\left(in\right)` | 86.138    | 86.081       | 0.999   |
+-------------------------------------------------------------+-----------+--------------+---------+

.. _projectile:

.. figure:: projectile/projectile.png
   :width: 75%
   :align: center

   Displacement of projectile over time.
