#!/usr/bin/env python3
# -*- encoding=utf8 -*-
# File              : test_2466.py
# Author            : Andy963
# Created time      : 2025-05-20 21:37:16
# Last Modified by  : Andy963
# Last Modified time: 2025-05-20 23:31:46


# ref:https://leetcode.cn/problems/count-ways-to-build-good-strings/description/

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 10 ** 9 + 7 
        
        def dfs(i):
            if i < 0:
                return 0
                
            if i == 0:
                return 1
            # dfs(i-zero) 后面加zero个0，dfs(i-one) 后面加one个1
            return (dfs(i-zero) + dfs(i-one)) % mod
        return sum(dfs(i) for i in range(low, high+1)) % mod
    def countGoodStrings2(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 10 ** 9 + 7 
        
        dp = [0] * (high + 1)
        dp[0] = 1
        for i in range(1, high + 1):
            if i >= zero:
                dp[i] += dp[i - zero]
            if i >= one:
                dp[i] += dp[i - one]
            dp[i] %= mod
        return sum(dp[i] for i in range(low, high + 1)) % mod
    


def test_case1():
    low, high, zero, one = 3, 3, 1, 1
    expected = 8
    result = Solution().countGoodStrings2(low, high, zero, one)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_case2():
    low, high, zero, one = 2, 3, 1, 2
    expected = 5
    result = Solution().countGoodStrings(low, high, zero, one)
    assert result == expected, f"Expected {expected}, but got {result}"

if __name__ == '__main__':
    import pytest
    pytest.main()