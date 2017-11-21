from matplotlib import colors, cm
import matplotlib.pyplot as plt
import numpy as np
import subprocess
import ast

kinem = ['rig', 'prb']
cases = ['A', 'B', 'C']
X_label = ['delta', 'delta', 'delta']
Y_label = ['epsilon', 'm', '(m, eps)']
X_index = [6, 6, 6]
Y_index = [7, 8, (7, 8)]
X_Y_plots = ['Total ietarations', 'Avg. iter. when converged', 'Diverged solves']


print 'Decompressing data files...'
process = subprocess.Popen('unzip -f data.zip', shell=True)
process.wait()

print 'Plotting iterations...'
for kin in kinem:
  for case in cases:
    V_X = {}
    V_Y = {}
    V_X_Y = {}
    ic = cases.index(case)
    with open('data/tr2-dru100-%s-iters' % kin, 'r') as inp:
      ln = inp.readline()
      ln = ln.split(' = ')
      while ln != ['']:
	name = ln[0].split('_')
	data = [int(x) for x in ln[1].split(',')]
	if name[0] == case:
	  x = float(name[X_index[ic]][4:])
	  yi = Y_index[ic]
	  if type(yi) is tuple:
	    y = (float(name[yi[0]][4:]), float(name[yi[1]][4:]))
	  else: y = float(name[yi][4:])
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
      for pnt in V_X_Y:
	i = V_X.index(pnt[0])
	j = V_Y.index(pnt[1])
	d = V_X_Y[pnt]
	Z[j][i] = float(d[k])
      plt.figure()
      plt.scatter(X, Y, c=Z, edgecolors='none', s=200, norm=colors.LogNorm(), cmap=cm.jet)
      plt.colorbar()
      plt.title(X_Y_plots[k])
      plt.xlabel(X_label[ic])
      plt.ylabel(Y_label[ic])
      plt.xticks (xlist[::2], [str(x) for x in V_X][::2])
      plt.yticks (ylist, [str(y) for y in V_Y])
      plt.savefig ('dru100_%s_%s%d.png' % (kin, case, k), bbox_inches='tight', pad_inches=0)
      plt.close()

print 'Plotting runtimes...'
for kin in kinem:
  for case in cases:
    V_X = {}
    V_Y = {}
    V_X_Y = {}
    ic = cases.index(case)
    with open('data/tr2-dru100-%s-runtimes' % kin, 'r') as inp:
      ln = inp.readline()
      ln = ln.split(' = ')
      while ln != ['']:
	name = ln[0].split('_')
	data = float(ln[1])
	if name[0] == case:
	  x = float(name[X_index[ic]][4:])
	  yi = Y_index[ic]
	  if type(yi) is tuple:
	    y = (float(name[yi[0]][4:]), float(name[yi[1]][4:]))
	  else: y = float(name[yi][4:])
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
    for pnt in V_X_Y:
      i = V_X.index(pnt[0])
      j = V_Y.index(pnt[1])
      Z[j][i] = V_X_Y[pnt]
    plt.figure()
    plt.scatter(X, Y, c=Z, edgecolors='none', s=200, norm=colors.LogNorm(), cmap=cm.jet)
    plt.colorbar()
    plt.title('Runtimes [s]')
    plt.xlabel(X_label[ic])
    plt.ylabel(Y_label[ic])
    plt.xticks (xlist[::2], [str(x) for x in V_X][::2])
    plt.yticks (ylist, [str(y) for y in V_Y])
    plt.savefig ('dru100_%s_%s_runtimes.png' % (kin, case), bbox_inches='tight', pad_inches=0)
    plt.close()

print 'Plotting timing ratios...'
for kin in kinem:
  for case in cases:
    V_X = {}
    V_Y = {}
    V_X_Y = {}
    ic = cases.index(case)
    with open('data/tr2-dru100-%s-timings' % kin, 'r') as inp:
      ln = inp.readline()
      ln = ln.split(' = ')
      while ln != ['']:
	name = ln[0].split('_')
	data = ast.literal_eval(ln[1])
	if name[0] == case:
	  x = float(name[X_index[ic]][4:])
	  yi = Y_index[ic]
	  if type(yi) is tuple:
	    y = (float(name[yi[0]][4:]), float(name[yi[1]][4:]))
	  else: y = float(name[yi][4:])
	  V_X[x] = True
	  V_Y[y] = True
	  V_X_Y[(x, y)] = data['CONSOL']/data['TOTAL']

	ln = inp.readline()
	ln = ln.split(' = ')

    V_X = sorted(V_X)
    V_Y = sorted(V_Y)
    xlist = np.linspace(0, len(V_X), len(V_X))
    ylist = np.linspace(0, len(V_Y), len(V_Y))
    X, Y = np.meshgrid(xlist, ylist)
    Z = X+Y
    for pnt in V_X_Y:
      i = V_X.index(pnt[0])
      j = V_Y.index(pnt[1])
      Z[j][i] = V_X_Y[pnt]
    plt.figure()
    plt.scatter(X, Y, c=Z, edgecolors='none', s=200, cmap=cm.jet)
    plt.colorbar()
    plt.title('Solver time / runtime')
    plt.xlabel(X_label[ic])
    plt.ylabel(Y_label[ic])
    plt.xticks (xlist[::2], [str(x) for x in V_X][::2])
    plt.yticks (ylist, [str(y) for y in V_Y])
    plt.savefig ('dru100_%s_%s_ratios.png' % (kin, case), bbox_inches='tight', pad_inches=0)
    plt.close()

print 'Cleaning up...'
process = subprocess.Popen('rm -fr data', shell=True)
process.wait()
