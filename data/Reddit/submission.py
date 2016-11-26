# -*- coding: utf-8 -*-
# @Author: Lich_
# @Date:   2016-11-26 18:14:52
# @Last Modified by:   LichAmnesia
# @Last Modified time: 2016-11-26 13:49:17

import json
import os


# generate the moderators from moderators file. the output is the moderators_subreddit file
def getmoderators():
    with open('E:\\Workspace\\NetworkData\\moderators') as fileobject:
        for line in fileobject:
            js = json.loads(line.replace('\n',''))
            moderators = js['moderators']
            for moderator in moderators:
                print(moderator['name'], js['subreddit'])

moderators_set = set([])
with open('moderators_subreddit') as fileobject:
    for line in fileobject:
        moderators_set.add(line.split()[0])


# This is to generate the comments
# the line of the RC 2016-09 is 67,000,000 lines
def getComments()
    cnt = 0
    with open('E:\\Workspace\\NetworkData\\RC_2016-09', 'r') as fileobject:
        with open('comments', 'w+') as file:
            for line in fileobject:
                js = json.loads(line.replace('\n',''))
                author = js['author']
                if author in moderators_set:
                    del js['body']
                    file.write(json.dumps(js) + '\n')
                cnt += 1
                if cnt % 1000000 == 0:
                    file.flush()
                    os.fsync(file)
                    print(cnt)
    file.close()