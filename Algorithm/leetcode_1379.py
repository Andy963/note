#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : leetcode_1379.py
# Author            : Andy
# Date              : 2022.09.06
# Last Modified Date: 2022.09.06
# Last Modified By  : Andy


class Solution:

    def getTargetCopy(self, original, cloned, target):
        tar = TreeNode()

        def dfs(root):
            nonlocal tar
            # 递归终止条件
            if not root:
                return

            if root.val == target.val:
                tar = root  # 一定要是root, 而非target, root才是cloned中的节点
                return

            # 这里可以不用判断，即使节点为空，dfs也会终止
            dfs(root.left)
            dfs(root.right)

        dfs(cloned)
        return tar
