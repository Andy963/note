#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : leetcode_046.py
# Author            : Andy
# Date              : 2022.08.15
# Last Modified Date: 2022.08.15
# Last Modified By  : Andy

# ref: https://leetcode.cn/problems/permutations/description/


class Solution:
    def permute(self, nums):
        n = len(nums)
        path = []
        result = []

        def find(index):
            # stop condition
            if index == n:
                result.append(path[:])
                return

            for i in range(n):
                if nums[i] in path:
                    continue
                path.append(nums[i])
                find(index + 1)
                path.pop()

        find(0)
        return result

    def backtrack(self, nums, path, used, result):
        n = len(nums)
        if len(path) == n:
            result.append(path[:])
            return

        for i in range(n):
            if used[i]:
                continue
            used[i] = True
            path.append(nums[i])
            self.backtrack(nums, path, used, result)
            path.pop()
            used[i] = False

    def permute2(self, nums):
        result = []
        self.backtrack(nums, [], [False] * len(nums), result)
        return result


# ref: https://leetcode.cn/problems/permutations-ii/submissions/215956444/
