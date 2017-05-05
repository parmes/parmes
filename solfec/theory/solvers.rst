.. _solfec-theory-solvers:

Constraint solvers
==================

Constraint solvers are used to find approximate a solution to the :ref:`constraints <solfec-theory-constraints>` equations

.. math::

  \mathbf{C}\left(\mathbf{U},\mathbf{R}\right)=\mathbf{0}

expressing :ref:`joints <solfec-theory-joints>` and :ref:`contact conditions <solfec-theory-conform>`, together with
the :ref:`local dynamics <solfec-theory-locdyn>` equations

.. math::

  \mathbf{U}=\mathbf{B}+\mathbf{WR}
  
The merit function used as one of the termination conditions by all solvers, and the algorithms of the Solfec solvers themselves,
are described in sections below.

Merit function
--------------

As discussed on the :ref:`basics page <solfec-theory-basics>`, at every time step an implicit equation
:math:`\mathbf{C}\left(\mathbf{R}\right)=\mathbf{0}` is solved. This solution is approximate. In order to express its accuracy
as a scalar value, we formulate :math:`\mathbf{C}\left(\mathbf{R}\right)` in terms of velocity
(see :ref:`the non-smooth velocity equation formulation <solfec-theory-conform-nsveq>`) and use

.. math::

   g\left(\mathbf{R}\right)=\sum_{\alpha}\left\langle \mathbf{W}_{\alpha\alpha}^{-1}\mathbf{C}_{\alpha}\left(\mathbf{R}\right),
   \mathbf{C}_{\alpha}\left(\mathbf{R}\right)\right\rangle /\sum_{\alpha}\left\langle \mathbf{W}_{\alpha\alpha}^{-1}\mathbf{B}_{\alpha},
   \mathbf{B}_{\alpha}\right\rangle

in order to approximately measure the relative amount of “energy”, due to an inexact satisfaction of constraints. The denominator corresponds
to the kinetic energy of the relative free motion, hence :math:`g\left(\mathbf{R}\right)` is the ratio of the “spurious energy” over the nominal
amount of the “energy available at the constraints”. Since inverting :math:`\mathbf{W}` would be unpractical or impossible due to its singularity,
we only use the diagonal blocks, which are always positive definite. To recapitulate, in short

.. math::

  g\left(\mathbf{R}\right)\simeq\frac{\mbox{"spurious energy due to inaccurate solution"}}{\mbox{"free energy available at the constraints"}}
  
Such merit function is used as one of the stopping criterions for the solvers described below.

.. _solfec-theory-solvers-gs:

Gauss--Seidel solver
--------------------

The equations of :ref:`local dynamics <solfec-theory-locdyn>` read

.. math::

  \mathbf{U}_{\alpha}=\mathbf{B}_{\alpha}+\sum_{\beta}\mathbf{W}_{\alpha\beta}\mathbf{R}_{\beta}
  
where :math:`\mathbf{U}_{\alpha}` are relative velocities and :math:`\mathbf{R}_{\alpha}` are reactions at constraint points. :math:`\mathbf{U}_{\alpha}`,
:math:`\mathbf{R}_{\alpha}`, :math:`\mathbf{B}_{\alpha}` are 3--vectors, while :math:`\mathbf{W}_{\alpha\beta}` are :math:`3\times3` matrix blocks. Each
constraint equation can be formulated as

.. math::

  \mathbf{C}_{\alpha}\left(\mathbf{U}_{\alpha},\mathbf{R}_{\alpha}\right)=\mathbf{0}
  
or in other words

.. math::
  :label: nleq

  \mathbf{C}_{\alpha}\left(\mathbf{B}_{\alpha}+\sum_{\beta}\mathbf{W}_{\alpha\beta}\mathbf{R}_{\beta},\mathbf{R}_{\alpha}\right)=\mathbf{0}
  
A series of 3--component non--linear equations :eq:`nleq` for all constrains can be approximately solved using the below serial Gauss--Seidel paradigm

.. |br| raw:: html

  <br />

