#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : leetcode_226.py
# Author            : Andy
# Date              : 2022.08.17
# Last Modified Date: 2022.08.17
# Last Modified By  : Andy


class Solution:
    def invertTree(self, root):
        # 终止条件
        if root == None:
            return 
        # 每个节点交换左右节点
        root.left, root.right = root.right, root.left
        # 对节点的左，右节点均做此操作
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

