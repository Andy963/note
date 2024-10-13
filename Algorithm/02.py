#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date     : 2024/9/21
# @FileName : 02.py # noqa
# Created by; Andy963
"""
一个XX产品行销总公司，只有一个b0ss，其有若千一级分销，一级分销又有若干二级分销，
每个分销只有唯一的上级分销。规定，每个月，下级分销需要将自己的总收入(自已的+下级上交的)
每满100元上交15元给自己的上级现给出一组分销的关系，和每个分销的收入，
请找出boss并计算出这个boss的收入。
比如:
·收入100元，上交15元:
·收入199元(99元不够100)，上交15元:。
收入200元，上交30元。
输入:
分销关系和收入:[[分销id上级分销id收入]，[分销id上级分销id收入]，[分销id 上级分销id 收入]]
·分销ID范围:0..65535
·收入范围:0..65535，单位元
提示:
输入的数据只存在1个boss，不存在环路
输出:
[boss的ID，总收入]
输入描述
第一行输入关系的总数量N
第二行开始，输入关系信息，格式:
分销ID上级分销ID收入
比如:
5
1 0 100
2 0 199
3 0 200
4 0 200
5 0 200
输出描述：
输出:
boss的ID总收入
0 120
比如:
0120
说明
给定的输入数据都是合法的,不存在环路,重复的
"""

def calculate_total_income(n, relations):
    parent_map = {}
    income_map = {}
    children_map = {}

    # 构建parent_map和income_map
    for rel in relations:
        child_id, parent_id, income = rel
        parent_map[child_id] = parent_id
        income_map[child_id] = income

        # 记录下每个分销的子级关系
        if parent_id not in children_map:
            children_map[parent_id] = []
        children_map[parent_id].append(child_id)
    print(parent_map)
    print(income_map)
    print(children_map)
    #{1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    #{1: 100, 2: 199, 3: 200, 4: 200, 5: 200}
    # {0: [1, 2, 3, 4, 5]}
    # 找到boss，即没有上级的分销
    boss_id = None
    for child, parent in parent_map.items():
        if parent not in parent_map:
            boss_id = parent

    # 递归计算收入
    def compute_income(distributor_id):
        total_income = income_map.get(distributor_id, 0)
        if distributor_id in children_map:
            for child_id in children_map[distributor_id]:
                total_income += compute_income(child_id)

        # 每满100元上交15元
        parent_id = parent_map.get(distributor_id, None)
        if parent_id is not None:
            income_to_pay = (total_income // 100) * 15
            income_map[parent_id] += income_to_pay

        return total_income - (total_income // 100) * 15

    # 计算boss的总收入
    boss_income = compute_income(boss_id)
    return boss_id, boss_income

# 示例输入
n = 5
relations = [
    (1, 0, 100),
    (2, 0, 199),
    (3, 0, 200),
    (4, 0, 200),
    (5, 0, 200)
]

calculate_total_income(n, relations)