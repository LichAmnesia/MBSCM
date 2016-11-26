# -*- coding: utf-8 -*-
# @Author: LichAmnesia
# @Date:   2016-11-26 13:20:29
# @Last Modified by:   LichAmnesia
# @Last Modified time: 2016-11-26 13:47:08
# This is to deal with the comments and generate every day's comments file.

import datetime
import json
timeStamp = 1381419600
dateArray = datetime.datetime.utcfromtimestamp(timeStamp)
otherStyleTime = dateArray.strftime("%Y-%m-%d")
print(otherStyleTime)

cnt = 0
with open('comments', 'r') as fileobject:
    cur_filename = ''
    file = None
    for line in fileobject:
        js = json.loads(line.replace('\n',''))
        time_stamp = js['created_utc']
        date_array = datetime.datetime.utcfromtimestamp(time_stamp)
        day = date_array.strftime("%Y-%m-%d")
        filename = 'comments_' + day
        if filename != cur_filename:
            if file:
                file.close()
            cur_filename = filename
            file = open(cur_filename, 'w')
            file.write('day' + '\t' + 'created_utc' + '\t' + 'subreddit_id' + '\t' + 'parent_id' + '\t' + 'author' + '\t' + 'subreddit' + '\t' + 'link_id' + '\t' + 'id' + '\t' + 'retrieved_on' + '\t' + 'score' + '\n')
        else:
            file.write(day + '\t' + str(js['created_utc']) + '\t' + js['subreddit_id'] + '\t' + js['parent_id'] + '\t' + js['author'] + '\t' + js['subreddit'] + '\t' + js['link_id'] + '\t' + js['id'] + '\t' + str(js['retrieved_on']) + '\t' + str(js['score']) + '\n')
        


