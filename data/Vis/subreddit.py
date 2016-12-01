# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Date:   2016-11-30 21:13:48
# @Last Modified by:   Lich_Amnesia
# @Last Modified time: 2016-11-30 21:43:19
# @Email: shen.huang@colorado.edu


with open('subreddit.data', 'r') as f:
	cnt = 0
	for line in f:
		a, b = line.split()
		a = a.replace(',', '')
		cnt += 1
		if cnt % 2:
			print(a, end=", ")
		else:
			print(a[0]+'\\n'+a[1:], end=", ")
		# print(b, end=", ")
		