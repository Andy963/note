#!/usr/bin/env python3
# -*- encoding=utf8 -*-
# File              : test_1191.py
# Author            : Andy963
# Created time      : 2025-05-27 21:04:57
# Last Modified by  : Andy963
# Last Modified time: 2025-05-27 21:06:50

# ref: https://leetcode.cn/problems/k-concatenation-maximum-sum/

import pytest
from typing import List

class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        def maxArr(nums):
            n = len(nums)
            max_val = 0
            ans = 0
            for i in range(n):
                max_val = max(max_val+nums[i],nums[i])
                ans = max(ans, max_val)
            return ans
        if k == 1:
            return maxArr(arr)
        ans = maxArr(arr * 2)
        ans += max(sum(arr), 0) *(k-2)
        return ans % (10**9 + 7)
    
def test_case1():
    arr = [1, -2, 1]
    k = 5
    expected = 2
    result = Solution().kConcatenationMaxSum(arr, k)
    assert result == expected, f"Expected {expected}, but got {result}"


def test_case2():
    arr = [1, 2]
    k = 3
    expected = 9
    result = Solution().kConcatenationMaxSum(arr, k)
    assert result == expected, f"Expected {expected}, but got {result}"

if __name__ == "__main__":
    pytest.main()