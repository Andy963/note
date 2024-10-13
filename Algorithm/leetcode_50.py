#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : leetcode_50.py
# Author            : Andy
# Date              : 2022.08.18
# Last Modified Date: 2022.08.18
# Last Modified By  : Andy


class Solution:
    def myPow(self, x, n):
        if n == 0:return 1

        if n < 0:
            return 1 / self.myPow(x, -n)

        if n % 2 != 0:
            return x * self.myPow(x, n-1)
        else:
            return self.myPow(x*x, n/2)
