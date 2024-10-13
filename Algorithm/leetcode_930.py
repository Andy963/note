#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : leetcode_930.py
# Author            : Andy
# Date              : 30.07.2022
# Last Modified Date: 30.07.2022
# Last Modified By  : Andy

# 主体思路：利用前缀和，并统计前缀和中每个和出现的次数
# 通过sums-goal 的次数来得到所有可能的结果,即可以通过当前
# sums 减去前面每次的 sums-goal可以得到goal

class Solution:
    def numSubarraysWithSum(self, nums, goal):
        count, sums = 0, 0
        dic = {0:1}
        for i in range(len(nums)):
            sums += nums[i]
            if sums - goal in dic:
                count += dic.get(sums-goal)
            dic[sums] = dic.get(sums, 0) + 1
        return count
