import subprocess
import time
import re
import os

nrecent = 10

print 'Generating up to %d recently updated pages list...' % nrecent

# Brose git log history and find recent commits
p = subprocess.Popen(['git', 'log',  '--name-status', '-%d' % nrecent], stdout=subprocess.PIPE, stderr=subprocess.STDOUT);
output = p.communicate()[0]
date = ['','','']
exclude = ['recent.rst', 'index.rst']
recorded = set()
recent = []
for line in output.splitlines():
  items = line.split()
  if len(items):
    if items[0] == 'Date:':
      date[0] = items[2]
      date[1] = items[3]
      date[2] = items[5]
    if items[0] in ['A', 'M'] and items[1].endswith('.rst') and \
      not items[1].startswith('blog') and items[1] not in exclude \
      and items[1] not in recorded:
      recorded.add (items[1])
      recent.append ((list(date), items[1]))

with open ('./recent.rst', 'w') as f:
  for page in recent[:nrecent]:
    date = page[0];
    name = page[1]
    tstr = date[0] + ' ' + date[1] + ' ' + date[2]
    parts = name[:-4].split('/')
    label = parts[0]
    for p in parts[1:]: label += '-'+p
    f.write ('\n')
    f.write ('* On %s :ref:`%s`\n' % (tstr, label))

# Previous version, below, was based on filesystem dates
'''
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
'''