**SERIAL_GS** :math:`\left(Constraints,\epsilon,\gamma\right)` |br|
1 :math:`\,\,` do |br|
2 :math:`\,\,\,\,\,\,` for each :math:`\alpha in Constraints` do |br|
3 :math:`\,\,\,\,\,\,` :math:`\mathbf{S}_{\alpha}=\mathbf{R}_{\alpha}` |br|
4 :math:`\,\,\,\,\,\,` find :math:`\mathbf{R}_{\alpha}` such that :math:`\mathbf{C}_{\alpha}\left(\mathbf{B}_{\alpha}+\sum_{\beta}\mathbf{W}_{\alpha\beta}\mathbf{R}_{\beta},\mathbf{R}_{\alpha}\right)=\mathbf{0}` |br|
5 :math:`\,\,\,\,\,\,\,\,\,\,` assuming :math:`\mathbf{R}_{\beta}=\mbox{constant}` for :math:`\beta\ne\alpha` |br|
6 :math:`\,\,`  while :math:`\left\Vert \mathbf{S}-\mathbf{R}\right\Vert /\left\Vert \mathbf{R}\right\Vert >\epsilon` and :math:`g\left(\mathbf{R}\right)>\gamma` |br|

Algorithm **SERIAL_GS** is quite simple: diagonal block problems are solved until reaction change is small enough. The Gauss--Seidel paradigm corresponds to the fact,
that the most recent off--diagonal reactions are used when solving the diagonal problem. Of course, because of that, a perfectly parallel implementation is not possible.
After all, reactions are updated in a sequence. We can nevertheless relax the need for sequential processing. Perhaps the most scalable Gauss--Seidel approach to date was
devised by Adams [1]_. Although originally it was used as a multigrid smoother, the core idea can be as well applied in our context. Each processor owes a subset of
(internal) constraints :math:`Q_{i}`, where :math:`i=1,2,...,n` are the processors indices. Therefore the local velocity update can be rewritten as

.. math::

  \mathbf{U}_{\alpha}=\mathbf{B}_{\alpha}+\sum_{\beta\in Q_{i}}\mathbf{W}_{\alpha\beta}\mathbf{R}_{\beta}+\sum_{\beta\notin Q_{i}}\mathbf{W}_{\alpha\beta}\mathbf{R}_{\beta}

Some of the :math:`\mathbf{W}_{\alpha\beta}` blocks and reactions :math:`\mathbf{R}_{\beta}` correspond to the (external) constraints stored on other processors (:math:`\beta\notin Q_{i}`).
Let us denote the set of corresponding reaction indices by :math:`P_{i}`. That is 

.. math::

  P_{i}=\left\{ \beta:\exists\mathbf{W}_{\alpha\beta}\ne\mathbf{0}\mbox{ and }\alpha\in Q_{i}\mbox{ and }\beta\notin Q_{i}\right\}
  
For each :math:`\beta\in P_{i}` we know an index of processor :math:`cpu\left(\beta\right)` storing the constraint with index :math:`\beta`.
For processor :math:`i` we can then define a set of adjacent processors as follows

.. math::

  adj\left(i\right)=\left\{ cpu\left(\beta\right):\beta\in P_{i}\right\}
  
When updating reactions, a processor needs to communicate only with other adjacent processors. We are going to optimize a pattern of this communication by
coloring the processors. We shall then assign to each processor a color, such that no two adjacent processors have the same color. A simple coloring method
is summarized in Algorithm **COLOR** below

**COLOR** :math:`\left(\right)` |br|
1 :math:`\,\,` for :math:`i=1,...,n` do :math:`color\left[i\right]=0` |br|
2 :math:`\,\,` for :math:`i=1,...,n` do |br|
3 :math:`\,\,\,\,\,\,` do |br|
4 :math:`\,\,\,\,\,\,\,\,\,\,` :math:`color\left[i\right]=color\left[i\right]+1` |br|
5 :math:`\,\,\,\,\,\,` while for any :math:`j\in adj\left(i\right)` there holds :math:`color\left[i\right]=color\left[j\right]` |br|

We try to assign as few colors as possible. We then split the index sets :math:`Q_{i}` as follows

.. math::

  Top_{i}=\left\{ \alpha:\forall\mathbf{W}_{\alpha\beta}:\beta\in P_{i}\wedge color\left[cpu\left(\beta\right)\right]<color\left[i\right]\right\} 

