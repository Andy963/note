#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : leetcode_2390.py
# Author            : Andy
# Date              : 2022.09.05
# Last Modified Date: 2022.09.05
# Last Modified By  : Andy


class Solution:

    def removeStarts(self, s):
        res = ""
        for i in s:
            if i == "*":
                if res:
                    res = res[:-1]
                else:
                    res += i
        return res
