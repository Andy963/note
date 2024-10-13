#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : leetcode_1457.py
# Author            : Andy
# Date              : 2022.10.13
# Last Modified Date: 2022.10.13
# Last Modified By  : Andy


class Solution:

    def pseudoPalindromicPaths(self, root):
        ans = 0

        def dfs(node, path):
            nonlocal ans

            if node is None:
                return

            dic = path.copy()
            dic[node.val] += 1

            if not node.left and not node.right:
                if sum([val % 2 == 1 for val in dic.values()]) <= 1:
                    ans += 1
                    return ans

            dfs(node.left, dic)
            dfs(node.right, dic)

        dfs(root, collections.defaultdict(int))
        return ans
