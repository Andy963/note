#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : leetcode_045.py
# Author            : Andy
# Date              : 2022.09.25
# Last Modified Date: 2022.09.25
# Last Modified By  : Andy


class Solution:

    def findBottomLeftVal(self, root):

        def bfs(node):
            if node is None:
                return None

            stack = [node]

            while stack:
                level = []
                next_level = []
                for s in stack:
                    level.append(s)

                    if s.left:
                        next_level.append(s.left)

                    if s.right:
                        next_level.append(s.right)

                if len(next_level) == 0:
                    return level[0].val

                stack = []
                stack.extend(next_level)

        return bfs(root)
