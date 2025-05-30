#!/usr/bin/env python3
# -*- encoding=utf8 -*-
# File              : test_152.py
# Author            : Andy963
# Created time      : 2025-05-28 21:21:06
# Last Modified by  : Andy963
# Last Modified time: 2025-05-28 21:26:10

# ref: https://leetcode.cn/problems/maximum-product-subarray/description/

import pytest
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        max_val = nums[0]
        min_val = nums[0]
        ans = nums[0]
        for i in range(1, n):
            temp_max = max_val
            max_val = max(nums[i], max_val * nums[i], min_val * nums[i])
            min_val = min(nums[i], temp_max * nums[i], min_val * nums[i])
            ans = max(ans, max_val)
        return ans


def test_case1():
    nums = [2, 3, -2, 4]
    expected = 6
    result = Solution().maxProduct(nums)
    assert result == expected, f"Expected {expected}, but got {result}"


def test_case2():
    nums = [-2, 0, -1]
    expected = 0
    result = Solution().maxProduct(nums)
    assert result == expected, f"Expected {expected}, but got {result}"


if __name__ == "__main__":
    pytest.main()
