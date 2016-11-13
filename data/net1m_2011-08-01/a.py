import re

node = set([])
with open('net1m_2011-08-01.txt', 'r') as f:
  for line in f.readlines():
    line = re.sub(r'\n', '', line)
    a, b = line.split(' ')
    node.add(a)
    node.add(b)

with open('net1m_2011-08-01_metadata.txt', 'r') as f:
  for line in f.readlines():
    a, b = line.split(' ')
    if a not in node:
      continue
    print(str(a) + ' ' + str(b)),
# print(node)
# print(len(node))