#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : leetcode_2396.py
# Author            : Andy
# Date              : 2022.09.14
# Last Modified Date: 2022.09.14
# Last Modified By  : Andy


class Solution:

    def isStrictlyPalindromic(self, n):

        def convert(n, b):
            rs = 0
            while n:
                rs += rs * b + n % b
                n //= b
            return rs

        for i in range(2, n - 1):
            rs = convert(n, i)
            if rs != n:
                return False

        return True
