#!/usr/bin/env python
# coding:utf-8

import re
import datetime

from normalizer import TimeNormalizer

class TimePoint:
    def __init__(self):
        self.tunit = [-1, -1, -1, -1, -1, -1]

class TimeUnit:
    def __init__(self, exp_time, n):
        self.Time_Expression = exp_time
        self.Time_Norm = ''
        self._tp = TimePoint()
        self._to_origin = TimePoint()
        self.__normalizer__ = n
        self.time = None
        self.time_full = None
        self.time_origin = None
        Time_Normalization()
    def __str__(self):
        return self.Time_Expression + ' --> ' + self.Time_Norm
    def __norm_set__(self, regex, idx):
        pattern = re.compile(regex)
        m = pattern.match(self.Time_Expression)
        if m:
            _tp.tunit[idx] = int(m.group())
    def norm_setyear(self):
        pattern = re.compile(u'[0-9]{2}(?=年)')
        m = pattern.match(self.Time_Expression)
        if m:
            _tp.tunit[0] = int(m.group())
            if _tp.tunit[0] > 0 and _tp.tunit[0] < 100:
                if _tp.tunit[0] < 30:
                    _tp.tunit[0] += 2000
                else:
                    _tp.tunit[0] += 1900
            return
        self.__norm_set__(u'[0-9]?[0-9]{3}(?=年)', 0)
    def norm_setmonth(self):
        self.__norm_set__(u'((10)|(11)|(12)|([1-9]))(?=月)', 1)
    def norm_setday(self):
        self.__norm_set__(u'((?<!\\d))([0-3][0-9]|[1-9])(?=(日|号))', 2)
    def norm_sethour(self):
        self.__norm_set__(u'(?<!(周|星期))([0-2]?[0-9])(?=(点|时))', 3)

        pattern = re.compile(u'(中午)|(午间)')
        m = pattern.match(self.Time_Expression);
        if m:
            if _tp.tunit[3] >= 0 and _tp.tunit[3] <= 10:
                _tp.tunit[3] += 12

        pattern = re.compile(u'(下午)|(午后)|(pm)|(PM)')
        m = pattern.match(self.Time_Expression);
        if m:
            if _tp.tunit[3] >= 0 and _tp.tunit[3] <= 11:
                _tp.tunit[3] += 12

        pattern = re.compile(u'晚');
        m = pattern.match(self.Time_Expression);
        if m:
            if _tp.tunit[3] >= 1 and _tp.tunit[3] <= 11:
                _tp.tunit[3] += 12
            elif _tp.tunit[3] == 12:
                _tp.tunit[3] = 0
    def norm_setminute(self):
        pattern = re.compile(u'([0-5]?[0-9](?=分(?!钟)))|((?<=((?<!小)[点时]))[0-5]?[0-9](?!刻))');
        m = pattern.match(self.Time_Expression)
        if m:
            if m.group():
                _tp.tunit[4] = int(m.group())

        pattern = re.compile(u'(?<=[点时])[1一]刻(?!钟)')
        m = pattern.match(self.Time_Expression)
        if m:
            _tp.tunit[4] = 15

        pattern = re.compile(u'(?<=[点时])半')
        m = pattern.match(self.Time_Expression)
        if m:
            _tp.tunit[4] = 30

        pattern = re.compile(u'(?<=[点时])[3三]刻(?!钟)')
        m = pattern.match(self.Time_Expression)
        if m:
            _tp.tunit[4] = 45
    def norm_setsecond(self):
        self.__norm_set__(([0-5]?[0-9](?=秒))|((?<=分)[0-5]?[0-9]), 5)
    def norm_setTotal(self):
        pattern = re.compile(u'(?<!(周|星期))([0-2]?[0-9]):[0-5]?[0-9]:[0-5]?[0-9]')
        m = pattern.match(self.Time_Expression)
        if m:
            tmp_target = m.group()
            tmp_parser = tmp_target.split(':')
            _tp.tunit[3] = int(tmp_parser[0])
            _tp.tunit[4] = int(tmp_parser[1])
            _tp.tunit[5] = int(tmp_parser[2])
        else:
            pattern = re.compile(u'(?<!(周|星期))([0-2]?[0-9]):[0-5]?[0-9]')
            m = pattern.match(self.Time_Expression)
            if m:
                tmp_target = m.group()
                tmp_parser = tmp_target.split(':')
                _tp.tunit[3] = int(tmp_parser[0])
                _tp.tunit[4] = int(tmp_parser[1])

        pattern = re.compile(u'(中午)|(午间)')
        m = pattern.match(self.Time_Expression)
        if m:
            if _tp.tunit[3] >= 0 and _tp.tunit[3] <= 10:
                _tp.tunit[3] += 12

        pattern = re.compile(u'(下午)|(午后)|(pm)|(PM)')
        m = pattern.match(self.Time_Expression)
        if m:
            if _tp.tunit[3] >= 0 and _tp.tunit[3] <= 11:
                _tp.tunit[3] += 12

        pattern = re.compile(u'晚')
        m = pattern.match(selfTime_Expression)
        if m:
            if _tp.tunit[3] >= 1 and _tp.tunit[3] <= 11:
                _tp.tunit[3] += 12
            elif _tp.tunit[3] == 12:
                _tp.tunit[3] = 0

        pattern = re.compile('[0-9]?[0-9]?[0-9]{2}-((10)|(11)|(12)|([1-9]))-((?<!\\d))([0-3][0-9]|[1-9])');
        m = pattern.match(self.Time_Expression)
        if m:
            tmp_target = m.group()
            tmp_parser = tmp_target.split('-')
            _tp.tunit[0] = int(tmp_parser[0])
            _tp.tunit[1] = int(tmp_parser[1])
            _tp.tunit[2] = int(tmp_parser[2])

        pattern = re.compile('((10)|(11)|(12)|([1-9]))/((?<!\\d))([0-3][0-9]|[1-9])/[0-9]?[0-9]?[0-9]{2}')
        m = pattern.match(self.Time_Expression)
        if m:
            tmp_target = m.group()
            tmp_parser = tmp_target.split('/')
            _tp.tunit[1] = int(tmp_parser[0])
            _tp.tunit[2] = int(tmp_parser[1])
            _tp.tunit[0] = int(tmp_parser[2])

        pattern = re.compile('[0-9]?[0-9]?[0-9]{2}\\.((10)|(11)|(12)|([1-9]))\\.((?<!\\d))([0-3][0-9]|[1-9])')
        m = pattern.matcher(self.Time_Expression)
        if m:
            tmp_target = match.group()
            tmp_parser = tmp_target.split('.')
            _tp.tunit[0] = int(tmp_parser[0])
            _tp.tunit[1] = int(tmp_parser[1])
            _tp.tunit[2] = int(tmp_parser[2])
    def norm_setBaseRelated(self):
        time_grid = self.__normalizer__.__time_base__.split('-')
        ini = [int(i) for i in time_grid]

        calendar = datetime.datetime(*ini)

        flag = [False, False, False]

        pattern = re.compile(u'\\d+(?=天[以之]?前)')
        m = pattern.match(self.Time_Expression)
        if m:
            flag[2] = True
            day = datetime.timedelta(int(match.group()))
            calendar -= day

        pattern = re.compile(u'\\d+(?=天[以之]?后)')
        m = pattern.match(self.Time_Expression)
        if m:
            flag[2] = True
            day = datetime.timedelta(int(match.group()))
            calendar += day

        pattern = re.compile(u'\\d+(?=(个)?月[以之]?前)')
        m = pattern.match(self.Time_Expression)
        if m:
            flag[1] = True
            month = int(match.group())
            calendar = datetime.datetime(calendar.year, calendar.month-month, calendar.day, calendar.hour, calendar.minute, calendar.second)

        pattern = re.compile(u'\\d+(?=(个)?月[以之]?后)')
        m = pattern.match(self.Time_Expression)
        if m:
            flag[1] = True
            month = int(match.group())
            calendar = datetime.datetime(calendar.year, calendar.month+month, calendar.day, calendar.hour, calendar.minute, calendar.second)

        pattern = re.compile(u'\\d+(?=年[以之]?前)')
        m = pattern.match(self.Time_Expression)
        if m:
            flag[0] = True
            year = int(match.group())
            calendar = datetime.datetime(calendar.year-year, calendar.month, calendar.day, calendar.hour, calendar.minute, calendar.second)

        pattern = re.compile(u'\\d+(?=年[以之]?后)')
        m = pattern.match(self.Time_Expression)
        if m:
            flag[0] = True
            year = int(match.group())
            calendar = datetime.datetime(calendar.year+year, calendar.month, calendar.day, calendar.hour, calendar.minute, calendar.second)

        if any(flag):
            _tp.tunit[0] = calendar.year
        if any(flag[:2])
            _tp.tunit[1] = calendar.month
        if flag[2]:
            _tp.tunit[2] = calendar.day
    def norm_setCurRelated(self):
        time_grid = self.__normalizer__.__old_time_base__.split('-')
        ini = [int(i) for i in time_grid]

        calendar = datetime.datetime(*ini)

        flag = [False, False, False]

        pattern = re.compile(u'前年')
        m = pattern.match(self.Time_Expression)
        if m:
            flag[0] = True
            calendar = datetime.datetime(calendar.year-2, calendar.month, calendar.day, calendar.hour, calendar.minute, calendar.second)

        pattern = re.compile(u'去年')
        m = pattern.match(self.Time_Expression)
        if m:
            flag[0] = True
            calendar = datetime.datetime(calendar.year-1, calendar.month, calendar.day, calendar.hour, calendar.minute, calendar.second)

        pattern = re.compile(u'今年')
        m = pattern.match(self.Time_Expression)
        if m:
            flag[0] = True
            calendar = datetime.datetime(datetime.datetime.now().year, calendar.month, calendar.day, calendar.hour, calendar.minute, calendar.second)

        pattern = re.compile(u'明年')
        m = pattern.match(self.Time_Expression)
        if m:
            flag[0] = True
            calendar = datetime.datetime(calendar.year+1, calendar.month, calendar.day, calendar.hour, calendar.minute, calendar.second)

        pattern = re.compile(u'后年')
        m = pattern.match(self.Time_Expression)
        if m:
            flag[0] = True
            calendar = datetime.datetime(calendar.year+2, calendar.month, calendar.day, calendar.hour, calendar.minute, calendar.second)

        pattern = re.compile(u'上(个)?月')
        m = pattern.match(self.Time_Expression)
        if m:
            flag[1] = True
            calendar = datetime.datetime(calendar.year, calendar.month-1, calendar.day, calendar.hour, calendar.minute, calendar.second)

        pattern = re.compile(u'(本|这个)月')
        m = pattern.match(self.Time_Expression)
        if m:
            flag[1] = True
            calendar = datetime.datetime(calendar.year, datetime.datetime.now().month, calendar.day, calendar.hour, calendar.minute, calendar.second)

        pattern = re.compile(u'下(个)?月')
        m = pattern.match(self.Time_Expression)
        if m:
            flag[1] = True
            calendar = datetime.datetime(calendar.year, calendar.month+1, calendar.day, calendar.hour, calendar.minute, calendar.second)

        pattern = re.compile(u'大前天')
        m = pattern.match(self.Time_Expression)
        if m:
            flag[2] = True
            calendar -= datetime.timedelta(3)

        pattern = re.compile(u'(?<!大)前天')
        m = pattern.match(self.Time_Expression)
        if m:
            flag[2] = True
            calendar -= datetime.timedelta(2)

        pattern = re.compile(u'昨')
        m = pattern.match(self.Time_Expression)
        if m:
            flag[2] = True
            calendar -= datetime.timedelta(1)

        pattern = re.compile(u'今(?!年)')
        m = pattern.match(self.Time_Expression)
        if m:
            flag[2] = True
            calendar = datetime.datetime(calendar.year, calendar.month, datetime.datetime.now().day, calendar.hour, calendar.minute, calendar.second)

        pattern = re.compile(u'明(?!年)')
        m = pattern.match(self.Time_Expression)
        if m:
            flag[2] = True
            calendar += datetime.timedelta(1)

        pattern = re.compile(u'(?<!大)后天')
        m = pattern.match(self.Time_Expression)
        if m:
            flag[2] = True
            calendar += datetime.timedelta(2)

        pattern = re.compile(u'大后天')
        m = pattern.match(self.Time_Expression)
        if m:
            flag[2] = True
            calendar += datetime.timedelta(3)

        pattern = re.compile(u'(?<=(上上(周|星期)))[1-7]')
        m = pattern.match(self.Time_Expression)
        if m:
            flag[2] = True
            calendar -= datetime.timedelta(14+calendar.weekday()-int(match.group()))

        pattern = re.compile(u'(?<=((?<!上)上(周|星期)))[1-7]')
        m = pattern.match(self.Time_Expression)
        if m:
            flag[2] = True
            calendar -= datetime.timedelta(7+calendar.weekday()-int(match.group()))

        pattern = re.compile(u'(?<=((?<!下)下(周|星期)))[1-7]')
        m = pattern.match(self.Time_Expression)
        if m:
            flag[2] = True
            calendar += datetime.timedelta(7-calendar.weekday()+int(match.group()))

        pattern = re.compile(u'(?<=(下下(周|星期)))[1-7]')
        m = pattern.match(self.Time_Expression)
        if m:
            flag[2] = True
            calendar += datetime.timedelta(7-calendar.weekday()+int(match.group()))

        pattern = re.compile(u'(?<=((?<!(上|下))(周|星期)))[1-7]')
        m = pattern.match(self.Time_Expression)
        if m:
            flag[2] = True
            calendar += datetime.timedelta(-calendar.weekday()+int(match.group()))

        if any(flag):
            _tp.tunit[0] = calendar.year
        if any(flag[1:])
            _tp.tunit[1] = calendar.month
        if flag[2]:
            _tp.tunit[2] = calendar.day
    def modifyTimeBase(self):
        time_grid = self.__normalizer__.__time_base__.split('-')
        s = '-'.join([ str(_tp.tunit[i]) if _tp.tunit[i] != -1 else t for i, t in enumerate(time_grid)])
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

        _tp_origin.tunit = _tp.tunit[:]

        time_grid = self.__normalizer__.__time_base__.split('-')

        tunitpointer = 5
        while tunitpointer >= 0 and _tp.tunit[tunitpointer] < 0:
            tunitpointer -= 1
        for i in range(tunitpointer):
            if _tp.tunit[i] < 0:
                _tp.tunit[i] = int(time_grid[i])

        _result_tmp = _tp.tunit[:]

        threshold = datetime.datetime.now().year % 100
        if _tp.tunit[0] > threshold and _tp.tunit[0] < 100:
            _result_tmp[0] = 1900 + _tp.tunit[0]
        elif _tp.tunit[0] > 0 and _tp.tunit[0] <= threshold:
            _result_tmp[0] = 2000 + _tp.tunit[0]

        first_n1_idx = _result_tmp.index(-1)
        if first_n1_idx < 3:
            _result_tmp = [x if x != -1 else 1 for x in _result_tmp]
            first_n1_idx = 3
        cale = datetime.datetime(*_result_tmp[:first_n1_idx])
        self.Time_Norm = cale.strftime(u'%Y年%m月%d日%H时%M分%S秒')
        self.time = cale
        self.time_full = _tp.tunit[:]
        self.time_origin = _tp_origin[:]
