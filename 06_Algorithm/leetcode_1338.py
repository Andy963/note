#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : leetcode_1338.py
# Author            : Andy
# Date              : 2022.08.30
# Last Modified Date: 2022.08.30
# Last Modified By  : Andy


# 先统计次数，再将次数排序，先从最大的开始减，只要能小于等于原来长度的一半即可达到要求
class Solution:

    def minSetSize(self, arr):
        counts = collections.Counter(arr)
        values = sorted(counts.values(), reverse=True)
        removed = 0
        length = len(arr)
        half = length // 2

        for v in values:
            length -= v
            removed += 1
            if length <= half:
                return removed
        return removed
