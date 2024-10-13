#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : leetcode_326.py
# Author            : Andy
# Date              : 2022.08.26
# Last Modified Date: 2022.08.26
# Last Modified By  : Andy


class Solution:

    def isPowerOfThree(self, n):
        x = 1
        while x < n:
            x = x * 3
        return x == n