.. math::

  Bottom_{i}=\left\{ \alpha:\forall\mathbf{W}_{\alpha\beta}:\beta\in P_{i}\wedge color\left[cpu\left(\beta\right)\right]>color\left[i\right]\right\} 

.. math::

  Middle_{i}=\left\{ \alpha:\forall\mathbf{W}_{\alpha\beta}:\beta\in P_{i}\wedge\alpha\notin Top_{i}\cup Bottom_{i}\right\} 

.. math::

  Inner_{i}=Q_{i}\setminus\left\{ Top_{i}\cup Bottom_{i}\cup Middle_{i}\right\}
  
The top constraints require communication only with processors of lower colors. The bottom constraints require communication only with processors of higher colors.
The middle constraints require communication with either. The inner constraints require no communication. The inner reactions are further split in two sets

.. math::

  Inner_{i}=Inner1_{i}\cup Inner2_{i}so that

.. math::
  :label: gsbalcnd

  \left|Bottom_{i}\right|+\left|Inner2_{i}\right|=\left|Top_{i}\right|+\left|Inner1_{i}\right|
  
The parallel Gauss--Seidel scheme is summarized in Algorithm **PARALLEL_GS** below. The presented version is simplified in the respect,
that alternate forward and backward runs are not accounted for (in terms of constraints ordering). 

**SWEEP** :math:`\left(Set\right)` |br|
1 :math:`\,\,` for each :math:`\alpha\in Set` do |br|
2 :math:`\,\,\,\,\,\,` find :math:`\mathbf{R}_{\alpha}` such that :math:`\mathbf{C}_{\alpha}\left(\mathbf{B}_{\alpha}+\sum_{\beta}\mathbf{W}_{\alpha\beta}\mathbf{R}_{\beta},\mathbf{R}_{\alpha}\right)=\mathbf{0}` |br|
3 :math:`\,\,\,\,\,\,\,\,\,\,` assuming :math:`\mathbf{R}_{\beta}=\mbox{constant}` for :math:`\beta\ne\alpha` |br|

**LOOP** :math:`\left(Set\right)` |br|
1 :math:`\,\,` descending sort of :math:`\alpha\in Set` based on :math:`\max\left(color\left[cpu\left(\beta\right)\right]\right)` where :math:`\exists\mathbf{W}_{\alpha\beta}` |br|
2 :math:`\,\,` for each ordered :math:`\alpha in Set` do |br|
3 :math:`\,\,\,\,\,\,` for each :math:`\beta` such that :math:`\exists\mathbf{W}_{\alpha\beta}` and :math:`color\left[cpu\left(\alpha\right)\right]<color\left[cpu\left(\beta\right)\right]` do |br|
4 :math:`\,\,\,\,\,\,\,\,\,\,` if not received :math:`\left(\mathbf{R}_{\beta}\right)` then receive :math:`\left(\mathbf{R}_{\beta}\right)` |br|
5 :math:`\,\,\,\,\,\,` find :math:`\mathbf{R}_{\alpha}` such that :math:`\mathbf{C}_{\alpha}\left(\mathbf{B}_{\alpha}+\sum_{\beta}\mathbf{W}_{\alpha\beta}\mathbf{R}_{\beta},\mathbf{R}_{\alpha}\right)=\mathbf{0}` |br|
6 :math:`\,\,\,\,\,\,\,\,\,\,` assuming :math:`\mathbf{R}_{\beta}=\mbox{constant}` for :math:`\beta\ne\alpha` |br|
7 :math:`\,\,\,\,\,\,` send :math:`\left(\mathbf{R}_{\alpha}\right)` |br|
8 :math: `\,\,` receive all remaining :math:`\mathbf{R}_{\beta}` |br|

