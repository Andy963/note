#!/usr/bin/env python3
# -*- encoding=utf8 -*-
# File              : test_518.py
# Author            : Andy963
# Created time      : 2025-05-21 22:06:15
# Last Modified by  : Andy963
# Last Modified time: 2025-05-21 22:10:31

from typing import List
from functools import cache
# ref https://leetcode.cn/problems/coin-change-ii/submissions/631527366/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        @cache
        def dfs(i, a):
            if i < 0:
                return 1 if a == 0 else 0
            if coins[i] > a:
                # 只能不选
                return dfs(i - 1, a)
            return dfs(i - 1, a) + dfs(i, a - coins[i])
        return dfs(len(coins) - 1, amount)
            
    def change1(self, amount: int, coins: List[int]) -> int:
        dp = [1] + [0] * amount
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] += dp[i - coin]
        return dp[amount]


def test_case1():
    amount = 5
    coins = [1, 2, 5]
    expected = 4
    result = Solution().change(amount, coins)
    assert result == expected, f"Expected {expected}, but got {result}"


def test_case2():
    amount = 3
    coins = [2]
    expected = 0
    result = Solution().change1(amount, coins)
    assert result == expected, f"Expected {expected}, but got {result}"


if __name__ == '__main__':
    import pytest
    pytest.main()