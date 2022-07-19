#!/usr/bin/env python
# coding: utf-8 
# Create by Andy963 @2022-07-15 22:41:02

def to_str(n,base):
    convert_str = "0123456789ABCDEF"
    # 结束条件
    if n < base:
        return convert_str[n]
    else:
        # 调用自身，前面为改变的条件
        return to_str(n//base, base) + convert_str[n%base]
