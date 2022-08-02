#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : leetcode_053.py
# Author            : Andy
# Date              : 02.08.2022
# Last Modified Date: 02.08.2022
# Last Modified By  : Andy


class Solution:
    def maxSubArray(self, nums):
        max_val = float(-inf)
        pre = 0
        for i in range(len(nums)):
            pre += nums[i]
            if pre > max_val:
                max_val = pre

            if pre < 0:
                pre = 0
        return max_val
