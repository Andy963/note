#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date     : 2024/9/19
# @FileName : 05.py # noqa
# Created by; Andy963

"""
商人经营一家店铺,有number种商品,由于仓库限制每件商品的最大持有数量是item[index],每种商品的价格是item_price[item_index][day]

通过对商品的买进和卖出获取利润,请给出商人在days天内能获取的最大的利润。

注:同-件商品可以反复买进和卖出

输入描述

3 // 输入商品的数量 number

3 // 输入商人售货天数 days

456//输入仓库限制每件商品的最大持有数量是 item[index

123//输入第一件商品每天的价格

432//输入第二件商品每天的价格

153//输入第三件商品每天的价格

输出描述

32 // 输出商人在这段时间内的最大利润

备注

根据输入的信息:
number=3
days=3
item[3]={4,5,6}
item_price[3][4]={{1,2,3},{4,3,2],{1,5,33}
针对第一件商品,商人在第一天的价格是itemprice[0][0]=1时买入item[0]件,在第三天item_price[0][2]=3的时候卖出,获利最大是8;
·针对第二件商品,不进行交易,获利最大时0;
针对第三件商品,商人在第一天价格是itemprice[2][0]=1时买入item[2]件,在第二天itemprice[2][0]=5的时候卖出,获利最大是24;
因此这段时间商人能获取的最大利润是8+24=32;
示例1
输入
3
3
4 5 6
1 2 3
4 3 2
1 5 2
输出
32
说明
示例2
1
1
1
1
输出
0
说明
解题思路：换个简单的思路，我们可以商品分开来看，单独计算每个商品能赚的最大利润。
一些同学会去找极小值、极大值取差，实际上在每天的价格信息后，我们仅需对比相邻两天的价格，
如果价格有上升，就前一天买入，后一天卖出。
"""


def solve():
    n = int(input())  # 商品种类数量n
    m = int(input())  # 售货天数m
    num = list(map(int, input().split()))  # 输入每种商品的最大持有数量
    ans = 0  # 初始化总利润变量为0
    for i in range(n):  # 遍历每种商品
        price = list(map(int, input().split()))  # 输入每种商品在每一天的价格
        res = 0  # 初始化临时利润变量res
        for j in range(m - 1):  # 遍历每一天的价格（不包括最后一天）
            if price[j + 1] > price[j]:  # 如果第二天的价格高于当天价格
                res += price[j + 1] - price[j]  # 计算当天买入第二天卖出的利润并累计到res
        ans += res * num[i]  # 计算该商品在所有天内可能获得的最大利润，并累加到总利润ans中
    print(ans)  # 输出商人在给定天数内可能获得的最大总利润

def outer(fn):

    print('outer')

    def inner():

        print('inner')

        return fn

    return inner

@outer
def fun():
    print('fun')

class Base(object):

    count = 0

    def __init__(self):

        pass
b1 = Base()
b2 = Base()

b1.count = b1.count + 1

print(b1.count,end=" ")

print(Base.count,end=" ")

print(b2.count)
# if __name__ == "__main__":
#     solve()