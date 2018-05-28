import subprocess

print 'Decompressing data files...'
process = subprocess.Popen('unzip -o data.zip', shell=True)
process.wait()

print 'Scanning runtimes...'
with open('data/tr2-dru100-nsgs-runtimes', 'r') as inp0:
  ln = inp0.readline()
  ln = ln.split(' = ')
  while ln != ['']:
    nsgsrun = ln[0]
    print 'run:', nsgsrun
    print 'solver:', 'GS' if 'GS' in nsgsrun else 'NS'
    if 'NS' in nsgsrun:
      print 'reldelta:', 'OFF' if 'RLDLOFF' in nsgsrun else \
      nsgsrun[nsgsrun.index('RLDL')+4:nsgsrun.index('LEPS')-1]
    print 'kinem:', 'RG' if 'RG' in nsgsrun else 'PR'
    print 'shape:', 'ELL' if 'ELL' in nsgsrun else 'SPH'
    print 'runtime = %g' % float(ln[1])
    with open('data/tr2-dru100-nsgs-timings', 'r') as inp:
      ln = inp.readline()
      ln = ln.split(' = ')
      while ln != ['']:
	if ln[0] == nsgsrun:
	  import re
	  txt = ln[1][1:-2].replace(' ','').replace("'",'')
	  itm = re.split(',|:', txt)
	  if itm[-2] == 'TOTAL':
	    print 'timing ratios:'
	    tot = float(itm[-1])
	    for i in range(1,len(itm),2):
	      itm[i] = float(itm[i])/tot
	      print '              ', itm[i-1], itm[i]
	ln = inp.readline()
	ln = ln.split(' = ')
    with open('data/tr2-dru100-nsgs-iters', 'r') as inp:
      ln = inp.readline()
      ln = ln.split(' = ')
      while ln != ['']:
	if ln[0] == nsgsrun:
	  print 'tot. iter, avg. iter, fails:', ln[1]
	ln = inp.readline()
	ln = ln.split(' = ')
    ln = inp0.readline()
    ln = ln.split(' = ')

print 'Cleaning up...'
process = subprocess.Popen('rm -fr data', shell=True)
process.wait()
