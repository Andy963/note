#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date     : 2024/9/20
# @FileName : 08.py # noqa
# Created by; Andy963
"""
小明从糖果盒中随意抓一把糖果，每次小明会取出一半的糖果分给同学们。
当糖果不能 平均分配只时，小明可以选择从糖果盒中(假设盒中糖果足够)取出一个糖果或放回一个糖果。
小明最少需要多少次(取出、放回和平均分配均记一次)，能将手中糖果分至只剩一颗。
输入描述
抓取的糖果数(<10000000000):15
输出描述
最少分至一颗糖果的次数:5
示例
输入
15
输出
5
说明
1.15+1=16;
2.16/2=8;
3.8/2=4;
4.412=2;
5.2/2=1;
"""
import sys

def min_steps_to_one(n):
    steps = 0
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            # 对于奇数情况，选择加1或减1，选择使得操作更少的一条路径
            # 比较 (n+1)/2 和 (n-1)/2 哪个操作次数更少
            if (n == 3) or ((n - 1) // 2 % 2 == 0):
                n -= 1
            else:
                n += 1
        steps += 1
    return steps

def main():
    input = sys.stdin.read
    candy = int(input())
    steps = min_steps_to_one(candy)
    print(steps)


if __name__ == '__main__':
    main()