from matplotlib import colors, cm
import matplotlib.pyplot as plt
import numpy as np
import subprocess
import ast

kinem = ['RG', 'PR']
X_label = 'delta'
Y_label = 'density'
X_Y_plots = ['Total ietarations', 'Avg. iter. when converged', 'Diverged solves']

print 'Decompressing data files...'
process = subprocess.Popen('unzip -o example1-data.zip', shell=True)
process.wait()

print 'Plotting iterations...'
for kin in kinem:
  V_X = {}
  V_Y = {}
  V_X_Y = {}
  with open('example1-data/tr2-dru100-density-iters', 'r') as inp:
    ln = inp.readline()
    ln = ln.split(' = ')
    while ln != ['']:
      name = ln[0].split('_')
      data = [int(x) for x in ln[1].split(',')]
      if name[2] == kin:
	x = float(name[5][4:])
	y = float(name[11][3:])
	V_X[x] = True
	V_Y[y] = True
	V_X_Y[(x, y)] = data

      ln = inp.readline()
      ln = ln.split(' = ')

  V_X = sorted(V_X)
  V_Y = sorted(V_Y)
  xlist = np.linspace(0, len(V_X), len(V_X))
  ylist = np.linspace(0, len(V_Y), len(V_Y))
  X, Y = np.meshgrid(xlist, ylist)
  for k in range (0, len(X_Y_plots)):
    Z = X+Y
    Z.fill(0)
    for pnt in V_X_Y:
      i = V_X.index(pnt[0])
      j = V_Y.index(pnt[1])
      d = V_X_Y[pnt]
      Z[j][i] = float(d[k])
    #print kin, k, Z
    plt.figure()
    if Z.max() > 0.0:
      plt.scatter(X, Y, c=Z, edgecolors='none', s=200, norm=colors.LogNorm(), cmap=cm.jet)
    else: plt.scatter(X, Y, c=Z, edgecolors='none', s=200, cmap=cm.jet)
    plt.colorbar()
    plt.title(X_Y_plots[k])
    plt.xlabel(X_label)
    plt.ylabel(Y_label)
    plt.xticks (xlist, [str(x) for x in V_X])
    plt.yticks (ylist, [str(y) for y in V_Y])
    plt.savefig ('dru100_%s_%d_dens.png' % (kin, k), bbox_inches='tight', pad_inches=0)
    plt.close()

print 'Plotting runtimes...'
for kin in kinem:
  V_X = {}
  V_Y = {}
  V_X_Y = {}
  with open('example1-data/tr2-dru100-density-runtimes', 'r') as inp:
    ln = inp.readline()
    ln = ln.split(' = ')
    while ln != ['']:
      name = ln[0].split('_')
      data = float(ln[1])
      if name[2] == kin:
	x = float(name[5][4:])
	y = float(name[11][3:])
	V_X[x] = True
	V_Y[y] = True
	V_X_Y[(x, y)] = data

      ln = inp.readline()
      ln = ln.split(' = ')

  V_X = sorted(V_X)
  V_Y = sorted(V_Y)
  xlist = np.linspace(0, len(V_X), len(V_X))
  ylist = np.linspace(0, len(V_Y), len(V_Y))
  X, Y = np.meshgrid(xlist, ylist)
  Z = X+Y
  Z.fill(0)
  for pnt in V_X_Y:
    i = V_X.index(pnt[0])
    j = V_Y.index(pnt[1])
    Z[j][i] = V_X_Y[pnt]
  plt.figure()
  plt.scatter(X, Y, c=Z, edgecolors='none', s=200, norm=colors.LogNorm(), cmap=cm.jet)
  plt.colorbar()
  plt.title('Runtimes [s]')
  plt.xlabel(X_label)
  plt.ylabel(Y_label)
  plt.xticks (xlist, [str(x) for x in V_X])
  plt.yticks (ylist, [str(y) for y in V_Y])
  plt.savefig ('dru100_%s_dens_runtimes.png' % kin, bbox_inches='tight', pad_inches=0)
  plt.close()

print 'Cleaning up...'
process = subprocess.Popen('rm -fr example1-data', shell=True)
process.wait()
