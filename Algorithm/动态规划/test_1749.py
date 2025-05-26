#!/usr/bin/env python3
# -*- encoding=utf8 -*-
# File              : test_1706.py
# Author            : Andy963
# Created time      : 2025-05-26 22:52:48
# Last Modified by  : Andy963
# Last Modified time: 2025-05-26 22:55:13

# ref: https://leetcode.cn/problems/maximum-absolute-sum-of-any-subarray/description/

import pytest 
from typing import List

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        n = len(nums)
        max_val = min_val= nums[0]
        max_abs = abs(nums[0])
        for i in range(1,n):
            #  calculate the min val and max val, one of them will be th answer
            min_val  = min(min_val, 0) + nums[i]
            max_val  = max(max_val, 0) + nums[i]
            max_abs = max(max_abs, abs(min_val), abs(max_val))
          
        return max_abs
    

def test_case1():
    nums = [1, -3, 2, 3, -4]
    expected = 5
    result = Solution().maxAbsoluteSum(nums)
    assert result == expected, f"Expected {expected}, but got {result}"


def test_case2():
    nums = [2, -5, 1, -4, 3, -2]
    expected = 8
    result = Solution().maxAbsoluteSum(nums)
    assert result == expected, f"Expected {expected}, but got {result}"


if __name__ == "__main__":
    pytest.main()