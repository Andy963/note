#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date     : 2024/9/22
# @FileName : 计算堆栈中的剩余数字.py # noqa
# Created by; Andy963
"""
向一个空栈中依次存入正整数，假设入栈元素n(1<=n<=2^31-1)按顺序依次为nx...n4、n3、n2、n1,
每当元素入栈时，如果n1=n2+...+ny(y的范围[2,x]，1<=x<=1000)，则n1~ny全部元素出栈，重新入栈新元素m(m=2*n1)。
如：依次向栈存入6、1、2、3,
当存入6、1、2时，栈底至栈顶依次为[6、1、2]；
当存入3时，3=2+1，3、2、1全部出栈，重新入栈元素6(6=2*3)，此时栈中有元素6；因为6=6，所以两个6全部出栈，存入12，最终栈中只剩一个元素12。
输入描述：
使用单个空格隔开的正整数的字符串，如"5 6 7 8"， 左边的数字先入栈，输入的正整数个数为x，1<=x<=1000。
输出描述：
最终栈中存留的元素值，元素值使用空格隔开，如"8 7 6 5"， 栈顶数字在左边。
补充说明：
示例1
输入：
5 10 20 50 85 1
输出：
1 170
说明：
5+10+20+50=85， 输入85时，5、10、20、50、85全部出栈，入栈170，最终依次出栈的数字为1和170。
示例2
输入：
6 7 8 13 9
输出：
9 13 8 7 6
说明：
示例3
输入：
1 2 5 7 9 1 2 2
输出：
4 1 9 14 1
"""
import unittest


def solve(nums):
    stack = []
    for n in nums:
        total = n
        matched = False
        # 从后依次往回减
        # length = len(stack)
        # # 通过total 来终于不必要的循环，即当total<0时不会继续循环
        # while length > 0 and total:
        #     total -= stack[length-1]
        #     if total == 0:
        #         stack = stack[:length-1]
        #         stack.append(n*2)
        #         break
        #     length -= 1
        # else:
        #     stack.append(n)
        # 有个问题，当total <0 时，仍然在做无意义的循环，必须要把整个stack遍历完，浪费
        for i in range(len(stack)-1,-1,-1):
            total -= stack[i]
            if total == 0:
                # 如果遇到减到0的情况，说明存在这样的连续数字，则将这些数字移除，
                # 再将它的2倍入栈
                stack = stack[:i]
                stack.append(n*2)
                matched = True
                break
            elif total < 0:
                break
        if not matched:
            stack.append(n)
    return stack[::-1]







class TestSolve(unittest.TestCase):
    def test_case_0(self):
        nums = [3,2,1,6]
        expected_output = [12]
        self.assertEqual(solve(nums), expected_output)

    def test_case_1(self):
        nums = [5, 10, 20, 50, 85, 1]
        expected_output = [1, 170]
        self.assertEqual(solve(nums), expected_output)

    def test_case_2(self):
        nums = [6, 7, 8, 13, 9]
        expected_output = [9, 13, 8, 7, 6]
        self.assertEqual(solve(nums), expected_output)

    def test_case_3(self):
        nums = [ 1, 2, 5, 7, 9, 1, 2, 2]
        expected_output = [4, 1, 9, 14, 1]
        self.assertEqual(solve(nums), expected_output)


if __name__ == '__main__':
    unittest.main()