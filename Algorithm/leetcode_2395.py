#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : leetcode_2395.py
# Author            : Andy
# Date              : 2022.09.14
# Last Modified Date: 2022.09.14
# Last Modified By  : Andy


class Solution:

    def findSubarrays(self, nums):
        n = len(nums)
        seen = set()
        for i in range(n - 1):
            s = nums[i] + nums[i + 1]
            if s in seen:
                return True

        return False
