#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : leetcode_239.py
# Author            : Andy
# Date              : 06.08.2022
# Last Modified Date: 06.08.2022
# Last Modified By  : Andy


class Solution:
    def maxSlideingWindow(nums, k):
        result = []
        q = []
        for i in range(len(nums)):
            # 
            while q and q[0] <= i -k:
                q.pop(0)

            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            q.append(i)

            if i >= k-1:
                result.append(nums[q[0]])
        return result

