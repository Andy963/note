#!/usr/bin/env python3
# -*- encoding=utf8 -*-
# File              : test_1089.py
# Author            : Andy963
# Created time      : 2025-06-08 11:54:16
# Last Modified by  : Andy963
# Last Modified time: 2025-06-08 12:36:02


# ref: https://leetcode.cn/problems/duplicate-zeros/description/
import pytest
from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        count0 = 0
        n = len(arr)
        for i in range(n):
            if arr[i] == 0:
                count0 += 1
        step = count0
        for j in range(n - 1, -1, -1):
            if arr[j] != 0 and j + step <= n - 1:
                arr[j + step] = arr[j]
            elif arr[j] == 0:
                step -= 1
                if j + step < n - 1:
                    arr[j + step + 1] = 0
                if j + step <= n - 1:
                    arr[j + step] = 0


def test_case1():
    arr = [1, 0, 2, 3, 0, 4, 5, 0]
    expected = [1, 0, 0, 2, 3, 0, 0, 4]
    Solution().duplicateZeros(arr)
    assert arr == expected, f"Expected {expected}, but got {arr}"


def test_case2():
    arr = [1, 2, 3]
    expected = [1, 2, 3]
    Solution().duplicateZeros(arr)
    assert arr == expected, f"Expected {expected}, but got {arr}"


def test_case3():
    arr = [0, 1, 7, 6, 0, 2, 0, 7]
    expected = [0, 0, 1, 7, 6, 0, 0, 2]
    Solution().duplicateZeros(arr)
    assert arr == expected, f"Expected {expected}, but got {arr}"


def test_case4():
    arr = [0, 0, 0, 0, 0, 0, 0]
    expected = [0, 0, 0, 0, 0, 0, 0]
    Solution().duplicateZeros(arr)
    assert arr == expected, f"Expected {expected}, but got {arr}"


def test_case5():
    arr = [8, 4, 5, 0, 0, 0, 0, 7]
    expected = [8, 4, 5, 0, 0, 0, 0, 0]
    Solution().duplicateZeros(arr)
    assert arr == expected, f"Expected {expected}, but got {arr}"


if __name__ == "__main__":
    pytest.main()
