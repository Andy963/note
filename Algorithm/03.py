#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date     : 2024/9/16
# @FileName : 03.py # noqa
# Created by; Andy963
"""
祖国西北部有一片大片荒地，其中零星的分布着一些湖泊，保护区，矿区:整体上常年光照良好，但是也有一些地区光照不太好。
某电力公司希望在这里建设多个光伏电站，生产清洁能源对每平方公里的土地进行了发电评估，其中不能建设的区域发电量为0kw，可以发电的区域根据光照，地形等给出了每平方公里年发电量x千瓦。
我们希望能够找到其中集中的矩形区域建设电站，能够获得良好的收益
输入描述
第一行输入为调研的地区长，宽，以及准备建设的电站【长宽相等，为正方形】的边长，最低要求的发电量，之后每行为调研区域每平方公里的发电量。
例如，输入为:
2526
13458
23671
表示调研的区域大小为长2宽5的矩形，我们要建设的电站的边长为 2，建设电站最低发电量为 6
输出描述
输出为这样的区域有多少个?
上述输入长度为 2 的正方形满足发电量大于等于6的区域有 4 个。则输出为:
备注
其中被调研的区域的长宽均大于等于 1，建设电站的边长大于等于 1，任何区域的发电量大于等于0
示例1
输入

2 5 2 6

1 3 4 5 8

2 3 6 7 1

输出

4

说明

输入长为2，宽为5的场地，建设的场地为正方形场地边长为2，要求场地的发电量大于等于6

示例2

2 5 1 6

1 3 4 5 8

2 3 6 7 1

输出

3

说明

输入长为2，宽为5的场地，建设的场地为正方形场地，边长为1，要求场地的发电量大于等于6

示例3

2 5 1 0

1 3 4 5 8

2 3 6 7 1

输出

10

说明

输入长为2，宽为5的场地，建设的场地为正方形场地，边长为1，要求场地的发电量大于等于0
解题思路

1、理解问题:

- 给定一个矩形区域的尺寸（长和宽）和一个正方形电站的边长，计算在这个矩形区域内所有可能的正方形子区域的总发电量。

判断这些正方形子区域中有多少个满足最低发电量要求。

2、前缀和的概念:

- 前缀和是一种预处理技术，用于快速计算矩阵中任意子矩阵的和。

通过构建一个前缀和矩阵，我们可以在常数时间内查询任何子矩阵的和。

3、构建前缀和矩阵:

- 创建一个与输入矩阵大小相同的前缀和矩阵prefixSum，其中prefixSum[i][j]表示从左上角 (0,0) 到 (i,j) 的所有元素之和。

计算公式：

prefixSum[i][j] = matrix[i][j]

                + prefixSum[i-1][j]

                + prefixSum[i][j-1]

                - prefixSum[i-1][j-1]

4、计算每个正方形子区域的发电量:

- 遍历每一个可能的正方形子区域的左上角坐标 (i, j)。

- 计算每个正方形区域的总发电量，使用前缀和矩阵快速查询：

totalPower = prefixSum[x2][y2]

           - prefixSum[x1-1][y2]

           - prefixSum[x2][y1-1]

           + prefixSum[x1-1][y1-1]

其中 (x1, y1) 是正方形的左上角坐标，(x2, y2) 是右下角坐标。通过这种方式，可以快速计算任意子矩阵的和。

5、判断和计数:

- 对于每个正方形子区域，计算其总发电量并判断是否满足最低发电量要求。

6、输出结果:

- 输出满足条件的正方形子区域的数量。
"""


def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    # 读取输入
    region_length = int(data[0])
    region_width = int(data[1])
    square_side = int(data[2])
    min_power = int(data[3])

    # 初始化发电量矩阵，增加1行1列用于前缀和计算简化
    power_grid = [[0] * (region_width + 1) for _ in range(region_length + 1)]

    # 读取每个位置的发电量
    index = 4
    for i in range(1, region_length + 1):
        for j in range(1, region_width + 1):
            power_grid[i][j] = int(data[index])
            index += 1

    # 构建前缀和矩阵直接在原始矩阵上
    for i in range(1, region_length + 1):
        for j in range(1, region_width + 1):
            power_grid[i][j] += power_grid[i - 1][j] + power_grid[i][j - 1] - \
                                power_grid[i - 1][j - 1]

    count = 0  # 满足条件的区域数量

    # 遍历所有可能的正方形子区域的左上角坐标 (i, j)
    for i in range(1, region_length - square_side + 2):
        for j in range(1, region_width - square_side + 2):
            # 子矩阵的右下角坐标
            x2 = i + square_side - 1
            y2 = j + square_side - 1

            # 计算子矩阵的总发电量
            total_power = power_grid[x2][y2] - power_grid[i - 1][y2] - power_grid[x2][
                j - 1] + power_grid[i - 1][j - 1]

            # 检查总发电量是否满足条件
            if total_power >= min_power:
                count += 1

    # 输出满足条件的区域数量
    print(count)


if __name__ == "__main__":
    main()