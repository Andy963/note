#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : leetcode_155.py
# Author            : Andy
# Date              : 27.07.2022
# Last Modified Date: 27.07.2022
# Last Modified By  : Andy

# 主体思路是用一个额外的栈存储一个最小前缀值，即当前数是前面n个数中最小值
# 在pop时两个栈同时pop
# 在push时，一个正常存储，另一个则只存当前值与栈底元素中最小的那个值

class Minstack:
    def __init__(self):
        self.__stack = []
        self.__min_stack = []

    def push(self, val:int) ->None:
        self.__stack.append(val)
        if not self.__min_stack:
            self.__min_stack.append(val)
        else:
            self.__min_stack.append(min(val, self.__min_stack[-1]))

    def pop(self) ->None:
        self.__stack.pop()
        self.__min_stack.pop()

    def top(self) ->int:
        return self.__min_stack[-1]
            
    def getMin(self) -> int:
        return self.__min_stack[-1]
