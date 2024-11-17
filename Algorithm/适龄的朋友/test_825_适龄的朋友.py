#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date     : 2024/11/17
# @FileName : test_825_适龄的朋友.py # noqa
# Created by: Andy963

# ref: https://leetcode.cn/problems/friends-of-appropriate-ages/description/
"""
思路: 排序后，分别找出x可以发送消息的左右边界，
"""

def solve(ages:list[int]):
    n = len(ages)
    ages.sort()
    left = right = ans = 0
    for age in ages:
        if age < 15:
            continue

        while ages[left] <= age * 0.5 + 7:
            left += 1

        while right +1 < n and ages[right + 1] <= age:
            right += 1
        ans += right - left
    return ans

# 测试用例
def test_case_1():
    ages = [16, 16]
    expected = 2
    assert solve(ages) == expected

def test_case_2():
    ages = [16, 17, 18]
    expected = 2
    assert solve(ages) == expected

def test_case_3():
    ages = [20, 30, 100, 110, 120]
    expected = 3
    assert solve(ages) == expected

if __name__ == '__main__':
    import pytest
    pytest.main()