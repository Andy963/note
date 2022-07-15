#!/usr/bin/python
# coding:utf-8

from pythonds.basic import Deque


def pal_checker(s: str) -> bool:
    d = Deque()
    for c in s:
        d.addRear(c)
    flag = True
    while d.size() > 1 and flag:
        first = d.removeFront()
        last = d.removeRear()
        if first != last:
            flag = False
    return flag
