#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date     : 2024/10/20
# @FileName : 选择排序.py # noqa
# Created by; Andy963
import unittest


def solve(arr: list):
    n = len(arr)
    for i in range(n - 1, 0, -1):
        max_index = i
        # 找到未排序的元素中最大的元素的索引
        for j in range(i):
            if arr[j] > arr[max_index]:
                max_index = j
        arr[i], arr[max_index] = arr[max_index], arr[i]
    return arr


def solve2(arr: list):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


class TestSolve(unittest.TestCase):
    def test_case_1(self):
        arr = [1, 0, 3, 5, 4, 7]
        expected_out = [0, 1, 3, 4, 5, 7]
        self.assertEqual(solve2(arr), expected_out)

    def test_case_2(self):
        arr = [1, 0, -3, 5, 4, -7]
        expected_out = [-7, -3, 0, 1, 4, 5]
        self.assertEqual(solve2(arr), expected_out)

    def test_case_3(self):
        arr = [1, 0, 0, -1]
        expected_out = [-1, 0, 0, 1]
        self.assertEqual(solve2(arr), expected_out)


if __name__ == "__main__":
    unittest.main()
