#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : leetcode_049.py
# Author            : Andy
# Date              : 2022.08.10
# Last Modified Date: 2022.08.10
# Last Modified By  : Andy

# 分类的主要思路是：有相同字母的是一类，只要单词一样，排序后肯定也是一样的
class Solution:
    def groupAnagrams(self, strs):
        res = {}
        for s in strs:
            tmp = ''.join(sorted(s))
            if tmp not in res:
                res[tmp] = s
            else:
                res[tmp].append(s)
        return list(res.values())
