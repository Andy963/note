#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : leetcode_lcp44.py
# Author            : Andy
# Date              : 2022.09.17
# Last Modified Date: 2022.09.17
# Last Modified By  : Andy


class Solution:

    def numColor(self, root):
        ans = []

        def dfs(node):
            if node is None:
                return

            if node.val not in ans:
                ans.append(node.val)

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return len(ans)
