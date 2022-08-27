#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : leetcode_869.py
# Author            : Andy
# Date              : 2022.08.27
# Last Modified Date: 2022.08.27
# Last Modified By  : Andy


"""
不管字符串怎么排列，排序后的数字均相同，那么只要2的n次方中产生的数字排列后有一个相同的就表示可以
"""


class Solution:
    def reorderPowerOfTwo(self,n):
        sn = sorted(str(n))
        for i in range(31):
            if sorted(str(2**i)) == sn:
                return True
        return False
