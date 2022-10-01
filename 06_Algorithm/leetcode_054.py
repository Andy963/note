#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : leetcode_054.py
# Author            : Andy
# Date              : 2022.10.01
# Last Modified Date: 2022.10.01
# Last Modified By  : Andy


# 尝试优先，后序遍历，先找到最右侧的节点
class Solution:

    def convertBST(self, root):
        total = 0

        def dfs(node):
            nonlocal total

            if node is None:
                return

            dfs(node.right)
            total += node.val
            node.val = total
            dfs(node.left)
            return node

    return dfs(root)
