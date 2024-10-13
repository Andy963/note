#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : leetcode_684.py
# Author            : Andy
# Date              : 2022.08.22
# Last Modified Date: 2022.08.22
# Last Modified By  : Andy


class UnionSet:
    def __init_(self, n):
        self.root = [-1] * (n + 1)

    def find(self, node):
        while self.root[node] != -1:
            node = self.root[node]
        return node

    def connect(self, node1, node2):
        first_root, second_root = self.find(node1), self.find(node2)
        if first_root != second_root:
            self.root[first_root] = second_root

class Solution:
    def findRedundantConnection(self, edges):
        node_set = set()
        for edge in edges:
            node_set.add(node[0])
            node_set.add(node[1])
        us = UnionSet(len(node_set))

        for e in edges:
            first, second = us.find(e[0]), us.find(e[1])
            if first != second:
                us.connect(first, second)
            else:
                return e
