#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date     : 2024/9/21
# @FileName : 09.py # noqa
# Created by; Andy963
"""
一个人设定一组四码的数字作为谜底，另一方猜,
每猜一个数，出数者就要根据这个数字给出提示，提示以XAYB形式呈现，直到猜中位置。
其中X表示位置正确的数的个数(数字正确且位置正确)，而Y表示数字正确而位置不对的数的个数。
例如，当谜底为8123，而猜谜者猜1052时，出题者必须提示0A2B.
例如，当谜底为5637，而猜谜者才4931时，出题者必须提示1A0B.
当前已知N组猜谜者猜的数字与提示，如果答案确定，请输出答案，不确定则输出NA。
输入描述
第一行输入一个正整数，0<N < 100.
接下来N行，每一行包含一个猜测的数字与提示结果。
输出描述
输出最后的答案，答案不确定则输出NA。
示例1
输入
6
4815 1A1B
5716 0A1B
7842 0A1B
4901 0A0B
8585 3A0B
8555 2A1B
输出
3585
说明
"""
def check_result(guess, target):
    guess = str(guess)
    # 计算x_count
    x_count = 0
    for i in range(len(guess)):
        if guess[i] == target[i]:
            x_count += 1

    guess_ = [guess[_] for _ in range(len(guess)) if guess[_] != target[_]]
    target_ = [target[_] for _ in range(len(guess)) if guess[_] != target[_]]
    # print(guess_, target_)
    # 计算y_count
    y_count = 0
    for i in range(len(guess_)):
        if guess_[i] in target_ and guess_[i] != target_[i]:
            y_count += 1
    return '{}A{}B'.format(x_count, y_count)

def find_answer(guesses):
    possible_answers = []
    for target in range(10000):
        target_str =  f"{target:04d}"
        valid = True

        for guess, result in guesses:
            if check_result(guess, target_str) != result:
                valid = False
                break
        if valid:
            possible_answers.append(target_str)
    print(possible_answers)
    if len(possible_answers) == 1:
        return possible_answers[0]
    else:
        return 'NA'

guesses = [
    (4815, '1A1B'),
    (5716, '0A1B'),
    (7842, '0A1B'),
    (4901, '0A0B'),
    (8585, '3A0B'),
    (8555, '2A1B')
]

# print(check_result(guesses[5][0], '3585'))

if __name__ == '__main__':
    print(find_answer(guesses))