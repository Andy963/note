#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : leetcode_070.py
# Author            : Andy
# Date              : 03.08.2022
# Last Modified Date: 03.08.2022
# Last Modified By  : Andy

# 主体思路：n级时，可以由最后走一步与n-1步时的可能性相加
# n=0时1，n=1时也是1，作业递归的终止条件#TODO 这里不知道有没有记错
# 经测试可以通过@functools.cache()的方式来缓存数据，缩短递归时间
class Solution:
    def climbStairs(self, n):
        f = [0] * (n+1)
        f[0] = f[1] = 1

        if n < 2:
            return 1
        for i in range(2, n+1):
            f[i] = f[i-1] + f[i-2]
        return f[n]
