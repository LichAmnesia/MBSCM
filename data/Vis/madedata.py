# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Date:   2016-11-30 21:41:16
# @Last Modified by:   Lich_Amnesia
# @Last Modified time: 2016-11-30 21:46:25
# @Email: shen.huang@colorado.edu


s = "(1,1.),(2,1.),(3,1.34),(4,1.34),(5,0.),(6,-0.34),(7,-0.34),(8,-1.),(9,-1.),(10,-1.),(11,-1.),(12,1.)"
s = s.replace('(', '')
s = s.replace(')', '')
s = s.split(',')
a = []
b = []
for i in range(len(s)):
	if i % 2 == 0:
		a.append(s[i])
	else:
		b.append(float(s[i]))

print(a)
print(b)