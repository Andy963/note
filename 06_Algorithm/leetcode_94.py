#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : leetcode_94.py
# Author            : Andy
# Date              : 2022.08.19
# Last Modified Date: 2022.08.19
# Last Modified By  : Andy


class Solution:
    def inorderTraversal(self, root):
        def finder(root):
            # 终止条件
            if not root:return
            # 左边节点
            finder(root.left)
            # 加上中间节点的值
            ans.append(root.val)
            # 加上右边节点的值
            finder(root.right)
        ans = []
        finder(root)
        return ans
