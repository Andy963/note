#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date     : 2024/9/27
# @FileName : 空栈压数.py # noqa
# Created by; Andy963
"""
向一个空栈压入正整数，每当压入一个整数时，执行以下规则(设:栈顶至栈底整数依次为n1,n2,. nx，其中n1为最新压入的整数)。
1.如果 n1 = n2，则 n1, n2 全部出栈，压入新数据 m(m =2*n1)
2.如果 n1 = n2 + ... + ny 的范围为 3,n，则 n1,n2,…, ny 全部出栈，压入新数据m(m=2*n1)3.如果上述规则均不满足，则不做操作。
如:依次向栈压入6，1，2，3，
1.当压入 2 时，栈顶至栈底依次为 2,1,6;
2.当压入3时，3=2+1，3，2,1全部出栈，重新入栈整数6，此时栈顶至栈底依次为 6,6;6=6，两个6全部出栈，压入 12，最终栈中只剩个元素 12。向栈中输入一串数字，请输出应用此规则后栈中最终存留的数字。
输入描述：
使用单个空格隔开的正整数的字符串 Q，如“5678”，左边的数字先入栈。
1.正整数大小为 [1，231-1]
2.正整数个数为 [1,1000]。
输出描述：
最终栈中存留的元素值，元素值使用单个空格隔开，从左至右依次为栈顶至栈底的数字
示例1
输入
10 20 50 80 1 1
输出
2 160
示例2
输入
5 10 20 50 85 1
输出
1 170
"""
import unittest


def solve(nums):
    stack = []
    for n in nums:
        total = n
        flag = False
        length = len(stack)
        while length > 0 and total > 0:
            total -= stack[length-1]
            if total == 0:
                stack = stack[:length-1]
                stack.append(n*2)
                flag = True
            length -= 1
        if not flag:
            stack.append(n)
    return stack[::-1]

class TestSolve(unittest.TestCase):
    def test_case_0(self):
        nums = [1,1]
        expected_output = [2]
        self.assertEqual(solve(nums), expected_output)
    def test_case_1(self):
        nums = [3,2,1,6]
        expected_output = [12]
        self.assertEqual(solve(nums), expected_output)

    def test_case_2(self):
        nums = [10, 20, 50, 80, 1, 1]
        expected_output = [2, 160]
        self.assertEqual(solve(nums), expected_output)

    def test_case_3(self):
        nums = [5, 10, 20, 50, 85, 1]
        expected_output = [1, 170]
        self.assertEqual(solve(nums), expected_output)

if __name__ == '__main__':
    unittest.main()