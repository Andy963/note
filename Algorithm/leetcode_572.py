#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : leetcode_572.py
# Author            : Andy
# Date              : 2022.08.25
# Last Modified Date: 2022.08.25
# Last Modified By  : Andy


class Solution:

    def isSubtree(self, root, subtree):

        def isSame(left, right):
            if not left and not right: return True

            if not left or not right: return False

            return left.val == right.val and isSame(
                left.left, right.left) and isSame(left.rifht, right.right)

        if not root and not subtree: return True

        if not root or not subtree: return False

        return isSame(root, subtree) or isSubtree(
            root.left, subtree) or isSubtree(root.right, subtree)
