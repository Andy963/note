#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date     : 2024/9/26
# @FileName : 39-2.py # noqa
# Created by; Andy963

"""
输入字符串s，输出s中包含所有整数的最小和

说明

1. 字符串s，只包含 a-z A-Z +- ；

2. 合法的整数包括

    1） 正整数 一个或者多个0-9组成，如 0 2 3 002 102

    2）负整数 负号 - 开头，数字部分由一个或者多个0-9组成，如 -0 -012 -23 -00023

输入描述：

包含数字的字符串

输出描述：

所有整数的最小和

示例1

输入：

bb1234aa
输出：

10
说明：

示例2

输入：

bb12-34aa
输出：

-31
说明：

1+2+（-34） = 31
"""



def main():


    flag = False
    count = 0
    temp = 0

    for i in range(len(input)):
        if input[i].islower() or input[i].isupper():
            count += temp
            flag = False
            temp = 0
        if input[i] == '+':
            count += temp
            flag = False
            temp = 0
        if input[i] == '-':
            if flag == False:
                flag = True
            else:
                count += temp
                flag = True
                temp = 0
        if input[i].isdigit():
            if flag:
                temp = temp * 10 - int(input[i])
            else:
                count += int(input[i])

    if temp != 0:
        count += temp
    print(count)


if __name__ == "__main__":
    main()
