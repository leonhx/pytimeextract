#!/usr/bin/env python
# coding:utf-8

import sys, os
sys.path.append(os.path.abspath('./time_expr'))
sys.path.append(os.path.abspath('./model'))

import datetime

import prehandler
import pattern
from unit import TimeUnit

class ReadModelError(Exception):
    def __init__(self, path):
        self.__path__ = path
    def __str__(self):
        return 'cannot read model from `%s`' % path

class TimeNormalizer:
    def __init__(self):
        self.__patterns__ = pattern.p
    def parse(self, target, time_base=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')):
        self.__target__ = target
        self.__time_base__ = time_base
        self.__old_time_base__ = time_base
        self.__pre_handling__()
        return self.__time_ex__(self.__target__, time_base)
    def __pre_handling__(self):
        self.__target__ = prehandler.rm(self.__target__, r'\s+')
        self.__target__ = prehandler.rm(self.__target__, u'的+')
        self.__target__ = prehandler.number_translator(self.__target__)
    def __time_ex__(self, tar, timebase):
        temp = []

        m = self.__patterns__.match(tar)
        while m:
            if m.start() == 0 and temp:
                temp[-1] = temp[-1] + m.group()
            else:
                startmark = False
                temp.append(m.group())
            tar = tar[m.end():]
            m = self.__patterns__.match(tar)

        Time_Result = [TimeUnit(t, self) for t in temp]
        return Time_Result
