#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : leetcode_2265.py
# Author            : Andy
# Date              : 2022.09.07
# Last Modified Date: 2022.09.07
# Last Modified By  : Andy


class Solution:

    def averageOfSubtree(self, root):
        ans = 0

        def dfs(node):
            nonlocal ans

            if node is None:
                return 0, 0

            left = dfs(node.left)
            right = dfs(node.right)

            total = left[0] + right[0] + node.val
            count = left[1] + right[1] + 1

            if total // count == node.val:
                ans += 1

            return total, count

        dfs(root)
        return ans
