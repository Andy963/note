#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : leetcode_048.py
# Author            : Andy
# Date              : 2022.08.31
# Last Modified Date: 2022.08.31
# Last Modified By  : Andy


class Solution:

    def rotate(self, matrix):
        rows, cols = len(matrix), len(matrix[0])

        def transpost(matrix):
            # 行列转置
            # TODO j为什么是到i+1,目前还没太明白
            for i in range(rows):
                for j in range(i + 1, cols):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        def reverse(matrix):
            # 前后倒置
            for i in range(len(matrix)):
                matrix[i] = matrix[i][::-1]

        transpost(matrix)
        reverse(matrix)