**PARALLEL_GS** :math:`\left(\epsilon,\gamma\right)` |br|
1 :math:`\,\,` COLOR :math:`\left(\right)` |br|
2 :math:`\,\,` do |br|
3 :math:`\,\,\,\,\,\,` :math:`\mathbf{S}=\mathbf{R}` |br|
4 :math:`\,\,\,\,\,\,` SWEEP :math:`\left(Top_{i}\right)` |br|
5 :math:`\,\,\,\,\,\,` send :math:`\left(Top_{i}\right)` |br|
6 :math:`\,\,\,\,\,\,` SWEEP :math:`\left(Inner2_{i}\right)` |br|
7 :math:`\,\,\,\,\,\,` receive :math:`\left(Top_{i}\right)` |br|
8 :math:`\,\,\,\,\,\,` LOOP :math:`\left(Middle_{i}\right)` |br|
9 :math:`\,\,\,\,\,\,` SWEEP :math:`\left(Bottom_{i}\right)` |br|
10 :math:`\,\,\,\,\,` send :math:`\left(Bottom_{i}\right)` |br|
11 :math:`\,\,\,\,\,` SWEEP :math:`\left(Inner1_{i}\right)` |br|
12 :math:`\,\,\,\,\,` receive :math:`\left(Bottom_{i}\right)` |br|
13 :math:`\,` while :math:`\left\Vert \mathbf{S}-\mathbf{R}\right\Vert /\left\Vert \mathbf{R}\right\Vert >\epsilon` and :math:`g\left(\mathbf{R}\right)>\gamma`

In **PARALLEL_GS** we first process the :math:`Top_{i}` set: a single sweep over the corresponding diagonal block problems is performed in line 4. Then we send the
computed top reactions to the processors with lower colors. We try to overlap communication and computation, hence we sweep over the :math:`Inner2_{i}` set (line 6) while
sending. We then receive the top reactions. It should be noted that all communication is asynchronous -- we only wait to receive reactions immediately necessary
for computations. In line 8 we enter the loop processing the :math:`Middle_{i}` set. This is the location of the computational bottleneck. Middle nodes communicate
with processors of higher and lower colors and hence, they need to be processed in a sequence. The sequential processing is still relaxed by using processor coloring.
In the **LOOP** algorithm we first sort the constraints according to the descending order of maximal colors of their adjacent processors (line 1). We then maintain
this ordering while processing constraints. As the top reactions were already sent, some of the constraints from the middle set will have their external reactions from
higher colors fully updated. These will be processed first in line 5 of LOOP and then sent to lower and higher (by color) processors in line 7. This way some processors
with lower colors will have their higher color off-diagonal reactions of middle set constraints fully updated and they will proceed next. And so on. At the end (line 8),
we need to receive all remaining reactions that have been sent in line 7 of **LOOP**. Coming back to **PARALLEL_GS**, after the bottleneck of the LOOP, in lines 9--12 we
process the :math:`Bottom_{i}` and :math:`Inner1_{i}` sets in the same way as we did with the :math:`Top_{i}` and :math:`Inner2_{i}` sets. The condition :eq:`gsbalcnd`
attempts to balance the amount of computations needed to hide the communication (e.g. the larger the :math:`Top_{i}` set is, the larger the :math:`Inner2_{i}` set becomes).
It should be noted that the convergence criterion in line 13 is global across all processors. 

In :ref:`User Manual Solvers Section <solfec-user-solvers>` several variants of the parallel Gauss--Seidel algorithm are listed. Algorithm **PARALLEL_GS** corresponds to
the FULL variant. We might like to relax the bottleneck of **LOOP** in line 8 of **PARALLEL_GS** by replacing it with

8.1 :math:`\,\,` SWEEP :math:`\left(Middle_{i}\right)` |br|
8.2 :math:`\,\,` send :math:`\left(Middle_{i}\right)` |br|
8.3 :math:`\,\,` receive :math:`\left(Middle_{i}\right)` |br|

so that the middle nodes are processed in an inconsistent manner: the off--processor information corresponds to the previous iteration (just like in the Jacobi method).
Usually the :math:`Middle_{i}` sets are small and hence this inconsistency does not have to lead to divergence (especially for deformable kinematics, where constraint
interactions are weak, while :math:`\mathbf{W}` is diagonally dominant). This is the MIDDLE_JACOBI variant of the algorithm. The last variant corresponds to a rather
gross inconsistency: something usually called “a processor Gauss-Seidel method”. Let us define the set

.. math::

  All_{i}=Top_{i}\cup Bottom_{i}\cup Middle_{i}\cup Inner_{i}
  
