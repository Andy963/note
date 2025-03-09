#!/usr/bin/env python3
# -*- encoding=utf8 -*-
# File              : main.py
# Author            : Andy963
# Created time      : 2024-12-15 15:46:23
# Last Modified by  : Andy963
# Last Modified time: 2024-12-15 16:10:42


import pytest


class Solution:
    def solve(self, nums:list[int]):
        n = len(nums)
        ans = [0] * n
        left, right, pos = 0, n-1, n-1
        while left <= right:
            l_val, r_val = nums[left] * nums[left], nums[right] * nums[right]
            if l_val < r_val:
                ans[pos] = r_val 
                right -= 1
            else:
                ans[pos] = l_val 
                left += 1
            pos -= 1
        return ans 

sl = Solution()
def test_case1():
    nums = [-4,-1,0,3,10]
    expected = [0,1,9,16,100]
    assert sl.solve(nums) == expected


def test_case2():
    nums = [-7,-3,2,3,11]
    expected = [4,9,9,49,121]
    assert sl.solve(nums) == expected



if __name__ == '__main__':
    pytest.main(['-v','-s'])