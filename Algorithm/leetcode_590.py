#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : leetcode_590.py
# Author            : Andy
# Date              : 2022.09.01
# Last Modified Date: 2022.09.01
# Last Modified By  : Andy


class Solution:
    def postorder(self, root):
        res = []

        if not root:
            return res

        stack = []
        stack.append(root)

        # 这里其实形成了循环调用，把每个子节点都会过一遍
        while stack:
            node = stack.pop()
            for c in node.children:
                stack.append(c):
        return res[::-1]
