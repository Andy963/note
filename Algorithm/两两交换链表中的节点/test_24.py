#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date     : 2025/3/9
# @FileName : test_24.py # noqa
# Created by: Andy963

# ref: https://leetcode-cn.com/problems/swap-nodes-in-pairs/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solve(head):
    vir_node = ListNode(next=head)
    cur = vir_node

    while cur.next and cur.next.next:
        tmp1 = cur.next
        tmp3 = cur.next.next.next

        # link to node 2
        cur.next = cur.next.next
        # node 2 link to node 1
        cur.next.next = tmp1
        # node 1 link to node 3
        tmp1.next = tmp3
        cur = cur.next.next
    return vir_node.next


def are_lists_equal(l1, l2):
    while l1 and l2:
        if l1.val != l2.val:
            return False
        l1 = l1.next
        l2 = l2.next
    return l1 is None and l2 is None

def test_case1():
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    expected = ListNode(2, ListNode(1, ListNode(4, ListNode(3))))
    assert are_lists_equal(solve(head), expected)