In this case, lines 4--12 of **PARALLEL_GS** need to be replaced with

3 :math:`\,\,` SWEEP :math:`\left(All_{i}\right)` |br|
4 :math:`\,\,` send :math:`\left(All_{i}\right)` |br|
5 :math:`\,\,` receive :math:`\left(All_{i}\right)` |br|

Although this kind of approach does work as a multigrid smoother, it has little use in our context. Nevertheless, we use it for illustration sake and name the BOUNDARY_JACOBI.

.. _solfec-theory-solvers-pqn:

Projected Newton solver
-----------------------

Using the :ref:`non--smooth velocity equation formulation <solfec-theory-conform-nsveq>` let us rewrite the frictional contact problem as

.. math::

  \mathbf{C}\left(\mathbf{R}\right)=\mathbf{F}\left(\mathbf{R}\right)+\mathbf{m}\left(\mathbf{R}-\mathbf{F}\left(\mathbf{R}\right)\right)=\mathbf{0}\mbox{ and }\mathbf{R}\in K
  
where :math:`K` is the direct sum of friction cones at all contact points. Since :math:`\mathbf{C}\left(\mathbf{R}\right)` is not smooth, to compute :math:`\nabla\mathbf{C}` we
generalize the approach from [2]_ and [3]_ and use a smoothed :math:`\nabla_{\omega}\mathbf{C}` with :math:`\omega>0` (we skip the details here), where only the self--dual case
was considered (friction coefficient equal to 1). Our idea is to employ the following projected quasi--Newton step

.. math::
  :label: newton

  \mathbf{R}^{k+1}=\mbox{proj}_{K}\left[\mathbf{R}^{k}-\mathbf{A}^{-1}\mathbf{C}\left(\mathbf{R}\right)\right]
  
so that, as required, the iterates remain within the friction cone and where 

.. math::

  \mathbf{A}\simeq\nabla_{\omega}\mathbf{C}
  
is an easy to invert approximation of :math:`\nabla_{\omega}\mathbf{C}`. Since in many practical situations :math:`\nabla_{\omega}\mathbf{C}` is singular, we cannot do not employ 
it directly. Instead, we then two variants of :math:`\mathbf{A}\simeq\nabla_{\omega}\mathbf{C}`. The first one reads

.. math::

  \mathbf{A}_{1}=\nabla_{\omega}\mathbf{C}+\delta\mathbf{I},\mbox{ combined with GMRES.}
  
where :math:`\delta\ge0`. This is related to numerical integration of an artificial ODE 

.. math::

  \frac{d\mathbf{R}}{dt}=\mathbf{C}\left(\mathbf{R}\right)

to a steady state (take one step of implicit Euler, in the literature this is called pseudo--transient continuation). The second variant reads

.. math::

  \mathbf{A}_{2}=\mbox{diag}_{3\times3}\left[\nabla_{\omega}\mathbf{C}\right],\mbox{ combined with direct inversion.}

and it is combined with a heuristic stabilization technique

.. math::

  \triangle\mathbf{R}^{k+1}=\left(1-\theta\right)\triangle\mathbf{R}^{k}-\theta\left(\mathbf{A}^{k}\right)^{-1}\mathbf{C}^{k}
  
where

.. math::

  \theta\in\left[0,1\right]\mbox{.}
  
We then have two variants of the projected quasi--Newton step:

1. PQN1:

.. math::

  \mathbf{R}^{k+1}=\mbox{proj}_{K}\left[\mathbf{R}^{k}-\left(\nabla_{\omega}\mathbf{C}^{k}+\delta\mathbf{I}\right)_{\mbox{GMRES}\left(\epsilon\left\Vert \mathbf{C}^{k}\right\Vert ,m\right)}^{-1}\mathbf{C}^{k}\right]

