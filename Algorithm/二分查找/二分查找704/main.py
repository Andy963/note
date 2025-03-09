#!/usr/bin/env python3
# -*- encoding=utf8 -*-

'''
File              : main.py
Author            : Andy963
Created time      : 2024-12-08 08:54:48
Last Modified by  : Andy963
Last Modified time: 2024-12-08 08:55:27
'''
from typing import List 

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return -1