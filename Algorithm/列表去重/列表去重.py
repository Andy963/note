#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date     : 2024/9/26
# @FileName : 列表去重.py # noqa
# Created by; Andy963

"""
给定一个列表，去除列表中重复的元素

1.不使用set
2.不额外开辟空间
def solve(nums):
    raw_nums = nums
    for i, n in enumerate(nums):
        if n in nums[i+1:]:
            tmp = nums[i+1:]
            tmp.remove(n)
            raw_nums[i+1:] = tmp
    return nums
"""
import unittest


def solve(nums):
    i = 0
    while i < len(nums):
        j = i + 1
        while j < len(nums):
            # 关键是len(nums)会重新计算长度，而当j元素被删除时，j没有+1，
            # 这样就不会导致j超出边界的情况发生
            if nums[j] == nums[i]:
                nums.pop(j)
            else:
                j+= 1
        i += 1

    return nums



class TestSolve(unittest.TestCase):

    def test_case_1(self):
        nums = [4, 1, 2, 5, 2, 4]
        expected_output = [4, 1, 2, 5]
        self.assertEqual(solve(nums), expected_output)

    def test_case_2(self):
        nums = [4, 4, 3, 3, 5, 2]
        expected_output = [4, 3, 5, 2]
        self.assertEqual(solve(nums), expected_output)

    def test_case_3(self):
        nums = [4,4]
        expected_output = [4]
        self.assertEqual(solve(nums), expected_output)


if __name__ == '__main__':
    unittest.main()