#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : leetcode_342.py
# Author            : Andy
# Date              : 2022.08.29
# Last Modified Date: 2022.08.29
# Last Modified By  : Andy


class Solution:

    def isPowerOfFour(self, n: int) -> bool:
        for i in range(16):
            if n == 4**i:
                return True
        return False
