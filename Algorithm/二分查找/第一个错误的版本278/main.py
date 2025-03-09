#!/usr/bin/env python3
# -*- encoding=utf8 -*-

'''
File              : main.py
Author            : Andy963
Created time      : 2024-12-08 08:41:42
Last Modified by  : Andy963
Last Modified time: 2024-12-08 08:42:47
'''
class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right =0, n
        while left < right:
            mid = left + (right -left) // 2
            if isBadVersion(mid):
                right = mid 
            else:
                left = mid + 1
        return right # return left also right