#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date     : 2025/3/9
# @FileName : test_19.py # noqa
# Created by: Andy963

# ref https://leetcode.cn/problems/remove-nth-node-from-end-of-list/description/
"""
题目:
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve(head, n):
    # define a virtual node
    vir_node = ListNode(next=head)
    slow = fast = vir_node
    # let fast move n steps , so when the fast move to the end, the slow will at the front of the node which need to be deleted
    for _ in range(n+1):
        fast = fast.next

    # move fast & slow
    while fast:
        slow = slow.next
        fast = fast.next

    # delete the node
    slow.next = slow.next.next
    return vir_node.next

def are_lists_equal(l1, l2):
    while l1 and l2:
        if l1.val != l2.val:
            return False
        l1 = l1.next
        l2 = l2.next
    return l1 is None and l2 is None

def test_case1():
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    n = 2
    expected = ListNode(1, ListNode(2, ListNode(3, ListNode(5))))
    assert are_lists_equal(solve(head, n), expected)

def test_case2():
    head = ListNode(1)
    n = 1
    expected = None
    assert are_lists_equal(solve(head, n), expected)

def test_case3():
    head = ListNode(1, ListNode(2))
    n = 1
    expected = ListNode(1)
    assert are_lists_equal( solve(head, n) , expected)