#!/usr/env python
#!coding:utf-8


def list_sum(num_list:list) -> int:
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + list_sum(num_list[1:])
