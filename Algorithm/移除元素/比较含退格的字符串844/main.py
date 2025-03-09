#!/usr/bin/env python3
# -*- encoding=utf8 -*-

"""
File              : main.py
Author            : Andy963
Created time      : 2024-12-07 16:50:16
Last Modified by  : Andy963
Last Modified time: 2024-12-07 17:06:02
"""

import pytest


class Solution:
    def solve2(self, s: str):
        # simulate a stack
        rs = []
        for i in range(len(s)):
            if s[i] != "#":
                rs.append(s[i])
            else:
                rs.pop()
        return rs

    def backspaceCompare2(self, s: str, t: str) -> bool:
        return self.parse(s) == self.parse(t)

    def solve(self, s: list):
        n = len(s)
        slow, fast = -1, 0
        while fast < n:
            if s[fast] != "#":
                slow += 1
                s[slow] = s[fast]
            else:
                if slow >= 0:
                    slow -= 1
            fast += 1
        print(s[:slow+1])
        return s[: slow + 1]

    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.solve(list(s)) == self.solve(list(t))


sl = Solution()


def test_case1():
    s = "ab#c"
    t = "ad#c"
    expected = True
    assert expected == sl.backspaceCompare(s, t)


def test_case2():
    s = "ab##"
    t = "c#d#"
    expected = True
    assert expected == sl.backspaceCompare(s, t)


def test_case3():
    s = "a#c"
    t = "b"
    expected = False
    assert expected == sl.backspaceCompare(s, t)


if __name__ == "__main__":
    pytest.main(
        [
            "-v",
            '-s'
        ]
    )
