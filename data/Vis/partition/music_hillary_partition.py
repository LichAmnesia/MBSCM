# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Date:   2016-11-30 22:30:39
# @Last Modified by:   Lich_Amnesia
# @Last Modified time: 2016-11-30 22:46:23
# @Email: shen.huang@colorado.edu


with open('comments_subreddit_Music_hillaryclinton_3_metadata.txt', 'r') as f:
	for line in f:
		a, b = line.split()
		print('{{"id": \"{0}\", "group": {1}}},'.format(a, b))

with open('comments_subreddit_Music_hillaryclinton_3.txt', 'r') as f:
	for line in f:
		a, b = line.split()
		print('{{\"source\": \"{0}\", \"target\": \"{1}\", \"value\": {2}}},'.format(a, b, '1'))



# g = [[], [2, 3, 5, 4, 7, 9, 10, 11],[12, 6, 8, 1]]
# for i in range(len(g)):
# 	for j in g[i]:
# 		


