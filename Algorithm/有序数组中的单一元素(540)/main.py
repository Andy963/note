#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date     : 2024/11/10
# @FileName : test_540_有序数组中的单一元素.py # noqa
# Created by: Andy963
# ref: https://leetcode.cn/problems/single-element-in-a-sorted-array/description/
"""
mid ^ 1 当mid是偶数时，mid ^ 1 等价于 mid = mid + 1
当mid是奇数时，mid ^ 1 等价于 mid= mid -1
nums = [1,1,2,2,3,4,4]
当数字正常时，如1下标为0,1, 2的下标是2，3，但3这个单个数字加入后，它的下标是4，导致
右侧的4的下标变成了5,6 即，单个数字左侧的下标是先侧后奇，而它后侧则相反是先奇后偶
而如果 nums[mid] == nums[mid^1] 则说明这对数字完整是重复的。
如果mid是偶数，那么mid^1是奇数，即mid 与mid+1 相等
如果mid是奇数，那么mid^1是偶数，即mid 与mid-1相等
都说明了这个数是重复的。所以单个数字肯定在它的右侧，相反将会在它的左侧,将r移动到mid
"""
def solve(nums:list[int])->int:
    l, r = 0, len(nums) -1
    while l < r :
        mid = (l + r ) // 2
        if nums[mid] == nums[mid ^ 1]:
            l = mid + 1
        else:
            r = mid
    return nums[l]

# 测试用例
def test_case_1():
    nums = [1,1,2,3,3,4,4,8,8]
    expected = 2
    assert solve(nums) == expected

def test_case_2():
    nums = [3, 3, 7, 7, 10, 11, 11]
    expected = 10
    assert solve(nums) == expected


if __name__ == '__main__':
    import pytest
    pytest.main()