#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date     : 2024/9/23
# @FileName : 18.py # noqa
# Created by; Andy963
"""
一群大雁往南飞,给定一个字符串记录地面上的游客听到的大雁叫声,请给出叫声最少由几只大雁发出。具体的
大雁发出的完整叫声为”quack“,因为有多只大雁同一时间嘎嘎作响,所以字符串中可能会混合多个”quack”
大雁会依次完整发出”quack”,即字符串中q,u,a,c,k这5个字母按顺序完整存在才能计数为一只大雁如果不完整或者没有按顺序则不予计数。
如果字符串不是由q,u,a,ck字符组合而成,或者没有找到一只大雁,请返回-1
输入描述
一个字符串,包含大雁quack的叫声。1<=字符串长度<=1000,字符串中的字符只有q,u,a,C,k
输出描述
大雁的数量
示例1
输入
quackquack
输出
1
说明：无
示例2
输入
qaauucqckk
输出
-1
说明：
示例3
输入
quacqkuac
输出
1
说明：
输入
qququaauqccauqkkcauqqkcauuqkcaaukccakkck
输出
5
"""
import unittest
from collections import deque


def solve(s):
    q = u = a = c = k = 0
    max_ducks = 0
    Q = deque()
    cnt = [0] * (len(s) +1)

    for i in range(len(s)):
        cnt[i+1] = cnt[i]

        if s[i] == 'q':
            q += 1
            Q.append(i)
        elif s[i] == 'u' and q > u:
            u += 1
        elif s[i] == 'a' and u > a:
            a += 1
        elif s[i] == 'c' and a > c:
            c += 1
        elif s[i] == 'k' and c > k:
            k += 1
            cnt[i+1] = cnt[i] + 1
            q_first  = Q.popleft()
            max_ducks = max(max_ducks, cnt[i+1] - cnt[q_first])
        elif s[i] not in 'uack':
            return -1
    return max_ducks if max_ducks > 0 else -1

class TestSolve(unittest.TestCase):
    def test_case_1(self):
        nums = "qququaauqccauqkkcauqqkcauuqkcaaukccakkck"
        expected_output = 5
        self.assertEqual(solve(nums), expected_output)

    def test_case_2(self):
        nums = "qaauucqckk"
        expected_output = -1
        self.assertEqual(solve(nums), expected_output)