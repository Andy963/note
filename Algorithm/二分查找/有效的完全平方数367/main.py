#!/usr/bin/env python3
# -*- encoding=utf8 -*-

'''
File              : main.py
Author            : Andy963
Created time      : 2024-12-07 21:57:32
Last Modified by  : Andy963
Last Modified time: 2024-12-07 22:02:50
'''
import pytest


class Solution:
    def solve(self, num:int):
        left, right = 0, num
        if num == 1:
            return True
        while left <= right:
            mid = left +(right - left) // 2
            if num / mid > mid:
                left = mid + 1
            elif num / mid < mid:
                right = mid - 1
            else:
                return True
        return False

sl = Solution()

def test_case1():
    num = 16
    expected = True
    assert sl.solve(num) == expected


def test_case2():
    num = 14
    expected = False
    assert sl.solve(num) == expected


def test_case3():
    num = 1
    expected = True
    assert sl.solve(num) == expected


if __name__ == '__main__':
    pytest.main(['-v','-s'])