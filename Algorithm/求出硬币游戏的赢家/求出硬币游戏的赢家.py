#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date     : 2024/11/5
# @FileName : 求出硬币游戏的赢家.py # noqa
# Created by: Andy963

# ref https://leetcode.cn/problems/find-the-winning-player-in-coin-game/description/
import pytest


def solve(x: int, y: int) -> str:
    return "Alice" if min(x, y // 4) & 1 else "Bob"


# 测试用例
def test_case_1():
    x, y = 2, 7
    expected = "Alice"
    assert solve(x, y) == expected


def test_case_2():
    x, y = 4, 11
    expected = "Bob"
    assert solve(x, y) == expected


if __name__ == "__main__":

    pytest.main()
