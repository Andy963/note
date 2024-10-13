#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : leetcode_011.py
# Author            : Andy
# Date              : 04.08.2022
# Last Modified Date: 04.08.2022
# Last Modified By  : Andy


# 主体思路, 两个指针，一个从左边开始，一个从右边开始，面积=底*高 底= right -left, 高= height[i], height[j]中较小的一个
# 所以求面积时要先用min, 而最后的结果是求最大值， 所以要用max

class Solution:
    def maxArea(self, height):
        ans = 0
        left, right = 0, len(height) -1
        while left < right:
            ans = max(ans, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right += 1
        return ans
