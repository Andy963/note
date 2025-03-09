#!/usr/bin/env python3
# -*- encoding=utf8 -*-
# File              : main.py
# Author            : Andy963
# Created time      : 2024-12-21 16:58:15
# Last Modified by  : Andy963
# Last Modified time: 2024-12-21 17:20:09

import pytest


class Solution:
    def solve(self, n:int):
        nums = [[0] * n for _ in range(n)]
        startx, starty = 0, 0
        loop, mid = n // 2, n // 2
        count = 1
        for offset in range(1, loop+1):
            for i in range(starty, n-offset):
                nums[startx][i] = count
                count += 1
            for  i in range(startx, n-offset):
                nums[i][n-offset] = count
                count += 1
            for i in range(n-offset, starty, -1):
                nums[n-offset][i] = count
                count += 1

            for i in range(n-offset, startx, -1):
                nums[i][starty] = count
                count += 1
            startx += 1
            starty += 1
        if n % 2 == 1:
            nums[mid][mid] = count
        print(nums)
        return nums

s = Solution()
def test_case1():
    n = 3
    expected = [[1,2,3],[8,9,4],[7,6,5]]
    assert s.solve(n) == expected


def test_case2():
    n = 1
    expected = [[1]]
    assert s.solve(n) == expected




if __name__ == '__main__':
    pytest.main(['-v','-s'])