#!/usr/bin/env python3
# -*- encoding=utf8 -*-
# File              : test_2606.py
# Author            : Andy963
# Created time      : 2025-05-25 22:29:42
# Last Modified by  : Andy963
# Last Modified time: 2025-05-25 22:33:56


# ref: https://leetcode.cn/problems/find-the-substring-with-maximum-cost/description/
import pytest
from typing import List

class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        n = len(s)
        # "" is a substring of any string, and it's value is 0
        dp = [0] * (n+1) 
        if s[0] in chars:
            dp[0]=vals[chars.index(s[0])]
        else:
            # ord('a') = 97, and index of 'a' is 1, val is 1, so minus 96
            dp[0] = ord(s[0]) - 96
        
        for i in range(1,n):
            if s[i] in chars:
                vi = vals[chars.index(s[i])]
            else:
                vi = ord(s[i]) - 96
            dp[i] = max(dp[i-1] + vi, vi)
        return max(dp)



def test_case1():
    s = "adaa"
    chars = "d"
    vals = [-1000]
    expected = 2
    result = Solution().maximumCostSubstring(s, chars, vals)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_case2():
    s = "abc"
    chars = "abc"
    vals = [-1,-1,-1]
    expected = 0
    result = Solution().maximumCostSubstring(s, chars, vals)
    assert result == expected, f"Expected {expected}, but got {result}"


if __name__ == "__main__":
    pytest.main()