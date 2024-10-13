#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date     : 2024/9/20
# @FileName : 07.py # noqa
# Created by; Andy963
"""题目描述
日志采集是运维系统的的核心组件。日志是按行生成，每行记做一条，由采集系统分批上报。
如果上报太频繁，会对服务端造成压力;
如果上报太晚，会降低用户的体验;
·如果一次上报的条数太多，会导致超时失败。
为此，项目组设计了如下的上报策略
1.每成功上报一条日志，奖励1分
2.每条日志每延迟上报1秒，扣1分
3.积累日志达到100条，必须立即上报
给出日志序列，根据该规则，计算首次上报能获得的最多积分数。
输入描述：
按时序产生的日志条数 T1,T2...Tn，其中
。1≤n≤ 1000
·0≤Ti≤ 100
输出描述：
首次上报最多能获得的积分数
示例1
输入
1 98 1
输出
98
说明
T1 时刻上报得1分
T2 时刻上报得98分，最大
T3 时刻上报得 0分
示例2
输入
50 60 1
输出
50
说明
如果第1个时刻上报，获得积分50。如果第2个时刻上报，最多上报100条，前50条延迟上报1s，每条扣除1分，共获得积分为100-50=50
示例3
输入
3 7 40 10 60
输出
37
说明
T1时刻上报得3分
T2时刻上报得7分
T3时刻上报得37分，最大
T4时刻上报得-3分
T5时刻上报，因为已经超了100条限制，所以只能上报100条，得-23分
"""

import sys


def main():
    input = sys.stdin.read
    logs = list(map(int, input().split()))  # 读取所有输入并转换为整数列表

    current_logs = 0  # 当前积累的日志条数
    max_score = float('-inf')  # 初始化最大积分为一个非常小的值
    total_delay_penalty = 0  # 总的延迟扣分
    # 遍历日志序列，寻找最佳的上报时间点
    for t in range(len(logs)):
        total_delay_penalty += current_logs  # 所有日志的总延迟时间
        current_logs += logs[t]

        if current_logs >= 100:  # 如果日志条数达到或超过100，必须上报
            max_score = max(max_score, 100 - total_delay_penalty)  # 更新最大积分
            break
        current_score = current_logs - total_delay_penalty
        max_score = max(max_score, current_score)  # 更新最大积分
    print(max_score)

if __name__ == '__main__':
    main()