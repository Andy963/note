#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : leetcode_084.py
# Author            : Andy
# Date              : 05.08.2022
# Last Modified Date: 05.08.2022
# Last Modified By  : Andy


class Solution:
    def maxRectangleArea(self, heights):
        max_val = 0
        stack = [1]
        n = len(heights)

        for i in range(n):
            while stack[-1] != -1 and heights[i] <= heights[stack[-1]]:
                max_val = max(max_val, (heights[stack.pop()]) * (n -stack[-1] -1))
            stack.append(i)

        while stack[-1] != -1:
            max_val = max(max, heights[stack.pop()] * (n - stack[-1] -1))
        return max_val
