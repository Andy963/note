#!/usr/bin/env python3
# -*- encoding=utf8 -*-

'''
File              : main.py
Author            : Andy963
Created time      : 2024-12-08 08:10:23
Last Modified by  : Andy963
Last Modified time: 2024-12-08 08:19:23
'''

import pytest
from typing import List

class Solution:
    def solve(self, nums:List[int],target:int)-> int:
        left, right = 0 , len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid +1
            else:
                return mid
        return left

sl = Solution()

def test_case1():
    nums = [1,3,5,6]
    target = 5
    expected = 2
    assert sl.solve(nums, target) == expected


def test_case2():
    nums = [1,3,5,6]
    target = 2
    expected = 1
    assert sl.solve(nums, target) == expected


def test_case3():
    nums = [1,3,5,6]
    target = 7
    expected = 4
    assert sl.solve(nums, target) == expected


if __name__ == '__main__':
    pytest.main(['-v','-s'])