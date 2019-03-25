from matplotlib import colors, cm
import matplotlib.pyplot as plt
import numpy as np
import subprocess
import ast

reldelta = ['minWii', 'avgWii', 'maxWii']
kinem = ['RG', 'PR']
cases = ['A', 'B', 'C']
X_label = ['delta', 'delta', 'delta']
Y_label = ['epsilon', 'm', '(m, eps)']
X_index = [6, 6, 6]
Y_index = [8, 9, (8, 9)]
X_Y_plots = ['Total ietarations', 'Avg. iter. when converged', 'Diverged solves']


print 'Decompressing data files...'
process = subprocess.Popen('unzip -o example1-data.zip', shell=True)
process.wait()

for rldl in reldelta:
  print 'Plotting %s iterations...' % rldl
  for kin in kinem:
    for case in cases:
      V_X = {}
      V_Y = {}
      V_X_Y = {}
      ic = cases.index(case)
      with open('example1-data/tr2-dru100-reldelta-iters', 'r') as inp:
	ln = inp.readline()
	ln = ln.split(' = ')
	while ln != ['']:
	  name = ln[0].split('_')
	  data = [int(x) for x in ln[1].split(',')]
	  if name[0] == case and name[3] == kin and name[7][4:] == rldl:
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
	Z.fill(0)
	for pnt in V_X_Y:
	  i = V_X.index(pnt[0])
	  j = V_Y.index(pnt[1])
	  d = V_X_Y[pnt]
	  Z[j][i] = float(d[k])
	plt.figure()
	plt.scatter(X, Y, c=Z, edgecolors='none', s=200, norm=colors.LogNorm(), cmap=cm.jet)
	plt.colorbar()
	plt.title(X_Y_plots[k] + ' (%s)' % rldl)
	plt.xlabel(X_label[ic])
	plt.ylabel(Y_label[ic])
	plt.xticks (xlist, [str(x) for x in V_X])
	plt.yticks (ylist, [str(y) for y in V_Y])
	plt.savefig ('dru100_%s_%s%d_%s.png' % (kin, case, k, rldl), bbox_inches='tight', pad_inches=0)
	plt.close()

  print 'Plotting %s runtimes...' % rldl
  for kin in kinem:
    for case in cases:
      V_X = {}
      V_Y = {}
      V_X_Y = {}
      ic = cases.index(case)
      with open('example1-data/tr2-dru100-reldelta-runtimes', 'r') as inp:
	ln = inp.readline()
	ln = ln.split(' = ')
	while ln != ['']:
	  name = ln[0].split('_')
	  data = float(ln[1])
	  if name[0] == case and name[3] == kin and name[7][4:] == rldl:
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
      Z.fill(0)
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
      plt.xticks (xlist, [str(x) for x in V_X])
      plt.yticks (ylist, [str(y) for y in V_Y])
      plt.savefig ('dru100_%s_%s_%s_runtimes.png' % (kin, case, rldl), bbox_inches='tight', pad_inches=0)
      plt.close()

  '''
  print 'Plotting %s timing ratios...' % rldl
  for kin in kinem:
    for case in cases:
      V_X = {}
      V_Y = {}
      V_X_Y = {}
      ic = cases.index(case)
      with open('data/tr2-dru100-reldelta-timings', 'r') as inp:
	ln = inp.readline()
	ln = ln.split(' = ')
	while ln != ['']:
	  name = ln[0].split('_')
	  data = ast.literal_eval(ln[1])
	  if name[0] == case and name[3] == kin and name[7][4:] == rldl:
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
      Z.fill(0)
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
      plt.xticks (xlist, [str(x) for x in V_X])
      plt.yticks (ylist, [str(y) for y in V_Y])
      plt.savefig ('dru100_%s_%s_%s_ratios.png' % (kin, case, rldl), bbox_inches='tight', pad_inches=0)
      plt.close()
  '''

print 'Cleaning up...'
process = subprocess.Popen('rm -fr example1-data', shell=True)
process.wait()
