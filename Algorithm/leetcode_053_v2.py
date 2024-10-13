#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : leetcode_053_v2.py
# Author            : Andy
# Date              : 03.08.2022
# Last Modified Date: 03.08.2022
# Last Modified By  : Andy

# 这种方式比较特殊，因为它只考虑前面的数字大于0的情况，因为如果前面的数字小于0，那么只会越加越小
# 同时它在原数组上进行修改，最后通过max来直接求最大值

class Solution:
    def maxSubArrary(self, nums):
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)
