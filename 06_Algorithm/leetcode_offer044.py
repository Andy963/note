#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : leetcode_offer044.py
# Author            : Andy
# Date              : 2022.10.11
# Last Modified Date: 2022.10.11
# Last Modified By  : Andy


# 典型的层序遍历，bfs
class Solution:

    def largestValues(self, root):
        if not root:
            return []

        stack = [root]
        ans = []

        while stack:
            cur_level = []
            next_level = []
            size = len(stack)
            while size:
                cur = stack.pop()
                cur_level.append(cur.val)
                if cur.left:
                    next_level.append(cur.left)
                if cur.right:
                    next_level.append(cur.right)
                size -= 1
            ans.append(max(cur_level))
            stack = next_level
        return ans
