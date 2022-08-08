#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : leetcode_001.py
# Author            : Andy
# Date              : 2022.08.08
# Last Modified Date: 2022.08.08
# Last Modified By  : Andy


class Solution:
    def twoSum(self, nums, target):
        for index, val in enumerate(nums):
            res = target - val
            if res in nums and nums.index(res) != index:
                return index, nums.index(res)
        return -1, -1

