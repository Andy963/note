#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date     : 2024/9/19
# @FileName : 06.py # noqa
# Created by; Andy963

"""
主管期望你来实现英文输入法单词联想功能。需求如下：

依据用户输入的单词前缀，从已输入的英文语句中联想出用户想输入的单词，按字典序输出联想到的单词序列，如果联想不到，请输出用户输入的单词前缀。

注意：

1.  英文单词联想时，区分大小写

2.  缩略形式如”don't”，判定为两个单词，”don”和”t”

3.  输出的单词序列，不能有重复单词，且只能是英文单词，不能有标点符号

输入描述：

输入为两行。

首行输入一段由英文单词word和标点符号组成的语句str；

接下来一行为一个英文单词前缀pre。

0 < word.length() <= 20

0 < str.length <= 10000

0 < pre <= 20

输出描述：

输出符合要求的单词序列或单词前缀，存在多个时，单词之间以单个空格分割

示例1

输入：

I love you
He
输出：

He
说明：

从用户已输入英文语句”I love you”中提炼出“I”、“love”、“you”三个单词，接下来用户输入“He”，从已输入信息中无法联想到任何符合要求的单词，因此输出用户输入的单词前缀。

示例2

输入：

The furthest distance in the world, Is not between life and death, But when I stand in front of you, Yet you don't know that I love you.
f
输出：

front furthest
说明：

从用户已输入英文语句”The furthestdistance in the world, Is not between life and death, But when I stand in frontof you, Yet you dont know that I love you.”中提炼出的单词，符合“f”作为前缀的，有“furthest”和“front”，按字典序排序并在单词间添加空格后输出，结果为“frontfurthest”。
解题思路：

1. 分词处理：

使用正则表达式对输入的文本进行分词。正则表达式 `\b\w+('\w+)?\b` 用于匹配单词，其中允许单词中包含撇号（如英文缩写 "it's"）。

对于包含撇号的单词，将其分割为两部分，例如 "it's" 分割为 "it" 和 "s"。

2. 前缀过滤：

遍历所有分词得到的单词列表。

检查每个单词是否以给定的前缀开始。如果是，将其添加到结果集合中。使用集合是为了自动去除重复的单词。

3. 结果排序和输出：

将结果集合转换为列表，并进行排序。这是为了输出时单词按字典序排列。

如果结果集为空（即没有单词以给定的前缀开始），则输出前缀本身。

如果结果集不为空，则输出所有满足条件的单词，单词之间用空格分隔。
"""

import re


# 使用正则表达式提取单词，并处理包含撇号的单词
def tokenize(text):
    tokens = []
    word_regex = re.compile(r"\b\w+('\w+)?\b")  # 匹配单词，允许撇号连接的单词
    matches = word_regex.finditer(text)

    for match in matches:
        word = match.group(0)
        pos = word.find("'")
        if pos != -1:
            # 如果存在撇号，分割单词
            tokens.append(word[:pos])
            tokens.append(word[pos + 1:])
        else:
            # 添加整个单词
            tokens.append(word)
    return tokens


# 根据前缀过滤并排序单词
def filter_and_sort_words(words, prefix):
    filtered = set()
    for word in words:
        if word.startswith(prefix):
            filtered.add(word)
    return sorted(filtered)


def main():
    import sys
    input = sys.stdin.read
    data = input().split('\n')

    text = data[0]
    prefix = data[1]

    # 对文本进行分词以提取单词
    words = tokenize(text)

    # 根据前缀过滤并排序单词
    result = filter_and_sort_words(words, prefix)

    # 输出结果
    if not result:
        print(prefix)
    else:
        print(" ".join(result))


if __name__ == "__main__":
    main()