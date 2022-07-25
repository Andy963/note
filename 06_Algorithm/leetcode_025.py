#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : leetcode_025.py
# Author            : Andy
# Date              : 25.07.2022
# Last Modified Date: 25.07.2022
# Last Modified By  : Andy


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        protect = ListNode(0,head)
        last = protect
        while head:
            # 获取本组的end节点
            end = self.get_end(head,k)
            if not end:
                break
            # 下一组的头，在当前情况下即是当前组end的下一节点（反转前）
            next_group_head = end.next

            # 反转
            self.reverseList(head, end)
            # 反转后，last指向end, 此时end
            # 是开头，head则是结束
            last.next = end
            # head.next （因为反转过，事实上是结尾）
            # 指向下一组的开头
            head.next = next_group_head
            # 将last 右移到本级的结束
            last = head
            # 将head指向下一组的开头
            head = next_group_head
        return protect.next


    def get_end(self, head, k):
        #
        while head:
            k -= 1
            if k == 0:
                break
            head = head.next
        return head

    def reverseList(self, head: ListNode, end:ListNode) :
        # 负责反转组内元素
        if head == end:
            return
        last = head
        head = head.next
        while head != end:
            # 保存next节点
            next_head = head.next
            head.next = last
            last = head
            head = next_head
        end.next = last