where GMRES is preconditioned with :math:`\left[\mbox{diag}_{3\times3}\left(\nabla_{\omega}\mathbf{C}_{\alpha\alpha}^{k}+\delta\mathbf{I}\right)\right]^{-1}` and :math:`\delta`,
:math:`\epsilon` and :math:`m` need to be suitably selected. The linear problem should be solved only roughly, usually :math:`\epsilon=0.25` and :math:`m=10` (iterations
bound) work well. For ill--conditioned problems a too accurate solution of the linear sub--problem results in a poor convergence rate. The diagonal regularization :math:`\delta`
needs to be adjusted “by hand”. The automatic update formulas that can be found in literature work only for well--conditioned cases and hence they are not very useful for us.
For ill--conditioned problems one should pick :math:`\delta` that delivers an overall best convergence behavior. Large values will slow down convergence, but stabilize it;
small values may destabilize convergence for ill--conditioned problems; :math:`\delta` (typically :math:`\ll1`) should be tuned together with :math:`\epsilon` and :math:`m`
(e.g. find a suitably small :math:`\delta` first, then tweak :math:`\epsilon`). Since rigorous analysis is still missing for these parameters, please experiment before settling
on specific values for a specific problem. Use linver = 'GMRES' in :ref:`NEWTON_SOLVER <solfec-command-NEWTON_SOLVER>` to enable this variant (this is also the default).

2. PQN2:

.. math::

  \mathbf{R}^{k+1}=\mbox{proj}_{K}\left[\mathbf{R}^{k}+\left(1-\theta\right)\triangle\mathbf{R}^{k}-\theta\left(\mbox{diag}_{3\times3}\left[\nabla_{\omega}\mathbf{C}^{k}\right]\right)^{-1}\mathbf{C}^{k}\right]
  
where :math:`\theta\in\left[0,1\right]` and the diagonal :math:`3\times3` blocks of :math:`\nabla_{\omega}\mathbf{C}^{k}` are directly inverted. This simple scheme is interesting
because it converges for a sufficiently small :math:`\theta`, while it is essentially a nonlinear Jacobi--type method. Use linver = 'DIAG' in :ref:`NEWTON_SOLVER <solfec-command-NEWTON_SOLVER>`
to enable this variant.

Both variants are summarized as algorithms below.

**PQN1** :math:`\left(\mathbf{R},\gamma,n,\omega,\delta,m,\epsilon\right)` |br|
1 :math:`\,\,` :math:`\triangle\mathbf{R}^{0}=\mathbf{0}, k=0` |br|
2 :math:`\,\,` Do |br|
3 :math:`\,\,\,\,\,\,` :math:`\mathbf{U}^{k}=\mathbf{W}\mathbf{R}^{k}+\mathbf{B}` |br|
4 :math:`\,\,\,\,\,\,` Compute :math:`\mathbf{C}^{k}` and :math:`\mathbf{A}^{k}=\nabla_{\omega}\mathbf{C}_{\alpha\alpha}^{k}+\delta\mathbf{I}` using smoothing :math:`\omega` |br|
5 :math:`\,\,\,\,\,\,` :math:`\triangle\mathbf{R}^{k+1}=-\left(\mathbf{A}^{k}\right)_{\mbox{GMRES}\left(\epsilon\left\Vert \mathbf{C}^{k}\right\Vert ,m\right)}^{-1}\mathbf{C}^{k}` |br|
6 :math:`\,\,\,\,\,\,` :math:`\mathbf{R}^{k+1}=\mbox{proj}_{K}\left[\mathbf{R}^{k}+\triangle\mathbf{R}^{k+1}\right]` |br|
7 :math:`\,\,\,\,\,\,` :math:`k=k+1` |br|
8 :math:`\,\,\,\,\,\,` while :math:`g\left(\mathbf{R}^{k}\right)\ge\gamma` and :math:`k<n` |br|

