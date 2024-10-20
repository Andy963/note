#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date     : 2024/10/20
# @FileName : 冒泡排序.py # noqa
# Created by; Andy963
import unittest


def bubble_sort1(arr: list):
    n = len(arr)
    for i in range(n):
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def bubble_sort2(arr: list):
    n = len(arr)
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


class TestSolve(unittest.TestCase):
    def test_case_1(self):
        arr = [5, 3, 4, 2, 1]
        self.assertEqual(bubble_sort1(arr), [1, 2, 3, 4, 5])

    def test_case_2(self):
        arr = [-5, 4, 3, 2, 1]
        self.assertEqual(bubble_sort2(arr), [-5, 1, 2, 3, 4])

    def test_case_3(self):
        arr = [1, 0, 0, -1]
        expected_out = [-1, 0, 0, 1]
        self.assertEqual(bubble_sort2(arr), expected_out)


if __name__ == '__main__':
    unittest.main()
