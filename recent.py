import time
import re
import os

nrecent = 8

print 'Generating up to %d recently updated pages list...' % nrecent

matches = []
exclude = ['./__*', './.git*', './blog*']
pattern = [re.compile(item) for item in exclude]
for root, dirnames, filenames in os.walk('.'):
  if not any (p.match(root) for p in pattern):
    for filename in filenames:
      if filename.endswith('.rst'):
	matches.append(os.path.join(root, filename))

exclude = ['./recent.rst', './index.rst']
matches = [item for item in matches if item not in exclude]
matches.sort(key=os.path.getmtime)
matches.reverse()
matches = matches[:nrecent]

with open ('./recent.rst', 'w') as f:
  for name in matches:
    parts = name[2:-4].split('/')
    label = parts[0]
    for p in parts[1:]: label += '-'+p
    tstr = time.strftime('%m/%d/%Y', time.gmtime(os.path.getmtime(name)))
    f.write ('\n')
    f.write ('* On %s :ref:`%s`\n' % (tstr, label))
