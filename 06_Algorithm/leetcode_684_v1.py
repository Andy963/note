#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : leetcode_684_v1.py
# Author            : Andy
# Date              : 2022.08.23
# Last Modified Date: 2022.08.23
# Last Modified By  : Andy

# 题解链接：
# https://leetcode.cn/problems/number-of-provinces/solution/python-duo-tu-xiang-jie-bing-cha-ji-by-m-vjdr/


class UnionFind:
    def __init__(self, size):
        # 记录父节点，初始化时为None
        self.father = {i:None for i in range(size)}

    def find(self, x, y):
        root = x
        while self.father[x] != None:
            root = self.father[root]

        # 路径压缩
        while x != root:
            origin_father = self.father[x]
            self.father[x] = root
            x = origin_father
        return root


    def merge(self, x, y):
        root_x, root_y = self.find(x), self.find(y)

        if root_x != root_y:
            self.father[root_x] = root_y

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)


    def add(self, x, y):
        if x not in self.father:
            self.father[x] = None

class Solution:
    def findRedundantConnection(self, edges):
        uf = UnionFind(len(edges))
        for x, y in edges:
            if uf.is_connected(x, y):
                return [x, y]
            uf.merge(x, y)
        return [None, None]
