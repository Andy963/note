#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date     : 2024/9/27
# @FileName : 游戏分组.py # noqa
# Created by; Andy963
"""
部门准备举办一场王者荣耀表演赛，有10名游戏爱好者参与，分为两队，每队5人。
每位参与者都有一个评分，代表着他的游戏水平。为了表演赛尽可能精彩，
我们需要把10名参赛者分为实力尽量相近的两队。一队的实力可以表示为这一队5名队员的评分总和。
现在给你10名参与者的游戏水平评分，请你根据上述要求分队，最后输出这两组的实力差绝对值。
例：10名参赛者的评分分别为5 1 8 3 4 6 7 10 9 2，分组为（1 3 5 8 10）（2 4  6 7 9）
两组实力差最小，差值为1。有多种分法，但实力差的绝对值最小为1。
输入描述：
10个整数，表示10名参与者的游戏水平评分。范围在[1, 10000]之间
输出描述：
1个整数，表示分组后两组实力差绝对值的最小值。
示例1
输入：
1 2 3 4 5 6 7 8 9 10
输出：
1
说明：
10名队员分成两组，两组实力差绝对值最小为1。
"""

import unittest
from itertools import combinations


# def solve(scores,index, t1,t2):
#     if len(t1) == 5 and len(t2) == 5:
#         return abs(sum(t1) - sum(t2))
#
#     if index == len(scores):
#         return float('inf')
#
#     if len(t1) == 5:
#         return solve(scores, index+1, t1, t2+[scores[index]])
#
#     if len(t2) == 5:
#         return solve(scores, index+1, t1+[scores[index]], t2)
#
#     d1 = solve(scores, index+1, t1+[scores[index]], t2)
#     d2 = solve(scores, index+1, t1, t2+[scores[index]])
#
#     return min(d1,d2)

def solve(scores):
    total = sum(scores)
    min_diff = float('inf')
    best_group = None

    # 遍历所有可能的5人组合
    for combo in combinations(scores, 5):
        team1_sum = sum(combo)
        team2_sum = total - team1_sum
        diff = abs(team1_sum - team2_sum)
        if diff < min_diff:
            min_diff = diff
            best_group = combo

    # 构建两个小组
    team1 = list(best_group)
    # 如果有重复数字，这里会出bug
    # team2 = [score for score in scores if score not in team1]

    print(team1, team2)
    return min_diff

class TestSolve(unittest.TestCase):
    # def test_case_1(self):
    #     nums = [5, 1, 8, 3, 4, 6, 7, 10, 9 ,2]
    #     expected_output = 1
    #     self.assertEqual(solve(nums), expected_output)
    #
    # def test_case_2(self):
    #     nums = [9, 1, 8, 3, 4, 6, 7, 10, 9 ,2]
    #     expected_output = 1
    #     self.assertEqual(solve(nums), expected_output)

    def test_case_3(self):
        nums = [9, 3, 8, 3, 4, 6, 7, 10, 9 ,2]
        expected_output = 1
        self.assertEqual(solve(nums), expected_output)

if __name__ == '__main__':
    unittest.main()