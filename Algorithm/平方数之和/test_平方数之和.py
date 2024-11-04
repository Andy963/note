#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date     : 2024/11/4
# @FileName : test_平方数之和.py # noqa
# Created by: Andy963

# ref: https://leetcode.cn/problems/sum-of-square-numbers/description/?envType=daily-question&envId=2024-11-04
from math import isqrt

# 使用列表存平方数，会导致超时
def solve(c:int) -> bool:
    a ,b = 0, isqrt(c)
    while a  <= b:
        s = a * a + b * b
        if s == c:
            print(a,b)
            return True
        if s > c:
            b -= 1
        else:
            a += 1
    return False

def solve2(c:int) -> int:
    # 注意a b 可相等
    a = 0
    while a * a * 2 <= c:
        b = isqrt(c - a * a)
        if a * a + b * b == c:
            return True
        a += 1
    return False

# 测试用例
def test_case_1():
    c = 5
    expected = True
    assert solve(c) == expected

def test_case_2():
    c = 4
    expected = True
    assert solve(c) == expected


def test_case_3():
    c = 3
    expected = False
    assert solve(c) == expected
def test_case_4():
    c = 2147482647
    expected = False
    assert solve(c) == expected

if __name__ == '__main__':
    import pytest
    pytest.main()