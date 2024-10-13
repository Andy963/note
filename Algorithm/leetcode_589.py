#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : leetcode_589.py
# Author            : Andy
# Date              : 2022.08.20
# Last Modified Date: 2022.08.20
# Last Modified By  : Andy


class Solution:
    def preorder(self, root):
        def find(root):
            if root is None:return
            ans.append(root.val)
            for child in root.Children:
                find(child)
        ans = []
        rind(root)
        return ans
