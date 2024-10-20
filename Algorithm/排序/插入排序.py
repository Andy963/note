#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date     : 2024/10/20
# @FileName : 插入排序.py # noqa
# Created by; Andy963

"""
1. 分组：插入排序将待排序的数组分为两个部分：已排序部分和未排序部分。开始时，已排序部分只有一个元素，未排序部分包括剩余的所有元素。

2. 插入元素：从未排序部分中取出一个元素，然后将它插入到已排序部分中。插入的过程是比较和移动：
   ⦁ 从已排序部分的最后一个元素开始，向前比较，找到合适的位置（即插入位置）使得已排序部分仍然保持有序。
   ⦁ 若已排序部分中元素大于待插入的元素，便将这个元素后移。
   ⦁ 继续比较，直到找到合适位置或遍历完已排序部分。

3. 重复步骤：重复以上步骤，直到未排序部分为空，此时已排序部分即为最终的排序结果
"""
def solve(arr:list):
    n = len(arr)
    for i in range(1, n):
        # 对已排序的遍历
        for j in range(i):
            # 如果有元素大于待插入的值，那么要将这个元素插入到这里
            # 后面的元素右移
            if arr[j] > arr[i]:
                # 记住arr[i]，将其它元素后移
                tmp = arr[i]
                for k in range(i, j, -1):
                    arr[k] = arr[k - 1]
                # 插入该元素
                arr[j] = tmp
                # 插入完成，跳出循环
                break
    return arr

# 测试用例
def test_case_1():
    arr = [1,0,3,5,4,7]
    expected_out = [0,1,3,4,5,7]
    assert solve(arr) == expected_out

def test_case_2():
    arr = [1,0,-3,5,4,-7]
    expected_out = [-7, -3, 0, 1, 4, 5]
    assert solve(arr) == expected_out

def test_case_3():
    arr = [1,0,0,-1]
    expected_out = [-1, 0, 0, 1]
    assert solve(arr) == expected_out


if __name__ == '__main__':
    import pytest
    pytest.main()
