#!/usr/bin/env python

import os
import pickle
import collections

class Indexer:
    def __init__(self, dir):
        self.__inv_index = collections.defaultdict(set)
        self.__start_dir = dir

    def start(self, ignore=''):
        print "staring index directories..."
        ignore_set = set(ignore.split(','))
        print 'ignore set:%s' % ignore_set
        for root, dir, files in os.walk(self.__start_dir):
            for item in dir:
                if item in ignore_set:
                    continue
                self.__inv_index[item].add(os.path.abspath(root))
        print "end of indexing, total directories:%d" % len(self.__inv_index)

    def dump(self, file="./inder.dt"):
        pickle.dump(self, open(file, "wb"))

    def get(self, name):
        if not name or name not in self.__inv_index:
            return []
        return list(self.__inv_index[name])

    def update(self, dir_list):
        for item in dir_list:
            self.__inv_index[os.path.basename(item)].append(item)


if __name__ == '__main__':
    import sys
    index = Indexer(sys.argv[1])
    index.dump("dt")
    input_str = raw_input("Input the directory name where you want to go:")
    for item in index.get(input_str):
        print item + '/' + input_str
