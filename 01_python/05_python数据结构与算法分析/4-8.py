#!/usr/bin/env python
# coding: utf-8 
# Create by Andy963 @2022-07-20 23:15:27


def move_tower(height, from, to, with):
    if height >= 1:
        # 将高度-1的借助中间柱移动到目标
        move_tower(height-1, from, with, to)
        move_disk(from, to)
        # 移回原来柱
        move_tower(height-1, with, to, from)

def move_disk(fp,tp):
    print(f"moving disk from {fp} to {tp}")

