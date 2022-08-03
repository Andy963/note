#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : leetcode_167.py
# Author            : Andy
# Date              : 03.08.2022
# Last Modified Date: 03.08.2022
# Last Modified By  : Andy


class Solution:
    def twoSum(self, numbers, target):
        left, right = 0, len(numbers) -1
        while left < right:
            tmp = numbers[left] + numbers[right]
            #结果大了，右边向左移
            #结果小了，左边右移
            if tmp > target:
                right -= 1
            elif tmp < target:
                left += 1
            elif tmp == target:
                return [left+1, right+1]
