#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : leetcode_1305.py
# Author            : Andy
# Date              : 2022.09.21
# Last Modified Date: 2022.09.21
# Last Modified By  : Andy

# 这题直接排序竟然能过，但没想到更好的能在递归时排序的方法


class Solution:

    def getAllElements(self, root1, root2) -> List[int]:
        ans = []

        def dfs(node):
            if node is None:
                return

            dfs(node.left)
            ans.append(node.val)
            dfs(node.right)

        dfs(root1)
        dfs(root2)

        ans.sort()
        return ans
