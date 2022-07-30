#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : leetcode_1248.py
# Author            : Andy
# Date              : 30.07.2022
# Last Modified Date: 30.07.2022
# Last Modified By  : Andy


class Solution:
    def numberOfSubarrays(self, nums, k):
        dic = {0:1}
        count, sums = 0, 0
        for i in range(len(nums)):
            nums[i] = nums[i] % 2
            sums += nums[i]
            if sums -k in dic:
                count += dic[sums-k]
            dic[sums] = dic.get(sums, 0) + 1
        return count
