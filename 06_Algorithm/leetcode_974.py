#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : leetcode_974.py
# Author            : Andy
# Date              : 01.08.2022
# Last Modified Date: 01.08.2022
# Last Modified By  : Andy

# 主体思路：每一种子数组都可以通过前缀和想减得到，而能被k整除，则要求两个子组数的余数相同
# 记录余数出现次数，当次数大于1时，可以通过组合的方式得到所有可能的子数组的组合

class Solution:
    def subarraysDivByK(self, nums, k):
        count, presum = 0, 0
        dic = {0:1} # 记录前缀和出现的次数
        for i in range(len(nums)):
            presum += nums[i]
            res = (presum % k + k) % k
            dic[res] = dic.get(res, 0) + 1

        for _, v in dic.items():
            if v > 1:
                count += (v -1) * v / 2 # 排列组合
        return count
