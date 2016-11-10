import re

with open('HVR_5.txt', 'r') as f:
  for line in f.readlines():
    line = re.sub(r',', ' ', line)
    print(line),    