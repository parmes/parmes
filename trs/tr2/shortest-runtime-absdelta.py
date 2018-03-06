import subprocess

kinem = ['RG', 'PR']
cases = ['A', 'B', 'C']
X_label = ['delta', 'delta', 'delta']
Y_label = ['epsilon', 'm', '(m, eps)']
X_index = [6, 6, 6]
Y_index = [8, 9, (8, 9)]
X_Y_plots = ['Total ietarations', 'Avg. iter. when converged', 'Diverged solves']

print 'Decompressing data-absdelta files...'
process = subprocess.Popen('unzip -o data-absdelta.zip', shell=True)
process.wait()

print 'Scanning runtimes...'
for kin in kinem:
  mintime = 1E10
  mintdelta = 0
  minteps = 0.0
  mintm = 0
  for case in cases:
    ic = cases.index(case)
    with open('data-absdelta/tr2-dru100-absdelta-runtimes', 'r') as inp:
      ln = inp.readline()
      ln = ln.split(' = ')
      while ln != ['']:
	name = ln[0].split('_')
	data = float(ln[1])
	if name[0] == case and name[3] == kin:
	  x = float(name[X_index[ic]][4:])
	  yi = Y_index[ic]
	  if type(yi) is tuple:
	    y = (float(name[yi[0]][4:]), float(name[yi[1]][4:]))
	  else: y = float(name[yi][4:])
	  if data < mintime:
	    mintime = data
	    mintdelta = x
	    if case == 'A':
	      minteps = y
	      mintm = 1000
	    elif case == 'B':
	      minteps = 0.001
	      mintm = y
	    else:
	      minteps = y[0]
	      mintm = y[1]
	ln = inp.readline()
	ln = ln.split(' = ')
  print '%s: min runtime = %g for (delta, epsilon, m) = (%g, %g, %d)' % (kin, mintime, mintdelta, minteps, mintm)

print 'Cleaning up...'
process = subprocess.Popen('rm -fr data-absdelta', shell=True)
process.wait()
