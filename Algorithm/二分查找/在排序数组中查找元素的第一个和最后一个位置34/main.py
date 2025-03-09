#!/usr/bin/env python3
# -*- encoding=utf8 -*-

'''
File              : main.py
Author            : Andy963
Created time      : 2024-12-08 09:01:04
Last Modified by  : Andy963
Last Modified time: 2024-12-08 09:01:20
'''
from typing import List 

class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums) -1 
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid -1
            else:
                left = mid + 1
        return left
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]
        p1 = self.search(nums, target)
        p2 = self.search(nums, target+1)
        return [p1,p2-1]