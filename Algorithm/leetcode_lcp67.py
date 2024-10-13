#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : leetcode_lcp67.py
# Author            : Andy
# Date              : 2022.10.12
# Last Modified Date: 2022.10.12
# Last Modified By  : Andy


class Solution:

    def expandBinaryTree(self, root):
        if not root:
            return

        def dfs(node):
            if not node:
                return

            if node.left:
                node.left = TreeNode(-1, left=node.left)
                dfs(node.left.left)

            if node.right:
                node.right = TreeNode(-1, right=node.right)
                dfs(node.right.right)

            return node

        return dfs(root)
