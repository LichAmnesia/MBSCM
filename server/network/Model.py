# @Author: Lich_Amnesia
# @Date:   2016-11-30T00:28:22-07:00
# @Email:  Shen.Huang@Colorado.Edu
# @Last modified by:   Lich_Amnesia
# @Last modified time: 2016-11-30T00:32:52-07:00


import networkx as nx

class Model(object):
    def __init__(self, filename):
        if not filename:
            print("no file")
            return
        with open(filename, 'r') as f:
            for line in f.read
