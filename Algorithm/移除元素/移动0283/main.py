#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : leetcode_283.py
# Author            : Andy
# Date              : 23.07.2022
# Last Modified Date: 23.07.2022
# Last Modified By  : Andy
import pytest

# 主体思路：将非零的元素留下，然后在末尾补零
# 什么样的元素要留下？判断是否等于0即可


def moveZeros(nums: list):
    n = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[n] = nums[i]
            n += 1
    while n < len(nums):
        nums[n] = 0
        n += 1


def solve(nums: list) -> list:
    slow, fast = 0, 0
    while fast < len(nums):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
        fast += 1
    return nums


def test_case1():
    nums = [0, 1, 0, 3, 12]
    expected = [1, 3, 12, 0, 0]
    assert solve(nums) == expected


def test_case2():
    nums = [0]
    expected = [0]
    assert solve(nums) == expected


if __name__ == "__main__":
    pytest.main(["-v", "-s"])
