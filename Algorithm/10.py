#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date     : 2024/9/21
# @FileName : 10.py # noqa
# Created by; Andy963

"""
孙悟空爱吃蟠桃，有一天趁着蟠桃园守卫不在来偷吃。已知蟠桃园有N颗桃树，每颗树上都有桃子，守卫将在H小时后回来。
孙悟空可以决定他吃蟠桃的速度K（个/小时），每个小时选一颗桃树，并从树上吃掉K个，如果树上的桃子少于K个，则全部吃掉，并且这一小时剩余的时间里不再吃桃。
孙悟空喜欢慢慢吃，但又想在守卫回来前吃完桃子。
请返回孙悟空可以在H小时内吃掉所有桃子的最小速度K（K为整数）。如果以任何速度都吃不完所有桃子，则返回0。
输入描述：
第一行输入为N个数字，N表示桃树的数量，这N个数字表示每棵桃树上蟠桃的数量。
第二行输入为一个数字，表示守卫离开的时间H。
其中数字通过空格分割，N、H为正整数，每棵树上都有蟠桃，且0<N<10000，0<H<10000。
输出描述：
吃掉所有蟠桃的最小速度K，无解或输入异常时输出0。
补充说明：
示例1
输入：
2 3 4 5
4
输出：
5
说明：
示例2
输入：
2 3 4 5
3
输出：
0
说明：
示例3
输入：
30 11 23 4 20
6
输出：
23
说明：
"""
import unittest


def solve(lis,n):
    if n < len(lis):
        return 0
    elif n == len(lis):
        return max(lis)
    else:
        l, r, ans = 0, max(lis), max(lis)
        while l <= r:
            mid = (l + r ) // 2
            wast_time = 0
            for x in lis:
                wast_time += (x + mid -1 ) // mid
            if wast_time <= n:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans


# 单元测试
class TestSolve(unittest.TestCase):

    def test_case_1(self):
        lis = [2, 3, 4, 5]
        tim = 4
        expected_output = 5
        self.assertEqual(solve(lis, tim), expected_output)

    def test_case_2(self):
        lis = [2, 3, 4, 5]
        tim = 3
        expected_output = 0
        self.assertEqual(solve(lis, tim), expected_output)

    def test_case_3(self):
        lis = [30, 11, 23, 4, 20]
        tim = 6
        expected_output = 23
        self.assertEqual(solve(lis, tim), expected_output)


if __name__ == '__main__':
    unittest.main()

