#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : leetcode_523.py
# Author            : Andy
# Date              : 31.07.2022
# Last Modified Date: 31.07.2022
# Last Modified By  : Andy


class Solution:
    def checkSubarraySum(self, nums, k):
        # 利用前缀和，如果两个间隔的前缀和与k取模的值相同，那么这两个前缀和中间的子数组
        # 的差值肯定就是k的整数倍，只需要记录前缀和的索引值就可以了,这里使用enumerate
        # 需要记录0，将其索引置为-1,来处理边界
        sums = 0
        hash = {0:-1}
        for i, val in enumerate(nums):
            sums += val
            if k:
                sums = sums % k
            if sums in hash:
                if i - hash.get(sums) >= 2:
                    return True
            else:
                hash[sums] = i
        return False
