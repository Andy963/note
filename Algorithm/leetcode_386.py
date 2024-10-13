#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : leetcode_386.py
# Author            : Andy
# Date              : 2022.09.10
# Last Modified Date: 2022.09.10
# Last Modified By  : Andy


class Solution:

    def lexicalOrder(n):
        res = []

        def dfs(cur, n):
            if cur > n:
                return

            res.append(cur)
            for i in range(10):
                next_n = cur * 10 + i
                if next_n > n:
                    continue

                dfs(next_n)

        for i in range(1, 10):
            dfs(i, n)

        return res
