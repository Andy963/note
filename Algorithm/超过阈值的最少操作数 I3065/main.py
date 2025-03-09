#!/usr/bin/env python3
# -*- encoding=utf8 -*-

'''
File              : main.py
Author            : Andy963
Created time      : 2024-12-08 08:52:07
Last Modified by  : Andy963
Last Modified time: 2024-12-08 08:52:36
'''
from typing import List
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return len(list(filter(lambda x: x < k, nums)))