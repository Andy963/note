#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : leetcode_000.py
# Author            : Andy
# Date              : 2022.08.09
# Last Modified Date: 2022.08.09
# Last Modified By  : Andy


class Solution:
    def robotSim(self, commands, obstacles):
        blockers = {tuple(o): 0 for o in obstacles}
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        result = 0
        dr = 0

        for cmd in commands:
            if cmd > 0:
                for i in range(cmd):
                    next_x = dx[dr]
                    next_y = dy[dr]

                    if(next_x, next_y) in blockers:
                        break
                    x, y = next_x, next_y
                    result = max(result, x*x+y*y)
            elif cmd == -1:
                dr = (dr + 1) % 4
            else:
                dr = (dr - 1 + 4) % 4
        return result
