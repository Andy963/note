#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date     : 2024/11/11
# @FileName : test_3254_长度为k的子数组的能量值.py # noqa
# Created by: Andy963

# ref:https://leetcode.cn/problems/find-the-power-of-k-size-subarrays-i/description/
"""
遍历整个列表，遍历到i时，继续遍历到i+k-1,即遍历k个元素，如果这k个元素是连续的，遍历
这个区间时，就能一直满足nums[j] - 1 == nums[j-1] 事实上这里：(i+1,i+1k)
如果遍历 (i, i+k-1),则可以判断nums[j] + 1 = nums[j+1]
"""
def solve(nums:list[int], k:int)->list[int]:
    n = len(nums)
    res = [-1] * (n-k+1)
    for i in range(n-k+1):
        valid = True
        for j in range(i+1, i+k):
            if nums[j] -1 != nums[j-1]:
                valid = False
                break
        if valid:
            res[i] = nums[i+k-1]
    return res

def solve2(nums:list[int], k:int)->list[int]:
    n = len(nums)
    res = [-1] * (n-k+1)
    cnt = 0
    for i in range(n):
        cnt = 0 if i == 0 or nums[i] - nums[i-1] != 1 else cnt + 1
        if cnt >= k:
            res[i+k-1] = nums[i]
    return res

# 测试用例
def test_case_1():
    nums = [1, 2, 3, 4, 3, 2, 5]
    k = 3
    expected = [3,4,-1,-1,-1]
    assert solve(nums, k) == expected

def test_case_2():
    nums = [2, 2, 2, 2, 2]
    k = 4
    expected = [-1,-1]
    assert solve(nums, k) == expected

def test_case_3():
    nums = [3, 2, 3, 2, 3, 2]
    k = 2
    expected = [-1,3,-1,3,-1]
    assert solve(nums, k) == expected

if __name__ == '__main__':
    import pytest
    pytest.main()