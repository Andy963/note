#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date     : 2024/9/14
# @FileName : 01.py # noqa
# Created by; Andy963

"""
在斗地主只扑克牌游戏中，扑克牌由小到大的顺序为:3.4,5.6,7.8,9,10.J,Q.K.A.2，玩家可以出的扑克牌阵型有:单张、对子、顺子、飞机、炸弹等。
其中顺子的出牌规则为:由至少5张由小到大连续递增的 扑克牌只 组成，且不能包含2。

例如:(3.4,5,6,7}、(3.4,5,6,7,8,9,10,J,Q,K,A}都是有效的顺子;而{,Q,K,A,2}、(2,3,4,5,6}、(3,4,5,6}、(3,4,5.6,8)等都不是顺子给定一个包含 13 张牌的数组，如果有满足出牌规则的顺子，请输出顺子。
如果存在多个顺子，请每行输出一个顺子，且需要按顺子的第一张牌的大小(必须从小到大)依次输出。
如果没有满足出牌规则的顺子，请输出NO。
输入描述：
13张任意顺序的扑克牌，每张扑克牌数字用空格隔开，每张扑克牌的数字都是合法的，并且不包括大小王:2 9 J 2 3 4 K A 7 9  A 5 6不需要考虑输入为异常字符的情况
输出描述：
组成的顺子，每张扑克牌数字用空格隔开:3 4 5 6 7

示例1

输入

2 9 J 2 3 4 K A 7 9 A 5 6

输出

3 4 5 6 7

说明

13张牌中，可以组成的顺子只有1组:3 4 5 6 7.

示例2

输入

2 9 J 1 0 3 4 K A 7 Q A 5 6

输出

3 4 5 6 7
9 10 J Q K A

说明

13张牌中，可以组成2组顺子，从小到大分别为:3 4 5 6 7和9 10 J Q K A

示例3

输入

2 9 9 9 3 4 K A 10 Q A 5 6

输出

No

说明

13张牌中，无法组成顺子。

题目分析：

- 扑克牌按从小到大的顺序排列为：3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A。牌 2 不能用于顺子。

- 顺子的规则是：至少由5张连续递增的牌组成，例如 (3, 4, 5, 6, 7)。

- 需要找出所有可能的顺子组合，每个顺子中的牌不能重复使用。

解题思路

1、输入准备:

- 从输入中读取13张扑克牌，存储在一个列表或数组中。

2、数据转换:

- 将扑克牌的字符表示（如 "J", "Q", "K", "A"）转换为对应的数字值，以便于排序和比较。

- 排除不能用于顺子的牌 2。

3、排序:

- 对转换后的牌进行排序，以便更容易查找连续递增的序列。

4、查找顺子:

- 初始化数据结构：创建一个布尔数组（或列表）used，初始化为false，- 用于跟踪每张牌是否已经被用作某个顺子的一部分。

- 遍历牌序列：使用两层循环：

- 外层循环从每一张未使用的牌作为起点开始。

- 内层循环尝试构建一个顺子：

- 如果下一张牌与当前顺子的最后一张牌连续且未被使用，添加到当前顺子中并标记为已使用。

- 如果不连续或已被使用，终止当前顺子的构建。

- 验证顺子长度：检查构建的顺子是否至少包含5张牌：

- 如果是，将该顺子保存起来。

- 如果不是，重置used数组中与当前顺子相关的牌的标记，使它们可以用于后续的顺子构建。

5、输出结果:

- 如果找到一个或多个顺子，按顺序输出它们。

- 如果没有找到任何顺子，输出 "NO"。
"""


def card_value(card):
    """将扑克牌转换为对应的数字值"""
    card_map = {"3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
        "J": 11, "Q": 12, "K": 13, "A": 14}
    return card_map.get(card, 0)  # 忽略 '2'


def find_sequences(card_numbers):
    """查找所有可能的顺子"""
    sequences = []
    used = [False] * len(card_numbers)  # 记录每张牌是否已被使用

    for i in range(len(card_numbers)):
        if used[i]:
            continue  # 已使用的牌跳过

        current_sequence = [card_numbers[i]]
        used[i] = True  # 标记当前牌已使用

        for j in range(i + 1, len(card_numbers)):
            if used[j]:
                continue  # 跳过已使用的牌

            if card_numbers[j] == current_sequence[-1] + 1:
                current_sequence.append(card_numbers[j])
                used[j] = True  # 标记当前牌已使用
            elif card_numbers[j] > current_sequence[-1] + 1:
                break  # 不再连续，结束当前顺子的查找

        if len(current_sequence) >= 5:
            sequences.append(current_sequence)
        else:
            # 如果当前顺子不满足要求，重置已使用标记
            for num in current_sequence:
                used[card_numbers.index(num)] = False

    return sequences


def main():
    # input_cards = input().split()
    input_cards = '2 9 J 2 3 4 K A 7 9 A 5 6'
    # 转换并排序卡片，排除 '2'
    card_numbers = [card_value(card) for card in input_cards if card_value(card) != 0]
    card_numbers.sort()
    print(card_numbers)

    # 查找所有顺子
    sequences = find_sequences(card_numbers)

    # 输出结果
    if not sequences:
        print("No")
    else:
        for seq in sequences:
            output_seq = []
            for value in seq:
                if value == 11:
                    output_seq.append("J")
                elif value == 12:
                    output_seq.append("Q")
                elif value == 13:
                    output_seq.append("K")
                elif value == 14:
                    output_seq.append("A")
                else:
                    output_seq.append(str(value))
            print(" ".join(output_seq))


if __name__ == "__main__":
    main()