**PQN2** :math:`\left(\mathbf{R},\theta,\gamma,n,\omega\right)` |br|
1 :math:`\,\,` :math:`\triangle\mathbf{R}^{0}=\mathbf{0}, k=0` |br|
2 :math:`\,\,` Do |br|
3 :math:`\,\,\,\,\,\,` :math:`\mathbf{U}^{k}=\mathbf{W}\mathbf{R}^{k}+\mathbf{B}` |br|
4 :math:`\,\,\,\,\,\,` Compute :math:`\mathbf{C}^{k}` and :math:`\mathbf{A}^{k}=\mbox{diag}_{3\times3}\left[\nabla_{\omega}\mathbf{C}_{\alpha\alpha}^{k}\right]` using smoothing :math:`\omega` |br|
5 :math:`\,\,\,\,\,\,` :math:`\triangle\mathbf{R}^{k+1}=\left(1-\theta\right)\triangle\mathbf{R}^{k}-\theta\left(\mathbf{A}^{k}\right)^{-1}\mathbf{C}^{k}` |br|
6 :math:`\,\,\,\,\,\,` :math:`\mathbf{R}^{k+1}=\mbox{proj}_{K}\left[\mathbf{R}^{k}+\triangle\mathbf{R}^{k+1}\right]` |br|
7 :math:`\,\,\,\,\,\,` :math:`k=k+1` |br|
8 :math:`\,\,` while :math:`g\left(\mathbf{R}^{k}\right)\ge\gamma` and :math:`k<n` |br|

.. _solfec-theory-solvers-penalty:

Penalty Solver
--------------

The penalty solver is quite straightforward. On each processor we split the constraints into :math:`Contacts_{i}` and :math:`Others_{i}`,
hence we separate contact constraints from bilateral ones. We then update the contacts using the spring--dashpot model and calculate reactions
of bilateral constraints using the Gauss--Seidel solver (fixed accuracy :math:`\mbox{epsilon=1E-4, maxiter = 1000}` is used). We use the
Gauss--Seidel approach for non--contacts because in this case it is quite fast, while it avoids issues related to penalization of bilateral constraints. 

**PENALTY_SOLVER** :math:`\left(\right)` |br|
1 :math:`\,\,` for all :math:`\alpha` in :math:`Contacts_{i}` do |br|
2 :math:`\,\,\,\,\,\,` SPRING_DASHPOT_CONTACT :math:`\left(h,gap_{\alpha},spring_{\alpha},dashpot_{\alpha},friction_{\alpha},cohesion_{\alpha},cohesive_{\alpha}\right)` |br|
3 :math:`\,\,` send :math:`\left(Contacts_{i}\right)` |br|
4 :math:`\,\,` receive :math:`\left(Contacts_{i}\right)` |br|
5 :math:`\,\,` PARALLEL_GS :math:`\left(Others_{i}\right)` |br|

Algorithm **PENALTY_SOLVER** summarizes the method. First all contact forces are calculated using the :ref:`SPRING_DASHPOT_CONTACT algorithm <spring-dashpot-contact>`.
In lines 3 and 4 contact domain boundary contact forces are sent to and received on the neighboring processors. Finally, the parallel Gauss--Seidel algorithm is executed
to calculate the reactions of the bilateral constraints. In the serial mode lines 3 and 4 are skipped, while **SERIAL_GS** is used instead of the parallel one.

Implementation
--------------

The Gauss--Seidel solver is implemented in `bgs.c <https://github.com/tkoziara/solfec/blob/master/bgs.c>`_ and
`bgs.h <https://github.com/tkoziara/solfec/blob/master/bgs.h>`_.
The projected Newton solver is implemented in `nts.c <https://github.com/tkoziara/solfec/blob/master/nts.c>`_ and
`nts.h <https://github.com/tkoziara/solfec/blob/master/nts.h>`_.
The penalty solver is implemented in `pes.c <https://github.com/tkoziara/solfec/blob/master/pes.c>`_ and
`pes.h <https://github.com/tkoziara/solfec/blob/master/pes.h>`_.

.. [1] Mark F. Adams, A distributed memory unstructured Gauss--Seidel algorithm for multigrid smoothers, In Supercomputing 01:
       Proceedings of the 2001 ACM/IEEE conference on Supercomputing, pages 4-4, New York, USA, 2001.
.. [2] Masao Fukushima, Zhi-Quan Luo, and Paul Tseng, Smoothing functions for second-order-cone complementarity problems,
       SIAM Journal on Optimization, 12(2):436–460, 2002.
.. [3] Shunsuke Hayashi, Nobuo Yamashita, and Masao Fukushima, A Combined Smoothing and Regularization Method for Monotone
       Second--Order Cone Complementarity Problems, SIAM J. Optim., 15(2), 593–615, 2005.
