#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : leetcode_1448.py
# Author            : Andy
# Date              : 2022.09.02
# Last Modified Date: 2022.09.02
# Last Modified By  : Andy


class Solution:

    def goodNodes(self, root):

        def dfs(node, largest):
            if not node:
                return

            if node.val >= largest:
                self.count += 1

            largest = max(largest, node.val)

            dfs(node.left, largest)
            dfs(node.right, largest)

        self.count = 0
        dfs(root, root.val)
        return self.count
