# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Date:   2016-11-30 22:30:39
# @Last Modified by:   Lich_Amnesia
# @Last Modified time: 2016-11-30 22:40:21
# @Email: shen.huang@colorado.edu


s = [(1,2),(1,3),(1,4),(1,5),(1,6),
                  (2,1),(2,3),(2,4),(2,5),(3,5),(5,12),(12,5),(12,2),(12,7),(7,12),(6,2),(6,7),
                  (7,2),(7,6),
                  (8,2),(8,6),(8,9),(8,10),(11,8),(11,10),(10,11),
                  (9,8),(9,6),(9,7),(9,10)]

for i in range(len(s)):
	a, b = s[i]
	# print('{{\"source\": {},'.format(str(a)))
	print('{{\"source\": \"{0}\", \"target\": \"{1}\", \"value\": {2}}},'.format(str(a), str(b), '1'))

g = [[], [2, 3, 5, 4, 7, 9, 10, 11],[12, 6, 8, 1]]
for i in range(len(g)):
	for j in g[i]:
		print('{{"id": \"{0}\", "group": {1}}},'.format(str(j), str(i)))


