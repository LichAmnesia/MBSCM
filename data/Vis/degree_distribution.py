# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Date:   2016-11-30 22:02:11
# @Last Modified by:   Lich_Amnesia
# @Last Modified time: 2016-11-30 22:08:58
# @Email: shen.huang@colorado.edu


dic = {}
with open('comments_subreddit_Music_hillaryclinton_3.txt', 'r') as f:
	for line in f:
		a, b = line.split()
		a, b = int(a), int(b)
		if a in dic:
			dic[a] += 1
		else:
			dic[a] = 1
		if b in dic:
			dic[b] += 1
		else:
			dic[b] = 1

ans = [0] * 24
for i in dic:
	ans[dic[i]] += 1
res = []
for i in range(len(ans)):
	res.append(str(i))
print(ans)
print(res)