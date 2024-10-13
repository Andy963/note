#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : leetcode_026.py
# Author            : Andy
# Date              : 22.07.2022
# Last Modified Date: 22.07.2022
# Last Modified By  : Andy

# 主体思路：
# 考虑什么样的元素需要留下来：
# 只有和前面一个元素不同的元素需要留下来

# 考虑边界，即i与i-1可能存在越界的问题
# 但是第一个元素肯定是要放进去的，所以索引为0单独考虑


class Solution:
    def removeDuplicates(self, nums: List[int]) ->int:
        n = 0
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                nums[n] = num[i]
                n += 1
        return n
