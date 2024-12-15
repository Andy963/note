#!/usr/bin/env python3
# -*- encoding=utf8 -*-
# File              : main.py
# Author            : Andy963
# Created time      : 2024-12-15 16:50:06
# Last Modified by  : Andy963
# Last Modified time: 2024-12-15 17:01:41
import pytest


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:


s = Solution()


def test_case1():
    nums = [2, 3, 1, 2, 4, 3]
    target = 7
    expected = 2
    assert expected == s.minSubArrayLen(target, nums)


def test_case2():
    nums = [1, 4, 4]
    target = 4
    expected = 1
    assert expected == s.minSubArrayLen(target, nums)


if __name__ == "__main__":
    pytest.main(["-s", "-v"])
