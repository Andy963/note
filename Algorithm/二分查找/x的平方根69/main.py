#!/usr/bin/env python3
# -*- encoding=utf8 -*-

'''
File              : main.py
Author            : Andy963
Created time      : 2024-12-08 08:58:59
Last Modified by  : Andy963
Last Modified time: 2024-12-08 08:59:01
'''
class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        ans = 0
        while left <= right:
            mid = left + (right-left) // 2
            if x < mid * mid:
                right = mid -1
            elif x >= mid * mid:
                ans = mid
                left = mid +1
            else:
                return mid
        return ans