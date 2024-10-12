#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date     : 2024/9/26
# @FileName : 数大雁.py # noqa
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
说明：
"""
import unittest
from collections import deque


def solve(s: str) -> int:
    # 计数器初始化：q, u, a, c, k 分别用于统计每个字符的数量
    q = u = a = c = k = 0
    max_ducks = 0  # 最大并发鸭子数量
    Q = deque()  # 用于记录每个 'q' 的位置
    cnt = [0] * (len(s) + 1)  # 前缀和数组，存储每个位置之前完整的 'quack' 的数量

    for i in range(len(s)):
        cnt[i + 1] = cnt[i]  # 更新前缀和，表示到当前位置为止的完整 'quack' 数量

        if s[i] == 'q':  # 如果当前字符是 'q'
            q += 1  # 增加 'q' 的计数
            Q.append(i)  # 记录 'q' 的位置
        elif s[i] == 'u' and q > u:  # 如果当前字符是 'u'，且 'q' 的数量多于 'u'
            u += 1  # 增加 'u' 的计数
        elif s[i] == 'a' and u > a:  # 如果当前字符是 'a'，且 'u' 的数量多于 'a'
            a += 1  # 增加 'a' 的计数
        elif s[i] == 'c' and a > c:  # 如果当前字符是 'c'，且 'a' 的数量多于 'c'
            c += 1  # 增加 'c' 的计数
        elif s[i] == 'k' and c > k:  # 如果当前字符是 'k'，且 'c' 的数量多于 'k'
            k += 1  # 增加 'k' 的计数
            cnt[i + 1] += 1  # 增加完整 'quack' 的数量

            q_first = Q.popleft()  # 获取最早的 'q' 位置
            # 计算当前区间内并发的鸭子数量，并更新最大并发数量
            max_ducks = max(max_ducks, cnt[i + 1] - cnt[q_first])
        elif s[i] not in 'uack':  # 非法字符，直接返回 -1
            return -1

    return max_ducks if max_ducks > 0 else -1  # 如果没有找到任何完整的 'quack'，返回 -1；否则返回最大并发鸭子数量

class TestSolve(unittest.TestCase):
    def test_case_1(self):
        s = "quackquack"
        expected_output = 1
        self.assertEqual(solve(s), expected_output)

    def test_case_2(self):
        s = "qaauucqckk"
        expected_output = -1
        self.assertEqual(solve(s), expected_output)

    def test_case_3(self):
        s = "qququaauqccauqkkcauqqkcauuqkcaaukccakkck"
        expected_output = 5
        self.assertEqual(solve(s), expected_output)



# 主函数，读取输入并输出结果
if __name__ == "__main__":
    unittest.main()