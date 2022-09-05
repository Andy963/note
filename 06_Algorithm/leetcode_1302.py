#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : leetcode_1302.py
# Author            : Andy
# Date              : 2022.09.05
# Last Modified Date: 2022.09.05
# Last Modified By  : Andy


class Solution:

    def deepestLeavesSum(self, root) -> int:
        stack = []
        stack.append([root])
        ans = root.val

        while stack:
            # 一个nodes表示一层节点
            nodes = stack.pop()
            # level记录当前层
            level = []
            for node in nodes:
                if node.left:
                    level.append(node.left)

                if node.right:
                    level.append(node.right)

            if level:
                ans = sum([l.val for l in level])
                stack.append(level)

        return ans
