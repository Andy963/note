#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : leetcode_020.py
# Author            : Andy
# Date              : 27.07.2022
# Last Modified Date: 27.07.2022
# Last Modified By  : Andy


class Solution:
    def isValid(self, s:str) -> bool:
        stack = []
        for ch in s:
            if ch in "([{":
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                if ch == ')':
                    if stack[-1] != '(':
                        return False
                elif ch == ']':
                    if stack['-1'] != '[':
                        return False
                elif ch == '}':
                    if stack[-1] != '{':
                        return False
        return len(stack) == 0
