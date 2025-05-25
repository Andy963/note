#!/usr/bin/env python3
# -*- encoding=utf8 -*-
# File              : test_270.py
# Author            : Andy963
# Created time      : 2025-05-24 07:10:17
# Last Modified by  : Andy963
# Last Modified time: 2025-05-24 09:44:32

# ref: https://leetcode.cn/problems/perfect-squares/description/
import pytest
from math import isqrt, inf
from itertools import cache


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] + [inf] * n
        for i in range(1, n + 1):
            for j in range(1, isqrt(i) + 1):
                dp[i] = min(dp[i], dp[i - j * j] + 1)
        return dp[n]

    def numSquares2(self, n: int) -> int:
        # 这种方案会超内存
        @cache
        def dfs(i, j):
            if i == 0:
                return inf if j else 0
            # i * i > j 则不能选择i, 直接选择i-1
            if i * i > j:
                return dfs(i - 1, j)
            # 选择i, dfs(i, j-i*i) + 1， 1即为选择i
            return min(dfs(i - 1, j), dfs(i, j - i * i) + 1)

        return dfs(isqrt(n), n)


def test_case1():
    n = 12
    expected = 3
    result = Solution().numSquares(n)
    assert result == expected, f"Expected {expected}, but got {result}"


def test_case2():
    n = 13
    expected = 2
    result = Solution().numSquares(n)
    assert result == expected, f"Expected {expected}, but got {result}"


if __name__ == "__main__":
    import pytest

    pytest.main()
