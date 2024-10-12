#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date     : 2024/9/23
# @FileName : 20.py # noqa
# Created by; Andy963
"""
小明每周上班都会拿到自己的工作清单，工作清单内包含 n 项工作，每项工作都有对应的耗时时间(单位 h)和报酬，工作的总报酬为所有已完成工作的报酬之和，那么请你帮小明安排一下工作，保证小明在指定的工作时间内工作收入最大化。
输入描述
输入的第一行为两个正整数 T，n。
T 代表工作时长 (单位 h，0<T< 1000000)，
n 代表工作数量 (1<n<= 3000)。
接下来是 n 行，每行包含两个整数 t，w。
t 代表该工作消耗的时长(单位 h，t>0)，w 代表该项工作的报酬
输出描述
输出小明指定工作时长内工作可获得的最大报酬
示例1
输入
40 3
20 10
20 20
20 5
输出
30
"""
import unittest


def solve(T,  tasks):
    dp = [0] *(T + 1)

    for t, w in tasks:
        for j in range(T, t-1, -1):
            dp[j] = max(dp[j],dp[j-t]+w)

    return dp[T]

class TestSolve(unittest.TestCase):
    def test_case_1(self):
        T, n = 40, 3
        tasks = [(20, 10), (20, 20), (20, 5)]
        expected_output = 30
        self.assertEqual(solve(T, tasks), expected_output)


if __name__ == '__main__':
    unittest.main()