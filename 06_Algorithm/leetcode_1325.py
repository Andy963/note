#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : leetcode_1325.py
# Author            : Andy
# Date              : 2022.09.16
# Last Modified Date: 2022.09.16
# Last Modified By  : Andy


class Solution:

    def removeLeafNodes(self, root, target):
        if root is None:
            return None

        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)

        if root.val == target and root.left is None and root.right is None:
            return None

        return root
