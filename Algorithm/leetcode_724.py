#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : leetcode_724.py
# Author            : Andy
# Date              : 31.07.2022
# Last Modified Date: 31.07.2022
# Last Modified By  : Andy

# 主体思路就是当前索引左边的前缀和，与总值减去当前前缀和
# 两者相等时返回当前索引即可

class Solution:
    def pivotIndex(self, nums):
        total = sum(nums)
        sums = 0
        for i in range(len(nums)):
            sums += nums[i]
            if sums - nums[i] == total - sums:
                return i
        return -1
