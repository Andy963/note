#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : leetcode_046.py
# Author            : Andy
# Date              : 2022.08.15
# Last Modified Date: 2022.08.15
# Last Modified By  : Andy


class Solution:
    def permute(self, nums):
        n = len(nums)
        path = []
        result = []

        def find(index):
            if index == n:
                result.append(path[:])
                return

            for i in range(n):
                if nums[i] in path:
                    continue
                path.append(nums[i])
                find(index+1)
                path.pop()
        find(0)
        return result
