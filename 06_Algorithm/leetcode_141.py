#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : leetcode_141.py
# Author            : Andy
# Date              : 27.07.2022
# Last Modified Date: 27.07.2022
# Last Modified By  : Andy

# 主体思路是：一直遍历，如果有环，那么跑得快的一定会追上跑得慢的
# 这里直接用head, fast就可以了，head走一步，fast走两步，边界条件
# 是fast, fast.next不为空，如果fast.next为空，fast.next.next会报错

class Solution:
    def hasCycle(self, head):
        fast = head 
        while fast and fast.next:
            head = head.next
            fast = fast.next.next
            if fast is head:
                return True
        return False
