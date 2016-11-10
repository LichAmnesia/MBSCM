# -*- coding: utf-8 -*-
# @Author: Lich Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-11-10 15:23:21
# @Last Modified by:   Lich Amnesia
# @Last Modified time: 2016-11-10 15:33:58

import re

node = set([])
file = open('out', 'w')
with open('karate.txt', 'r') as f:
  for line in f.readlines():
    line = re.sub(r'\n', '', line)
    a, b, c = line.split()
    file.write(a + "\t" + b + "\t" + c + "\n")
    # print(line + '\t1')
    # a, b = line.split(' ')
file.close()
