#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : leetcode_690.py
# Author            : Andy
# Date              : 2022.10.11
# Last Modified Date: 2022.10.11
# Last Modified By  : Andy

# 子元素的id可以通过subordinates获取到，直接遍历就行，
# 前提通过id获取到employee本身


class Solution:

    def getImportance(self, employees, id):
        total = 0
        stack = [id]
        hashmap = {}
        for e in employees:
            hashmap[e.id] = e

        while stack:
            cur = stack.pop()
            total += cur.importance

            for sub in subordinates:
                stack.append(sub)

        return total
