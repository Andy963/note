#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date     : 2024/10/20
# @FileName : 791自定义字符串排序.py # noqa
# Created by: Andy963

# ref: https://leetcode.cn/problems/custom-sort-string/description/


def solve(order: str, s: str):
    def f(c: str):
        return order.index(c) if c in order else 201

    return "".join(sorted(s, key=f))


# 测试用例
def test_case_1():
    order = "cba"
    s = "abcd"
    expected = "cbad"
    assert solve(order, s) == expected


def test_case_2():
    order = "cbafg"
    s = "abcd"
    expected = "cbad"
    assert solve(order, s) == expected


def test_case_3():
    pass


if __name__ == "__main__":
    import pytest

    pytest.main()
