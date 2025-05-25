#!/usr/bin/env python3
# -*- encoding=utf8 -*-
# File              : test_53.py
# Author            : Andy963
# Created time      : 2025-05-25 16:22:09
# Last Modified by  : Andy963
# Last Modified time: 2025-05-25 16:25:30

# ref: https://leetcode.cn/problems/maximum-subarray/description/

import pytest
from typing import List


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            # dp[i] = max(dp[i - 1], 0) + nums[i]
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        return max(dp)


def test_case1():
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    expected = 6
    result = Solution().maxSubArray(nums)
    assert result == expected, f"Expected {expected}, but got {result}"


def test_case2():
    nums = [1]
    expected = 1
    result = Solution().maxSubArray(nums)
    assert result == expected, f"Expected {expected}, but got {result}"


if __name__ == "__main__":
    pytest.main()
