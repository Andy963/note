#!/usr/bin/env python
# coding: utf-8 
# Create by Andy963 @2022-07-15 23:00:43

from pythonds.basic import Stack

rStack = Stack()


def to_str(n, base):
   convert_str = "0123456789ABCDEF"
   if n < base:
       rStack.push(convert_str[n])
   else:
       rStack.push(convert_str[n % base])
       to_str(n//base, base)
