#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : leetcode_283.py
# Author            : Andy
# Date              : 23.07.2022
# Last Modified Date: 23.07.2022
# Last Modified By  : Andy


# 主体思路：将非零的元素留下，然后在末尾补零
# 什么样的元素要留下？判断是否等于0即可

def moveZeros(nums:list):
    n = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[n] = nums[i]
            n += 1
    while n < len(nums):
        nums[n] = 0
        n += 1

