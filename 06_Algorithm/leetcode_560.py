#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : leetcode_560.py
# Author            : Andy
# Date              : 30.07.2022
# Last Modified Date: 30.07.2022
# Last Modified By  : Andy


class Solution:
    def subarraySum(self, nums, k) :
        n = lens(nums)
        ans = 0 # 最终要返回的结果计数，初始化为0
        dic = {0:1} # 前面结果为0的子数组次数为1
        sum_i = 0 # 前缀和的值初始化为0 

        for i in range(n):
            # 前缀和，累加
            sum_i += nums[i]
            # 如果要找的部分前缀的值已经出现过，那么通过当前的前缀和与这部分前缀相减就可以得到这个k值，
            # 只需要将这部分前缀出现的次数加上即可,
            # 如果没有出现，继续统计，把当前的前缀和的值存入字典
            # 如果当前前缀和的值还没有出现，那么置为1，即首次出现
            if sum_i - k in dic:
                ans += dic.get(sum_i-k)
            dic[sum_i] = dic.get(sum_i,0) + 1
        return ans
