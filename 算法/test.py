#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date     : 2024/9/20
# @FileName : test.py # noqa
# Created by; Andy963

def fn():

    t = []

    i = 0

    while i < 2:

        t.append(lambda x: print(i*x,end=","))

        i += 1

    return t

print(fn())