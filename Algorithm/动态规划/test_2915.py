#!/usr/bin/env python3
# -*- encoding=utf8 -*-
# File              : test_2915.py
# Author            : Andy963
# Created time      : 2025-05-30 06:55:39
# Last Modified by  : Andy963
# Last Modified time: 2025-05-30 06:59:26

# ref: https://leetcode.cn/problems/length-of-the-longest-subsequence-that-sums-to-target/description/
import pytest 
from functools import cache
from typing import List
from math import inf as inf

class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        @cache
        def dfs(i, t):
            if i < 0:
                return 0 if t==0 else -inf
            if nums[i] > t:
                # 不能选
                return dfs(i-1, t)
            # 不选则在返回i-1, 选则长度+1
            return max(dfs(i-1,t), dfs(i-1, t-nums[i])+1)

        ans = dfs(len(nums)-1, target)
        dfs.cache_clear()
        return ans if ans > 0 else -1
    
def test_case1():
    nums = [1, 2, 3, 4, 5]
    target = 9
    expected = 3
    result = Solution().lengthOfLongestSubsequence(nums, target)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_case2():
    nums = [4,1,3,2,1,5]
    target = 7
    expected = 4 
    result = Solution().lengthOfLongestSubsequence(nums, target)
    assert result == expected, f"Expected {expected}, but got {result}"


if __name__ == '__main__':
    pytest.main()