#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date     : 2024/9/22
# @FileName : 12.py # noqa
# Created by; Andy963
"""
智能手机方便了我们生活的同时，也侵占了我们不少的时间。“手机App防沉迷系统”能够让我们每天合理的规划手机App使用时间，在正确的时间做正确的事。
它的大概原理是这样的：
1、在一天24小时内，可注册每个App的允许使用时段；
2、一个时段只能使用一个App，举例说明：不能同时在09:00-10:00注册App2和App3；
3、App有优先级，数值越高，优先级越高。注册使用时段时，如果高优先级的App时间和低优先级的时段有冲突，
则系统会自动注销低优先级的时段；如果App的优先级相同，则后添加的App不能注册。
举例1：
（1）注册App3前：
（2）App3注册时段和App2有冲突：
（3）App3优先级高，系统接受App3的注册，自动注销App2的注册：
举例2：
（1）注册App4：
（2）App4和App2及App3都有冲突，优先级比App2高，但比App3低，这种场景下App4注册不上，最终的注册效果如下：
4、一个App可以在一天内注册多个时段。
请编程实现，根据输入数据注册App，并根据输入的时间点，返回该时间点可用的App名称，如果该时间点没有注册任何App，请返回字符串"NA"。
输入描述：
输入分3部分：第一行表示注册的App数N（N≤100）；第二部分包括N行，每行表示一条App注册数据；最后一行输入一个时间点，程序即返回该时间点的可用App。
2
App1 1 09:00 10:00
App2 2 11:00 11:30
09:30
数据说明如下：
1、N行注册数据以空格分隔，四项数据依次表示：App名称、优先级、起始时间、结束时间
2、优先级1-5，数字值越大，优先级越高
3、时间格式HH:MM，小时和分钟都是两位，不足两位前面补0
4、起始时间需小于结束时间，否则注册不上
5、注册信息中的时间段包含起始时间点，不包含结束时间点
输出描述：
输出一个字符串，表示App名称，或NA表示空闲时间。
补充说明：
1、用例保证时间都介于00:00-24:00之间；
2、用例保证数据格式都是正确的，不用考虑数据输入行数不够、注册信息不完整、字符串非法、优先级超限、时间格式不正确的问题。
示例1
输入：
1
App1 1 09:00 10:00
09:30
输出：
App1
说明：
App1注册在9点到10点间，9点半可用的应用名是App1
示例2
输入：
2
App1 1 09:00 10:00
App2 2 09:10 09:30
09:20
输出：
App2
说明：
App1和App2的时段有冲突，App2的优先级比App1高，注册App2后，系统将App1的注册信息自动注销后，09:20时刻可用应用名是App2.
示例3
输入：
2
App1 1 09:00 10:00
App2 2 09:10 09:30
09:50
输出：
NA
说明：
App1被注销后，09:50时刻没有应用注册，因此输出NA。
代码报告
"""
import unittest
class App:
    """表示一个App的类，包含名称、优先级、开始时间和结束时间"""
    def __init__(self, name, priority, start_time, end_time):
        self.name = name
        self.priority = priority
        self.start_time = self.time_to_minutes(start_time)
        self.end_time = self.time_to_minutes(end_time)


    @staticmethod
    def time_to_minutes(time_str):
        """将时间字符串（格式HH:MM）转换为一天中从00:00开始的分钟数"""
        return int(time_str[:2]) * 60 + int(time_str[3:5])

    def __str__(self):
        return self.name

def solve(N, apps,query_time):
    registered_apps = []
    for i in range(N):
        app = App(apps[i][0], apps[i][1], apps[i][2], apps[i][3])
        if app.start_time >= app.end_time:
            continue

        # 检查是否能注册
        can_register = True
        for ra in registered_apps:
            # 时间冲突，且优先级更高
            if app.start_time <= ra.end_time and app.end_time > ra.start_time and app.priority <= ra.priority:
                can_register = False
                break
        if can_register:
            new_registered = [a for a in registered_apps if not (a.start_time < app.end_time and a.end_time >  app.start_time and app.start_time < app.end_time)]
            new_registered.append(app)
            registered_apps = new_registered
    print([app.name for app in registered_apps])
    query_time = App.time_to_minutes(query_time)
    for app in registered_apps:
        if app.start_time <= query_time <= app.end_time:
            return app.name
    return 'NA'





class TestSolve(unittest.TestCase):

    def test_case_1(self):
        N = 2
        App = [['App1', 1, '09:00', '10:00'], ['App2', 2, '09:10', '09:30']]
        query_time = '09:20'
        expected_output = 'App2'
        self.assertEqual(solve(N, App,query_time), expected_output)

    def test_case_2(self):
        N = 2
        App = [['App1', 1, '09:00', '09:10'], ['App2', 2, '09:10', '09:30']]
        query_time = '09:50'
        expected_output = 'NA'
        self.assertEqual(solve(N, App,query_time), expected_output)

if __name__ == '__main__':
    unittest.main()