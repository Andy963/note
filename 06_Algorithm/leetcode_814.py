#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : leetcode_814.py
# Author            : Andy
# Date              : 2022.09.19
# Last Modified Date: 2022.09.19
# Last Modified By  : Andy


class Solution:

    def pruneTree(self, root):

        def dfs(node):
            if node is None:
                return

            node.left = dfs(node.left)
            node.right = dfs(node.right)

            if node.left is None and node.right is None:
                # 有数字1的节点返回，如果没有则消除
                return node if node.val == 1 else None

            # 非叶子节点
            return node

        return dfs(root)
