import subprocess

reldelta = ['minWii', 'avgWii', 'maxWii']
kinem = ['RG', 'PR']
cases = ['A', 'B', 'C']
X_label = ['delta', 'delta', 'delta']
Y_label = ['epsilon', 'm', '(m, eps)']
X_index = [6, 6, 6]
Y_index = [8, 9, (8, 9)]
X_Y_plots = ['Total ietarations', 'Avg. iter. when converged', 'Diverged solves']

print 'Decompressing data-reldelta files...'
process = subprocess.Popen('unzip -o data-reldelta.zip', shell=True)
process.wait()

print 'Scanning runtimes...'
for kin in kinem:
  for rldl in reldelta:
    mintime = 1E10
    mintdelta = 0
    minteps = 0.0
    mintm = 0
    for case in cases:
      ic = cases.index(case)
      with open('data-reldelta/tr2-dru100-reldelta-runtimes', 'r') as inp:
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
    print '%s %s: min runtime = %g for (delta, epsilon, m) = (%g, %g, %d)' % (kin, rldl, mintime, mintdelta, minteps, mintm)

print 'Cleaning up...'
process = subprocess.Popen('rm -fr data-reldelta', shell=True)
process.wait()
