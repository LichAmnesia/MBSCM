# -*- coding: utf-8 -*-
# @Author: LichAmnesia
# @Date:   2016-11-26 13:20:29
# @Last Modified by:   Lich_Amnesia
# @Last Modified time: 2016-11-30 21:06:17
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

# 只运算两个subreddit的
def read_edge_date2(filename='comments_2016-09-01.csv'):
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



labels_data, moderators_map, subreddit_map = read_label_write_label_file()
def main():
    # read_edge_date()
    read_edge_date(filename='comments_subreddit_politics_GlobalOffensiveTrade.csv')

if __name__ == '__main__':
    main()