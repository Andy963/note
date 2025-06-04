#!/usr/bin/env python3
# -*- encoding=utf8 -*-
# File              : test_2001.py
# Author            : Andy963
# Created time      : 2025-06-04 21:59:20
# Last Modified by  : Andy963
# Last Modified time: 2025-06-04 22:06:08

# ref: https://leetcode.cn/problems/number-of-pairs-of-interchangeable-rectangles/description/

import pytest
from collections import defaultdict
from typing import List


class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        cnt = defaultdict(int)
        ans = 0
        for w, h in rectangles:
            if w/h in cnt:
                ans += cnt[w/h]
            cnt[w/h] += 1
        return ans


def test_case1():
    rectangles = [[4,8],[3,6],[10,20],[15,30]]
    expected = 6
    result = Solution().interchangeableRectangles(rectangles)
    assert result == expected, f"Expected {expected}, but got {result}"


def test_case2():
    rectangles = [[4,5],[7,8]]
    expected = 0
    result = Solution().interchangeableRectangles(rectangles)
    assert result == expected, f"Expected {expected}, but got {result}"


if __name__ == '__main__':
     pytest.main()