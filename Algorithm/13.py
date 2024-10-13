#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date     : 2024/9/22
# @FileName : 13.py # noqa
# Created by; Andy963
"""
小王设计了一个简单的猜字谜游戏，游戏的谜面是一个错误的单词，比如 nesw，
玩家需要猜出谜底库中正确的单词。猜中的要求如下.对于某个谜面和谜底单词，满足下面任一条件都表示猜中:
1、变换顺序以后一样的，比如通过变换 w和e的顺序，“nwes”跟“news”是可以完全对应的:
2、字母去重以后是一样的，比如“woood”和“wood”是一样的，它们去重后都是“wod'请你写一个程序帮忙在谜底库中找到正确的谜底。
谜面是多个单词，都需要找到对应的谜底，如果找不到的话，返回“not found
输入描述
1.谜面单词列表，以“，”分隔
2.谜底库单词列表，以“，”分隔
输出描述
匹配到的正确单词列表，以“，”分隔
如果找不到，返回“not found'
备注
1.单词的数量 N 的范围:0<N<1000
2.词汇表的数量 M 的范围:0<M<1000
3.单词的长度 P 的范围:0<P<20
4.输入的字符只有小写英文字母，没有其他字符
示例1
输入
Conection
connection,today
输出
Connection
说明
示例2
输入
bdni,wooood
bind,wrong,wood
输出
bind,wood
说明
"""
import unittest


def solve(targets,sources):
    ans = []
    t_ = [sorted(t) for t in targets]
    for s in sources:
        # 排序后相同
        if sorted(s) in t_:
            ans.append(s)
            continue
        # 去重
        for t in t_:
            if set(t) == set(s):
                ans.append(s)
                break
    if ans:
        return ','.join(ans)
    else:
        return 'not found'


class TestSolve(unittest.TestCase):
    def test_case_1(self):
        targets = ["conection",]
        source = ['connection','today']
        expected_output = 'connection'
        self.assertEqual(solve(targets,source), expected_output)

    def test_case_2(self):
        targets = ['bdni','wooood']
        source = ['bind','wrong','wood']
        expected_output = 'bind,wood'
        self.assertEqual(solve(targets,source), expected_output)

if __name__ == '__main__':
    unittest.main()