# -*- coding: utf-8 -*-
# @Author: LichAmnesia
# @Date:   2016-11-26 13:20:29
# @Last Modified by:   Lich_Amnesia
# @Last Modified time: 2016-11-30 20:59:35
# This is to deal with the comments and generate every day's comments file.

import datetime
import json
timeStamp = 1381419600
dateArray = datetime.datetime.utcfromtimestamp(timeStamp)
otherStyleTime = dateArray.strftime("%Y-%m-%d")
print(otherStyleTime)


# 创建每天的comments文件
def generateComments_date():
    cnt = 0
    with open('comments', 'r') as fileobject:
        cur_filename = ''
        file = None
        for line in fileobject:
            js = json.loads(line.replace('\n',''))
            time_stamp = js['created_utc']
            date_array = datetime.datetime.utcfromtimestamp(time_stamp)
            day = date_array.strftime("%Y-%m-%d")
            filename = 'comments_' + day + '.csv'
            if filename != cur_filename:
                if file:
                    file.close()
                cur_filename = filename
                file = open(cur_filename, 'w')
                file.write('day' + '\t' + 'created_utc' + '\t' + 'subreddit_id' + '\t' + 'parent_id' + '\t' + 'author' + '\t' + 'subreddit' + '\t' + 'link_id' + '\t' + 'id' + '\t' + 'retrieved_on' + '\t' + 'score' + '\n')
            else:
                file.write(day + '\t' + str(js['created_utc']) + '\t' + js['subreddit_id'] + '\t' + js['parent_id'] + '\t' + js['author'] + '\t' + js['subreddit'] + '\t' + js['link_id'] + '\t' + js['id'] + '\t' + str(js['retrieved_on']) + '\t' + str(js['score']) + '\n')
        

# 计算最多subreddit的comment数目
def countLargestReddit():
    cnt = 0
    dic_subreddit = {}
    with open('comments', 'r') as fileobject:
        cur_filename = ''
        file = None
        for line in fileobject:
            js = json.loads(line.replace('\n',''))
            if js['subreddit'] not in dic_subreddit:
                dic_subreddit[js['subreddit']] = 1
            else:
                dic_subreddit[js['subreddit']] += 1
    ans = sorted(dic_subreddit.items(), key=lambda x: x[1], reverse=True)
    print(ans[:10])


# 创建comment，根据subreddit进行筛选
def generateComments_subreddit_name(subredditlist=["politics", "GlobalOffensiveTrade"]):
    cnt = 0
    with open('comments', 'r') as fileobject:
        cur_filename = ''
        file = None
        for line in fileobject:
            js = json.loads(line.replace('\n',''))
            time_stamp = js['created_utc']
            date_array = datetime.datetime.utcfromtimestamp(time_stamp)
            day = date_array.strftime("%Y-%m-%d")
            filename = 'comments_subreddit_' + subredditlist[0] + '_' + subredditlist[1] + '.csv'
            if filename != cur_filename:
                if file:
                    file.close()
                cur_filename = filename
                file = open(cur_filename, 'w')
                file.write('day' + '\t' + 'created_utc' + '\t' + 'subreddit_id' + '\t' + 'parent_id' + '\t' + 'author' + '\t' + 'subreddit' + '\t' + 'link_id' + '\t' + 'id' + '\t' + 'retrieved_on' + '\t' + 'score' + '\n')
            else:
                if js['subreddit'] in subredditlist:
                    file.write(day + '\t' + str(js['created_utc']) + '\t' + js['subreddit_id'] + '\t' + js['parent_id'] + '\t' + js['author'] + '\t' + js['subreddit'] + '\t' + js['link_id'] + '\t' + js['id'] + '\t' + str(js['retrieved_on']) + '\t' + str(js['score']) + '\n')

def main():
    # countLargestReddit()
    generateComments_subreddit_name()

if __name__ == '__main__':
    main()
