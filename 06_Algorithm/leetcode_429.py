#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : leetcode_429.py
# Author            : Andy
# Date              : 2022.08.21
# Last Modified Date: 2022.08.21
# Last Modified By  : Andy


class Solution:
    def levelOrder(self, root):
        result = []
        q = []
        if not root: return result

        q.append(root)

        while q:
            size = len(q)
            cur = []
            for i in range(size):
                node = q[0]
                del q[0]
                cur.append(node.val)
                for child in node.children:
                    q.append(child)
            result.append(cur)
        return result
