#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date     : 2024/11/2
# @FileName : 使两个整数相等的位更改次数.py # noqa
# Created by: Andy963
# https://leetcode.cn/problems/number-of-bit-changes-to-make-two-integers-equal/description/
def solve(n:int, k:int) -> int:
    if k > n:
        return -1
    if k == n:
        return 0

    if n & k != k:
        return -1

    return bin(n).count('1') - bin(k).count('1')

# 测试用例
def test_case_1():
    n = 20
    k = 20
    expected_output = 0
    assert solve(n, k) == expected_output

def test_case_2():
    n = 14
    k = 13
    expected_output = -1
    assert solve(n, k) == expected_output

def test_case_3():
    n = 13
    k = 4
    expected_output = 2
    assert solve(n, k) == expected_output

if __name__ == '__main__':
    import pytest
    pytest.main()