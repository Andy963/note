#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date     : 2024/9/22
# @FileName : 14.py # noqa
# Created by; Andy963
"""
程序员小明打了一辆出租车去上班。出于职业敏感，他注意到这辆出租车的计费表有点问题，总是偏大。
出租车司机解释说他不喜欢数字4，所以改装了计费表，任何数字位置遇到数字4就直接跳过，其余功能都正常。
比如：
1.     23再多一块钱就变为25；
2.     39再多一块钱变为50；
3.     399再多一块钱变为500；
小明识破了司机的伎俩，准备利用自己的学识打败司机的阴谋。
给出计费表的表面读数，返回实际产生的费用。
输入描述：
只有一行，数字N，表示里程表的读数。
(1<=N<=888888888)。
输出描述：
一个数字，表示实际产生的费用。以回车结束。
示例1
输入：
5
输出：
4
说明：
5表示计费表的表面读数。
4表示实际产生的费用其实只有4块钱。
示例2
输入：
17
输出：
15
说明：
17表示计费表的表面读数。
15表示实际产生的费用其实只有15块钱。
示例3
输入：
100
输出：
81
说明：
100表示计费表的表面读数。
81表示实际产生的费用其实只有81块钱。
"""
import unittest


def solve(N):
    n_str = str(N)
    res = 0
    multiplier = 1
    for i in range(len(n_str)-1, -1,-1):
        digit = int(n_str[i])
        if digit > 4:
            digit -= 1
        res += digit * multiplier
        multiplier *= 9
    return res


class TestSolve(unittest.TestCase):
    def test_case_1(self):
        N = 5
        expected_output = 4
        self.assertEqual(solve(N), expected_output)

    def test_case_2(self):
        N = 17
        expected_output = 15
        self.assertEqual(solve(N), expected_output)

    def test_case_3(self):
        N = 100
        expected_output = 81
        self.assertEqual(solve(N), expected_output)

if __name__ == '__main__':
    unittest.main()