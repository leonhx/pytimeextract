#!/usr/bin/env python
# coding:utf-8

import sys, os
sys.path.append(os.path.abspath('./time_expr'))
sys.path.append(os.path.abspath('./model'))

import re
import datetime

class TimePoint:
    def __init__(self):
        self.tunit = [-1, -1, -1, -1, -1, -1]

class TimeUnit:
    def __init__(self, exp_time, n):
        self.Time_Expression = exp_time
        self.Time_Norm = ''
        self._tp = TimePoint()
        self._tp_origin = TimePoint()
        self.__normalizer__ = n
        self.time = None
        self.time_full = None
        self.time_origin = None
        self.Time_Normalization()
    def __str__(self):
        return self.Time_Expression + u' --> ' + self.Time_Norm
    def __norm_set__(self, regex, idx):
        pattern = re.compile(regex, re.UNICODE)
        m = pattern.search(self.Time_Expression)
        if m:
            self._tp.tunit[idx] = int(m.group())
    def norm_setyear(self):
        pattern = re.compile(u'[0-9]{2}(?=年)', re.UNICODE)
        m = pattern.search(self.Time_Expression)
        if m:
            self._tp.tunit[0] = int(m.group())
            if self._tp.tunit[0] > 0 and self._tp.tunit[0] < 100:
                if self._tp.tunit[0] < 30:
                    self._tp.tunit[0] += 2000
                else:
                    self._tp.tunit[0] += 1900
            return
        self.__norm_set__(u'[0-9]?[0-9]{3}(?=年)', 0)
    def norm_setmonth(self):
        self.__norm_set__(u'((10)|(11)|(12)|([1-9]))(?=月)', 1)
    def norm_setday(self):
        self.__norm_set__(u'((?<!\\d))([0-3][0-9]|[1-9])(?=(日|号))', 2)
    def norm_sethour(self):
        self.__norm_set__(u'(?<!周)([0-2]?[0-9])(?=(点|时))|(?<!星期)([0-2]?[0-9])(?=(点|时))', 3)

        pattern = re.compile(u'(中午)|(午间)', re.UNICODE)
        m = pattern.search(self.Time_Expression);
        if m:
            if self._tp.tunit[3] >= 0 and self._tp.tunit[3] <= 10:
                self._tp.tunit[3] += 12

        pattern = re.compile(u'(下午)|(午后)|(pm)|(PM)', re.UNICODE)
        m = pattern.search(self.Time_Expression);
        if m:
            if self._tp.tunit[3] >= 0 and self._tp.tunit[3] <= 11:
                self._tp.tunit[3] += 12

        pattern = re.compile(u'晚', re.UNICODE);
        m = pattern.search(self.Time_Expression);
        if m:
            if self._tp.tunit[3] >= 1 and self._tp.tunit[3] <= 11:
                self._tp.tunit[3] += 12
            elif self._tp.tunit[3] == 12:
                self._tp.tunit[3] = 0
    def norm_setminute(self):
        pattern = re.compile(u'([0-5]?[0-9](?=分(?!钟)))|((?<=((?<!小)[点时]))[0-5]?[0-9](?!刻))', re.UNICODE);
        m = pattern.search(self.Time_Expression)
        if m:
            if m.group():
                self._tp.tunit[4] = int(m.group())

        pattern = re.compile(u'(?<=[点时])[1一]刻(?!钟)', re.UNICODE)
        m = pattern.search(self.Time_Expression)
        if m:
            self._tp.tunit[4] = 15

        pattern = re.compile(u'(?<=[点时])半', re.UNICODE)
        m = pattern.search(self.Time_Expression)
        if m:
            self._tp.tunit[4] = 30

        pattern = re.compile(u'(?<=[点时])[3三]刻(?!钟)', re.UNICODE)
        m = pattern.search(self.Time_Expression)
        if m:
            self._tp.tunit[4] = 45
    def norm_setsecond(self):
        self.__norm_set__(u'([0-5]?[0-9](?=秒))|((?<=分)[0-5]?[0-9])', 5)
    def norm_setTotal(self):
        pattern = re.compile(u'(?<!周)([0-2]?[0-9]):[0-5]?[0-9]:[0-5]?[0-9]|(?<!星期)([0-2]?[0-9]):[0-5]?[0-9]:[0-5]?[0-9]', re.UNICODE)
        m = pattern.search(self.Time_Expression)
        if m:
            tmp_target = m.group()
            tmp_parser = tmp_target.split(':')
            self._tp.tunit[3] = int(tmp_parser[0])
            self._tp.tunit[4] = int(tmp_parser[1])
            self._tp.tunit[5] = int(tmp_parser[2])
        else:
            pattern = re.compile(u'(?<!周)([0-2]?[0-9]):[0-5]?[0-9]|(?<!星期)([0-2]?[0-9]):[0-5]?[0-9]', re.UNICODE)
            m = pattern.search(self.Time_Expression)
            if m:
                tmp_target = m.group()
                tmp_parser = tmp_target.split(':')
                self._tp.tunit[3] = int(tmp_parser[0])
                self._tp.tunit[4] = int(tmp_parser[1])

        pattern = re.compile(u'(中午)|(午间)', re.UNICODE)
        m = pattern.search(self.Time_Expression)
        if m:
            if self._tp.tunit[3] >= 0 and self._tp.tunit[3] <= 10:
                self._tp.tunit[3] += 12

        pattern = re.compile(u'(下午)|(午后)|(pm)|(PM)', re.UNICODE)
        m = pattern.search(self.Time_Expression)
        if m:
            if self._tp.tunit[3] >= 0 and self._tp.tunit[3] <= 11:
                self._tp.tunit[3] += 12

        pattern = re.compile(u'晚', re.UNICODE)
        m = pattern.search(self.Time_Expression)
        if m:
            if self._tp.tunit[3] >= 1 and self._tp.tunit[3] <= 11:
                self._tp.tunit[3] += 12
            elif self._tp.tunit[3] == 12:
                self._tp.tunit[3] = 0

        pattern = re.compile('[0-9]?[0-9]?[0-9]{2}-((10)|(11)|(12)|([1-9]))-((?<!\\d))([0-3][0-9]|[1-9])', re.UNICODE)
        m = pattern.search(self.Time_Expression)
        if m:
            tmp_target = m.group()
            tmp_parser = tmp_target.split('-')
            self._tp.tunit[0] = int(tmp_parser[0])
            self._tp.tunit[1] = int(tmp_parser[1])
            self._tp.tunit[2] = int(tmp_parser[2])

        pattern = re.compile('((10)|(11)|(12)|([1-9]))/((?<!\\d))([0-3][0-9]|[1-9])/[0-9]?[0-9]?[0-9]{2}', re.UNICODE)
        m = pattern.search(self.Time_Expression)
        if m:
            tmp_target = m.group()
            tmp_parser = tmp_target.split('/')
            self._tp.tunit[1] = int(tmp_parser[0])
            self._tp.tunit[2] = int(tmp_parser[1])
            self._tp.tunit[0] = int(tmp_parser[2])

        pattern = re.compile('[0-9]?[0-9]?[0-9]{2}\\.((10)|(11)|(12)|([1-9]))\\.((?<!\\d))([0-3][0-9]|[1-9])', re.UNICODE)
        m = pattern.search(self.Time_Expression)
        if m:
            tmp_target = m.group()
            tmp_parser = tmp_target.split('.')
            self._tp.tunit[0] = int(tmp_parser[0])
            self._tp.tunit[1] = int(tmp_parser[1])
            self._tp.tunit[2] = int(tmp_parser[2])
    def norm_setBaseRelated(self):
        time_grid = self.__normalizer__.__time_base__.split('-')
        ini = [int(i) for i in time_grid]

        calendar = datetime.datetime(*ini)

        flag = [False, False, False]

        pattern = re.compile(u'\\d+(?=天[以之]?前)', re.UNICODE)
        m = pattern.search(self.Time_Expression)
        if m:
            flag[2] = True
            day = datetime.timedelta(int(m.group()))
            calendar -= day

        pattern = re.compile(u'\\d+(?=天[以之]?后)', re.UNICODE)
        m = pattern.search(self.Time_Expression)
        if m:
            flag[2] = True
            day = datetime.timedelta(int(m.group()))
            calendar += day

        pattern = re.compile(u'\\d+(?=(个)?月[以之]?前)', re.UNICODE)
        m = pattern.search(self.Time_Expression)
        if m:
            flag[1] = True
            month = int(m.group())
            calendar = datetime.datetime(calendar.year, calendar.month-month, calendar.day, calendar.hour, calendar.minute, calendar.second)

        pattern = re.compile(u'\\d+(?=(个)?月[以之]?后)', re.UNICODE)
        m = pattern.search(self.Time_Expression)
        if m:
            flag[1] = True
            month = int(m.group())
            calendar = datetime.datetime(calendar.year, calendar.month+month, calendar.day, calendar.hour, calendar.minute, calendar.second)

        pattern = re.compile(u'\\d+(?=年[以之]?前)', re.UNICODE)
        m = pattern.search(self.Time_Expression)
        if m:
            flag[0] = True
            year = int(m.group())
            calendar = datetime.datetime(calendar.year-year, calendar.month, calendar.day, calendar.hour, calendar.minute, calendar.second)

        pattern = re.compile(u'\\d+(?=年[以之]?后)', re.UNICODE)
        m = pattern.search(self.Time_Expression)
        if m:
            flag[0] = True
            year = int(m.group())
            calendar = datetime.datetime(calendar.year+year, calendar.month, calendar.day, calendar.hour, calendar.minute, calendar.second)

        if any(flag):
            self._tp.tunit[0] = calendar.year
        if any(flag[:2]):
            self._tp.tunit[1] = calendar.month
        if flag[2]:
            self._tp.tunit[2] = calendar.day
    def norm_setCurRelated(self):
        time_grid = self.__normalizer__.__old_time_base__.split('-')
        ini = [int(i) for i in time_grid]

        calendar = datetime.datetime(*ini)

        flag = [False, False, False]

        pattern = re.compile(u'前年', re.UNICODE)
        m = pattern.search(self.Time_Expression)
        if m:
            flag[0] = True
            calendar = datetime.datetime(calendar.year-2, calendar.month, calendar.day, calendar.hour, calendar.minute, calendar.second)

        pattern = re.compile(u'去年', re.UNICODE)
        m = pattern.search(self.Time_Expression)
        if m:
            flag[0] = True
            calendar = datetime.datetime(calendar.year-1, calendar.month, calendar.day, calendar.hour, calendar.minute, calendar.second)

        pattern = re.compile(u'今年', re.UNICODE)
        m = pattern.search(self.Time_Expression)
        if m:
            flag[0] = True
            calendar = datetime.datetime(datetime.datetime.now().year, calendar.month, calendar.day, calendar.hour, calendar.minute, calendar.second)

        pattern = re.compile(u'明年', re.UNICODE)
        m = pattern.search(self.Time_Expression)
        if m:
            flag[0] = True
            calendar = datetime.datetime(calendar.year+1, calendar.month, calendar.day, calendar.hour, calendar.minute, calendar.second)

        pattern = re.compile(u'后年', re.UNICODE)
        m = pattern.search(self.Time_Expression)
        if m:
            flag[0] = True
            calendar = datetime.datetime(calendar.year+2, calendar.month, calendar.day, calendar.hour, calendar.minute, calendar.second)

        pattern = re.compile(u'上(个)?月', re.UNICODE)
        m = pattern.search(self.Time_Expression)
        if m:
            flag[1] = True
            calendar = datetime.datetime(calendar.year, calendar.month-1, calendar.day, calendar.hour, calendar.minute, calendar.second)

        pattern = re.compile(u'(本|这个)月', re.UNICODE)
        m = pattern.search(self.Time_Expression)
        if m:
            flag[1] = True
            calendar = datetime.datetime(calendar.year, datetime.datetime.now().month, calendar.day, calendar.hour, calendar.minute, calendar.second)

        pattern = re.compile(u'下(个)?月', re.UNICODE)
        m = pattern.search(self.Time_Expression)
        if m:
            flag[1] = True
            calendar = datetime.datetime(calendar.year, calendar.month+1, calendar.day, calendar.hour, calendar.minute, calendar.second)

        pattern = re.compile(u'大前天', re.UNICODE)
        m = pattern.search(self.Time_Expression)
        if m:
            flag[2] = True
            calendar -= datetime.timedelta(3)

        pattern = re.compile(u'(?<!大)前天', re.UNICODE)
        m = pattern.search(self.Time_Expression)
        if m:
            flag[2] = True
            calendar -= datetime.timedelta(2)

        pattern = re.compile(u'昨', re.UNICODE)
        m = pattern.search(self.Time_Expression)
        if m:
            flag[2] = True
            calendar -= datetime.timedelta(1)

        pattern = re.compile(u'今(?!年)', re.UNICODE)
        m = pattern.search(self.Time_Expression)
        if m:
            flag[2] = True
            calendar = datetime.datetime(calendar.year, calendar.month, datetime.datetime.now().day, calendar.hour, calendar.minute, calendar.second)

        pattern = re.compile(u'明(?!年)', re.UNICODE)
        m = pattern.search(self.Time_Expression)
        if m:
            flag[2] = True
            calendar += datetime.timedelta(1)

        pattern = re.compile(u'(?<!大)后天', re.UNICODE)
        m = pattern.search(self.Time_Expression)
        if m:
            flag[2] = True
            calendar += datetime.timedelta(2)

        pattern = re.compile(u'大后天', re.UNICODE)
        m = pattern.search(self.Time_Expression)
        if m:
            flag[2] = True
            calendar += datetime.timedelta(3)

        pattern = re.compile(u'(?<=(上上星期))[1-7]|(?<=(上上周))[1-7]', re.UNICODE)
        m = pattern.search(self.Time_Expression)
        if m:
            flag[2] = True
            calendar -= datetime.timedelta(14+calendar.weekday()-int(m.group()))

        pattern = re.compile(u'(?<=((?<!上)上周))[1-7]|(?<=((?<!上)上星期))[1-7]', re.UNICODE)
        m = pattern.search(self.Time_Expression)
        if m:
            flag[2] = True
            calendar -= datetime.timedelta(7+calendar.weekday()-int(m.group()))

        pattern = re.compile(u'(?<=((?<!下)下星期))[1-7]|(?<=((?<!下)下周))[1-7]', re.UNICODE)
        m = pattern.search(self.Time_Expression)
        if m:
            flag[2] = True
            calendar += datetime.timedelta(7-calendar.weekday()+int(m.group()))

        pattern = re.compile(u'(?<=(下下周))[1-7]|(?<=(下下星期))[1-7]', re.UNICODE)
        m = pattern.search(self.Time_Expression)
        if m:
            flag[2] = True
            calendar += datetime.timedelta(7-calendar.weekday()+int(m.group()))

        pattern = re.compile(u'(?<=((?<!(上|下))星期))[1-7]|(?<=((?<!(上|下))周))[1-7]', re.UNICODE)
        m = pattern.search(self.Time_Expression)
        if m:
            flag[2] = True
            calendar += datetime.timedelta(-calendar.weekday()+int(m.group()))

        if any(flag):
            self._tp.tunit[0] = calendar.year
        if any(flag[1:]):
            self._tp.tunit[1] = calendar.month
        if flag[2]:
            self._tp.tunit[2] = calendar.day
    def modifyTimeBase(self):
        time_grid = self.__normalizer__.__time_base__.split('-')
        s = '-'.join([ str(self._tp.tunit[i]) if self._tp.tunit[i] != -1 else t for i, t in enumerate(time_grid)])
        self.__normalizer__.__time_base__ = s
    def Time_Normalization(self):
        self.norm_setyear()
        self.norm_setmonth()
        self.norm_setday()
        self.norm_sethour()
        self.norm_setminute()
        self.norm_setsecond()
        self.norm_setTotal()
        self.norm_setBaseRelated()
        self.norm_setCurRelated()
        self.modifyTimeBase()

        self._tp_origin.tunit = self._tp.tunit[:]

        time_grid = self.__normalizer__.__time_base__.split('-')

        tunitpointer = 5
        while tunitpointer >= 0 and self._tp.tunit[tunitpointer] < 0:
            tunitpointer -= 1
        for i in range(tunitpointer):
            if self._tp.tunit[i] < 0:
                self._tp.tunit[i] = int(time_grid[i])

        _result_tmp = self._tp.tunit[:]

        threshold = datetime.datetime.now().year % 100
        if self._tp.tunit[0] > threshold and self._tp.tunit[0] < 100:
            _result_tmp[0] = 1900 + self._tp.tunit[0]
        elif self._tp.tunit[0] > 0 and self._tp.tunit[0] <= threshold:
            _result_tmp[0] = 2000 + self._tp.tunit[0]

        first_n1_idx = _result_tmp.index(-1)
        if first_n1_idx < 3:
            _result_tmp = [x if x != -1 else 1 for x in _result_tmp]
            first_n1_idx = 3
        cale = datetime.datetime(*_result_tmp[:first_n1_idx])
        self.Time_Norm = cale.strftime(u'%Y-%m-%d %H:%M:%S')
        self.time = cale
        self.time_full = self._tp.tunit
        self.time_origin = self._tp_origin
