#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date     : 2024/10/20
# @FileName : 二分查找.py # noqa
# Created by: Andy963

def solve(nums:list, target:int):
    flag = False
    index = -1
    low = 0
    high = len(nums) -1

    while not flag and low <= high:
        mid = (low + high) // 2

        if target < nums[mid]:
            high = mid - 1
        elif target > nums[mid]:
            low = mid + 1
        else:
            flag = True
            index = mid
    return index

# 测试用例
def test_case_1():
    nums = [1,3,4,5,6,8]
    target = 4
    expected = 2
    assert solve(nums, target) == expected

def test_case_2():
    nums = [1,2,3,4,5]
    target = 1
    expected = 0
    assert solve(nums, target) == expected

def test_case_3():
    nums = [1,2,3,4,5]
    target = 5
    expected = 4
    assert solve(nums, target) == expected

if __name__ == '__main__':
    import pytest
    pytest.main()