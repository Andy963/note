#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date     : 2024/9/26
# @FileName : 42-2.py # noqa
# Created by; Andy963
"""
在某个项目中有多个任务（用 tasks 数组表示）需要您进行处理，其中 tasks[i] = [si, ei]，
你可以在 si <= day <= ei 中的任意一天处理该任务。请返回你可以处理的最大任务数。
注：一天可以完成一个任务的处理。
输入描述：
第一行为任务数量 n，1 <= n <= 100000。后面 n 行表示各个任务的开始时间和终止时间，
用 si 和 ei 表示，1 <= si <= ei <= 100000。
输出描述：
输出为一个整数，表示可以处理的最大任务数。
补充说明：
示例1
输入：
3
1 1
1 2
1 3
输出：
3
说明：
第一天处理任务 1，第二天处理任务 2，第三天处理任务 3。
一个简单的贪心问题，要尽可能处理多的任务，我们要优先处理当前可以处理且最早结束的任务，
使用一个小根堆来维护当前我们最应该处理的任务，在处理完成之后天数加1，然后更新我们的小根堆，
剔除过期的任务，增加新一天可以完成的任务。
"""

from collections import defaultdict
import heapq

# 使用 defaultdict 创建一个字典，用于存储每个开始时间对应的结束时间列表
g = defaultdict(list)


def solve():
    global g
    n = int(input())  # 读取任务数量
    for _ in range(n):
        s, t = map(int, input().split())  # 读取每个任务的开始和结束时间
        g[s].append(t)  # 将结束时间添加到对应开始时间的列表中

    ans = 0  # 记录可以处理的最大任务数量
    priority_queue = []  # 初始化优先队列（小顶堆）

    # 从第1天到第100000天遍历，尝试处理任务
    for i in range(1, int(1e5) + 1):
        # 将当前天开始的所有任务的结束时间加入优先队列
        for t in g[i]:
            heapq.heappush(priority_queue, t)

        # 清除所有无法在当前或以后完成的任务（结束时间已过）
        while priority_queue and priority_queue[0] < i:
            heapq.heappop(priority_queue)

        # 如果队列中还有任务，完成结束时间最早的任务
        if priority_queue:
            ans += 1  # 完成任务数加一
            heapq.heappop(priority_queue)  # 移除已完成的任务

    # 输出可以完成的最大任务数
    print(ans)


if __name__ == '__main__':
    solve()