#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : leetcode_206.py
# Author            : Andy
# Date              : 24.07.2022
# Last Modified Date: 24.07.2022
# Last Modified By  : Andy

"""
主体思路：先保存下一节点，然后将头节点指向空
然后last节点右移一步，指向当前head
head 节点再右移一步（事先保存好了节点）
重复以上步骤
"""

class Solution:
    def reverseList(self,head:ListNode) -> ListNode:
        last = None
        while head:
            #保存下一个节点
            next_head = head.next
            head.next = last
            last = head
            head = next_head
        return last
