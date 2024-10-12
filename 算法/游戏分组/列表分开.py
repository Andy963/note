#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date     : 2024/9/28
# @FileName : 列表分开.py # noqa
# Created by; Andy963

"""
在做游戏分组时使用combination时发现一个问题，当分的两组数中有相同的数时，
最后返回的两组数会出现问题。
问题简化为：nums中有相同的数时，返回的两组数会出现重复。已经其中部分数字组成的子列表
需要返回除这些数字外的另一部分列表。
"""
import unittest


def solve(nums,t1):

    dp1 = [False] * len(nums)
    dp2 = [False] * len(t1)
    for i,n in enumerate(nums):
        for j,m  in enumerate(t1):
            if dp2[j]:
                continue
            if n == m:
                dp2[j] = True
                dp1[i] = True
                break
    return [ nums[i] for i in range(len(nums)) if not dp1[i]]


def solve(nums, t1):
    # 用于存放结果
    result = []

    for num in nums:
        if num in t1:
            t1.remove(num)  # 删除第一个匹配的元素
        else:
            result.append(num)  # 如果不在 t1 中，加入结果
    return result

class TestSolve(unittest.TestCase):
    def test_case_1(self):
        nums = [1,1,2,3,3]
        t1 = [1,2]
        expected_output = [1,3,3]
        self.assertEqual(solve(nums,t1), expected_output)

    def test_case_2(self):
        nums = [1,1,2,3,3]
        t1 = [1,2,1]
        expected_output = [3,3]
        self.assertEqual(solve(nums,t1), expected_output)

    def test_case_3(self):
        nums = [1,1,2,]
        t1 = [1,2,1]
        expected_output = []
        self.assertEqual(solve(nums,t1), expected_output)

if __name__ == '__main__':
    unittest.main()