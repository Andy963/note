#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date     : 2024/9/22
# @FileName : 16-2.py # noqa
# Created by; Andy963
"""
一个局域网内有很多台电脑，分别标注为0 - N-1的数字。相连接的电脑距离不一样，所以感染时间不一样，感染时间用t表示。
其中网络内一个电脑被病毒感染，其感染网络内所有的电脑需要最少需要多长时间。如果最后有电脑不会感染，则返回-1
给定一个数组times表示一个电脑把相邻电脑感染所用的时间。
如图：path[i]= {i,j, t} 表示电脑i->j 电脑i上的病毒感染j，需要时间t。
输入描述：
4
3
2 1 1
2 3 1
3 4 1
2
输出描述：
2
补充说明：
第一个参数:局域网内电脑个数N 1<=N<=200;
第二个参数：总共多少条网络连接
第三个 1 2 1 表示1->2时间为1
第七行：表示病毒最开始所在的电脑号1
 收起
示例1
输入：
4
3
2 1 1
2 3 1
3 4 1
2
输出：
2
"""