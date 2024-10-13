#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : leetcode_053_v1.py
# Author            : Andy
# Date              : 02.08.2022
# Last Modified Date: 02.08.2022
# Last Modified By  : Andy


class Solution:
    def maxSubArray(self, nums):
        dp = [0] * len(nums)
        dp[0] = nums[0]
        result = -10001
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
            result = max(dp[i], result)
    return result
