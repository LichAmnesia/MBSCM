# -*- coding: utf-8 -*-
# @Author: LichAmnesia
# @Date:   2016-11-26 13:20:29
# @Last Modified by:   Lich Amnesia
# @Last Modified time: 2016-11-30 17:37:12
# This is to deal with the comments and generate every day's comments file.

import datetime
import json
import pandas as pd
import collections

# generate a graph file


def read_label_write_label_file():
    labels_data = pd.read_csv('moderators_subreddit.csv', delimiter='\t')
    moderators_map = {}
    subreddit_map = {}
    for moderator in labels_data['moderators']:
        if moderator not in moderators_map:
            moderators_map[moderator] = len(moderators_map) + 1

    for subreddit in labels_data['subreddit']:
        if subreddit not in subreddit_map:
            subreddit_map[subreddit] = len(subreddit_map) + 1
    return labels_data, moderators_map, subreddit_map

def read_edge_date(filename='comments_2016-09-01.csv'):
    edge_data = pd.read_csv(filename, delimiter='\t')
    edge_map = collections.defaultdict(list)
    for line_num in range(len(edge_data)):
        line = edge_data.loc[line_num]
        # print(line['author'])
        edge_map[line['link_id']].append(moderators_map[line['author']])

    summary = 0
    edge_filename = filename.split('.')[0]
    label_filename = edge_filename + '_metadata' + '.txt'
    edge_filename = edge_filename + '.txt'
    edge_file = open(edge_filename, 'w')
    label_file = open(label_filename, 'w')

    # The node in the edge_list
    has_set = set([])
    for i in edge_map:
        if len(edge_map[i]) > 1:
            for j in range(len(edge_map[i]) - 1):
                if edge_map[i][j + 1] != edge_map[i][j]:
                    has_set.add(edge_map[i][j + 1])
                    has_set.add(edge_map[i][j])
                    edge_file.write(str(edge_map[i][j + 1]) + ' ' + str(edge_map[i][j]) + '\n')
    edge_file.close()
    print(has_set)

    for line_num in range(len(labels_data)):
        line = labels_data.loc[line_num]
        if moderators_map[line['moderators']] in has_set:
            label_file.write(str(moderators_map[line['moderators']]) + ' ' + str(subreddit_map[line['subreddit']]) + '\n')
    label_file.close()

# 只运算两个subreddit的, 然后对一个linkid是一个点
def read_edge_subreddit(filename='comments_2016-09-01.csv'):
    # labels_data = pd.read_csv('moderators_subreddit.csv', delimiter='\t')
    # moderators_map = {}
    # subreddit_map = {}
    # for moderator in labels_data['moderators']:
    #     if moderator not in moderators_map:
    #         moderators_map[moderator] = len(moderators_map) + 1

    # for subreddit in labels_data['subreddit']:
    #     if subreddit not in subreddit_map:
    #         subreddit_map[subreddit] = len(subreddit_map) + 1
    # return labels_data, moderators_map, subreddit_map

    # 读取图，然后把author的评论顺序记下来。同一个author对不同link_id的评论，就是一条边
    edge_data = pd.read_csv(filename, delimiter='\t')
    edge_map = collections.defaultdict(list)
    author_map = collections.defaultdict(list)
    link_id_map = {}
    node_label_map = {}
    for line_num in range(len(edge_data)):
        line = edge_data.loc[line_num]
        # print(line['author'])
        if line['link_id'] not in link_id_map:
            link_id_map[line['link_id']] = len(link_id_map) + 1
        author_map[line['author']].append(link_id_map[line['link_id']])
        if line['subreddit'] not in node_label_map:
            node_label_map[line['subreddit']] = len(node_label_map) + 1

    print(node_label_map)
    summary = 0
    edge_filename = filename.split('.')[0]
    label_filename = edge_filename + '_metadata' + '.txt'
    edge_filename = edge_filename + '.txt'
    edge_file = open(edge_filename, 'w')
    label_file = open(label_filename, 'w')

    # The node in the edge_list
    has_set = set([])
    for i in author_map:
        if len(author_map[i]) > 1:
            for j in range(len(author_map[i]) - 1):
                if author_map[i][j + 1] != author_map[i][j]:
                    has_set.add(author_map[i][j + 1])
                    has_set.add(author_map[i][j])
                    edge_file.write(str(author_map[i][j]) + ' ' + str(author_map[i][j + 1]) + '\n')
    edge_file.close()
    print(has_set, len(has_set))

    has_wirte = set([])
    for line_num in range(len(edge_data)):
        line = edge_data.loc[line_num]
        node = link_id_map[line['link_id']]
        if node in has_set and node not in has_wirte:
            has_wirte.add(node)
            label_file.write(str(node) + ' ' + str(node_label_map[line['subreddit']]) + '\n')
    label_file.close()



# labels_data, moderators_map, subreddit_map = read_label_write_label_file()
def main():
    # read_edge_date()
    read_edge_subreddit(filename='comments_subreddit_politics_GlobalOffensive_Trade_1.csv')

if __name__ == '__main__':
    main()