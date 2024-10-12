#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date     : 2024/9/22
# @FileName : 16.py # noqa
# Created by; Andy963
"""
小明来到某学校当老师，需要将学生按考试总分或单科分数进行排名，你能帮帮他吗？
输入描述：
第1行输入两个整数，学生人数n和科目数量m。0<n<100,0<m<10
第2行输入m个科目名称，彼此之间用空格隔开。科目名称只由英文字母构成，单个长度不超过10个字符。科目的出现顺序和后续输入的学生成绩一一对应。不会出现重复的科目名称。
第3行开始的n行，每行包含一个学生的姓名和该生m个科目的成绩（空格隔开），学生不会重名。学生姓名只由英文字母构成，长度不超过10个字符。成绩是0~100的整数，依次对应第2行中输入的科目。
第n+2行，输入用作排名的科目名称。若科目不存在，则按总分进行排序。
输出描述：
输出一行，按成绩排序后的学生名字，空格隔开。成绩相同的按照学生姓名字典顺序排序。
补充说明：
 收起
示例1
输入：
3 2
yuwen shuxue
fangfang 95 90
xiaohua 88 95
minmin 100 82
shuxue
输出：
xiaohua fangfang minmin
说明：
按shuxue成绩排名，依次是xiaohua、fangfang、minmin
示例2
输入：
3 2
yuwen shuxue
fangfang 95 90
xiaohua 88 95
minmin 90 95
zongfen
输出：
fangfang minmin xiaohua
说明：
排序科目不存在，按总分排序，fangfang和minmin总分相同，按姓名的字典顺序，fangfang排在前面
"""
import unittest


def solve():
    pass


class TestSolve(unittest.TestCase):

    def test_case_1(self):
        nums = [4, 1, 3, 5, 2]
