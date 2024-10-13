#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : leetcode_0403.py
# Author            : Andy
# Date              : 2022.10.08
# Last Modified Date: 2022.10.08
# Last Modified By  : Andy

# 广度优先，层序遍历


class Solution:

    def listOfDepth(self, tree):
        stack = [tree]
        ans = []
        while stack:
            next_level = []
            node = ListNode()
            head = node
            for st in stack:
                node.next = ListNode(st.val)
                node = node.next

                if st.left:
                    next_level.append(st.left)

                if st.right:
                    next_level.append(st.right)
            ans.append(head.next)
            stack = next_level
        return ans
