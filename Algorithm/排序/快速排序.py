#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date     : 2024/10/20
# @FileName : 快速排序.py # noqa
# Created by; Andy963

def solve(arr, start, end):
    low = start
    high = end

    if low > high:
        return

    pivot = arr[low]
    while low < high:
        while low < high:
            if arr[high] > pivot:
                high -= 1
            else:
                arr[low] = arr[high]
                break
        while low < high:
            if arr[low] < pivot:
                low += 1
            else:
                arr[high] = arr[low]
                break

    if low == high:
        arr[low] = pivot

    solve(arr, start, high-1)
    solve(arr, low+1, end)
    return arr



# 测试用例
def test_case_1():
    arr = [1,0,3,5,4,7]
    expected_out = [0,1,3,4,5,7]
    assert solve(arr, 0, len(arr) - 1) == expected_out

def test_case_2():
    arr = [1,0,-3,5,4,-7]
    expected_out = [-7,-3,0,1,4,5]
    assert solve(arr, 0, len(arr) -1 ) == expected_out

def test_case_3():
    arr = [-1,-3,0,1]
    expected_out = [-3,-1,0,1]
    assert solve(arr, 0, len(arr) -1 ) == expected_out

if __name__ == '__main__':
    import pytest
    pytest.main()