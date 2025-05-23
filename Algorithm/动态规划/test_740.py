#!/usr/bin/env python3
# -*- encoding=utf8 -*-
# File              : test_740.py
# Author            : Andy963
# Created time      : 2025-05-23 22:09:21
# Last Modified by  : Andy963
# Last Modified time: 2025-05-23 22:10:32

# ref: https://leetcode.cn/problems/delete-and-earn/description/
from typing import List

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        a = [0] * (max(nums) + 1)
        for i in nums:
            a[i] += i 
        
        f0 = f1= 0
        for x in a:
            f0, f1 = f1, max(f1, f0+x)
        return f1
    

def test_case1():
    nums = [3, 4, 2]
    expected = 6
    result = Solution().deleteAndEarn(nums)
    assert result == expected, f"Expected {expected}, but got {result}"


def test_case2():
    nums = [2, 2, 3, 3, 3, 4]
    expected = 9
    result = Solution().deleteAndEarn(nums)
    assert result == expected, f"Expected {expected}, but got {result}"


if __name__ == '__main__':
    import pytest
    pytest.main()