#!/usr/bin/env python3
# -*- encoding=utf8 -*-

'''
File              : main.py
Author            : Andy963
Created time      : 2024-12-08 08:44:38
Last Modified by  : Andy963
Last Modified time: 2024-12-08 08:45:15
'''
class Solution:
    def guessNumber(self, n: int) -> int:
        left,right = 1,n
        while left <= right:
            mid = (right + left) // 2
            if guess(mid) == 0:
                return mid 
            elif guess(mid) == -1:
                right = mid -1
            elif guess(mid) == 1:
                left = mid +1