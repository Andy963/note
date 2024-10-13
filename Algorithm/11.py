#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date     : 2024/9/21
# @FileName : 11.py # noqa
# Created by; Andy963
"""
C 语言有一个库函数Q: char *strstr(const char *haystack,const char *needle)，
实现在字符串 haystack 中查找第一次出现字符串 needle 的位置，如果未找到则返回 null。
现要求实现一个strstr的增强函数，可以使用带可选段的字符串来模糊査询，
与strstr一样返回首次查找到的字符串位置可选段使用“"“标识，
表示该位置是可选段中任意一个字符即可满足匹配条件。
比如“a[bc]"表示可以匹配“ab”或"ac”注意目标字符串中可选段可能出现多次。
输入描述
与strstr函数只一样，输入参数是两个字符串指针，分别是源字符串和目标字符串
输出描述
与strstr函数不同，返回的是源字符串中，匹配子字符串相对于源字符串地址的偏移(从0开始算)，如果没有匹配返回-1。
补充说明:
源字符串中必定不包含”;目标字符串中"必定成对出现，且不会出现嵌套。
输入的字符串长度在[1,100]之间。
示例1
输入
abcd
b（cd）
输出
1
说明
相当于是在源字符串中查找bc或者bd，bc子字符串相对于abcd的偏移是1
"""
import unittest


def solve(haystack, needle):
    n = len(haystack)
    l = len(needle)
    for i in range(n):
        k = i
        j = 0 # 遍历 needle 中的每个字符
        match = True
        while  j < l and  k < n:
            if needle[j] == '[':
                option_match = False
                j += 1
                while needle[j] != ']':
                    if haystack[k] == needle[j]:
                        option_match = True
                    j += 1
                if not option_match:
                    match = False
                    break
                j += 1
            else:
                if haystack[k] != needle[j]:
                    match = False
                    break
                j += 1
            k += 1
        if match:
            return i
    return -1




class TestSolve(unittest.TestCase):
    def test_case_1(self):
        haystack = "abcd"
        needle = "b[c]d"
        expected_output = 1
        self.assertEqual(solve(haystack, needle), expected_output)

    def test_case_2(self):
        haystack = "abcd"
        needle = "bd[dc]"
        expected_output = -1
        self.assertEqual(solve(haystack, needle), expected_output)


if __name__ == '__main__':
    unittest.main()