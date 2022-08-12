#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : leetcode_078.py
# Author            : Andy
# Date              : 2022.08.12
# Last Modified Date: 2022.08.12
# Last Modified By  : Andy


class Solution:
    def subsets(self, nums):
        path = []
        ans = []

        def find_subsets(ans, nums, index):
            if index == len(nums):
                ans.append(path[:])
                return

            #不选择
            find_subsets(ans, nums, index+1)
            # 选择，加入到路径中
            path.append(nums[index])
            find_subsets(ans, nums, index+1)
            # 还原
            path.pop()

        find_subsets(ans, nums, 0)
        return ans


