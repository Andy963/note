#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : leetcode_1315.py
# Author            : Andy
# Date              : 2022.09.08
# Last Modified Date: 2022.09.08
# Last Modified By  : Andy


class Solution:

    def sumEvenGrandparent(self, root):
        ans = 0

        def dfs(node):
            nonlocal ans

            if node is None:
                return 0

            if node.left is not None:
                if node.left.left is not None:
                    ans += node.left.left.val
                if node.left.right is not None:
                    ans += node.left.right.val

            if node.right is not None:
                if node.right.left is not None:
                    ans += node.right.left.val

                if node.right.right is not None:
                    ans += node.right.right.val

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ans
