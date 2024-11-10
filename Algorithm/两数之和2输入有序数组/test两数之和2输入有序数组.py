#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date     : 2024/11/4
# @FileName : test两数之和2输入有序数组.py # noqa
# Created by: Andy963

# ref https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/submissions/208081069/
def solve(numbers:list, target:int) -> list:
    left, right = 0, len(numbers) - 1
    while left < right:
        if numbers[left] + numbers[right] == target:
            return [left + 1, right + 1]
        elif numbers[left] + numbers[right] < target:
            left += 1
        else:
            right -= 1

# 测试用例
def test_case_1():
    numbers = [0,0,3,4]
    target = 0
    expected = [1,2]
    assert(solve(numbers, target) == expected)

def test_case_2():
    numbers = [2,3,4]
    target = 6
    expected = [1,3]
    assert(solve(numbers, target) == expected)


def test_case_3():
    numbers = [-1,0]
    target = -1
    expected = [1,2]
    assert(solve(numbers, target) == expected)

def test_case_4():
    numbers = [2,7,11,15]
    target = 9
    expected = [1,2]
    assert(solve(numbers, target) == expected)

if __name__ == '__main__':
    import pytest
    pytest.main()