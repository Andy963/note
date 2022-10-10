#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : leetcode_1161.py
# Author            : Andy
# Date              : 2022.10.10
# Last Modified Date: 2022.10.10
# Last Modified By  : Andy


class Solution:

    def maxLevelSum(self, root) -> int:
        if not root:
            return

        stack = [root]
        ans = {"max_val": -10001, "level": []}
        level = 0

        while stack:
            size = len(stack)
            level += 1
            cur_total = 0
            next_level = []

            while size:

                cur = stack.pop()
                cur_total += cur.val

                if cur.left:
                    next_level.append(cur.left)
                if cur.right:
                    next_level.append(cur.right)
                size -= 1

            if cur_total > ans['max_val']:
                ans['max_val'] = cur_total
                ans['level'] = [level]
            elif cur_total == ans['max_val']
                ans['level'].append(level)
        return min(ans['level'])
