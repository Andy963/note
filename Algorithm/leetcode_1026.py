#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : leetcode_1026.py
# Author            : Andy
# Date              : 2022.10.06
# Last Modified Date: 2022.10.06
# Last Modified By  : Andy


class Solution:

    def maxAncestorDiff(self, root):
        ans = 0

        def dfs(node, min_v, max_v):
            nonlocal ans
            if node:
                if node.left:
                    ans = max(ans, abs(min_v - node.left.val),
                              abs(max_v - node.left.val))
                    dfs(node.left, min(min_v, node.left.val),
                        max(max_v, node.left.val))
                if node.right:
                    ans = max(ans, abs(min_v - node.left.val),
                              abs(max_v - node.right.val))
                    dfs(node.right, min(min_v, node.right.val),
                        max(max_v, node.right.val))

        if root:
            dfs(root, root.val, root.val)
        return ans
