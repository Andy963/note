#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : leetcode_669.py
# Author            : Andy
# Date              : 2022.09.20
# Last Modified Date: 2022.09.20
# Last Modified By  : Andy


class Solution:

    def trimBST(self, root, low, high):
        if root is None:
            return
        # bst 左树小于root,小于右树
        # 所以当值比low小时，那就遍历右树，因为左树的子树比左树节点更小
        if root.val < low:
            return self.trimBST(root.right, low, high)

        if root.val > high:
            return self.trimBST(root.left, low, high)

        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)

        return root
