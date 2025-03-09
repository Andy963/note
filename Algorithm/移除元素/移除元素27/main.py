#!/usr/bin/env python3
# -*- encoding=utf8 -*-

"""
File              : main.py
Author            : Andy963
Created time      : 2024-12-07 21:45:12
Last Modified by  : Andy963
Last Modified time: 2024-12-07 21:48:56
"""

import pytest
from typing import List


class Solution:
    def solve(self, nums: List, val: int):
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow


sl = Solution()


def test_case1():
    nums = [3, 2, 2, 3]
    val = 3
    expected = 2
    assert sl.solve(nums, val) == expected


def test_case2():
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    expected = 5
    assert sl.solve(nums, val) == expected


if __name__ == "__main__":
    pytest.main(
        [
            "-v",
            '-s'
        ]
    )
