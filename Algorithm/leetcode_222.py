#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : leetcode_222.py
# Author            : Andy
# Date              : 2022.09.24
# Last Modified Date: 2022.09.24
# Last Modified By  : Andy


class Solution:

    def countNodes(self, root):
        count = 0
        if root is None:
            return count

        def dfs(node):
            nonlocal count
            if node is None:
                return

            if node is not None:
                count += 1

                dfs(node.left)
                dfs(node.right)

        dfs(root)
        return count
