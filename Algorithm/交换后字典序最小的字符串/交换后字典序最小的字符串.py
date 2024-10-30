#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date     : 2024/10/30
# @FileName : 交换后字典序最小的字符串.py # noqa
# Created by: Andy963
# https://leetcode.cn/problems/lexicographically-smallest-string-after-a-swap/
def solve(s: str) -> str:
    s = list(s)
    for i in range(1, len(s)):
        pre = int(s[i - 1])
        cur = int(s[i])
        if (cur % 2) == (pre % 2) and pre > cur:
            s[i], s[i - 1] = s[i - 1], s[i]
            break
    return "".join(s)


# 测试用例
def test_case_1():
    s = "45320"
    expected = "43520"
    assert solve(s) == expected


def test_case_2():
    s = "001"
    expected = "001"
    assert solve(s) == expected


if __name__ == "__main__":
    import pytest

    pytest.main()
