#!/usr/bin/env python
# coding:utf-8

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
        startline = endline = -1
        temp = []
        rpointer = 0

        m = self.__patterns__.match(tar)
        startmark = True
        while m:
            startline = m.start()
            if endline == startline:
                rpointer -= 1
                temp[rpointer] = temp[rpointer] + m.group()
            else:
                if not startmark:
                    rpointer -= 1
                    # print temp[rpointer]
                    rpointer += 1
                startmark = False
                temp[rpointer] = m.group()
            endline = m.end()
            rpointer += 1

        if rpointer > 0:
            rpointer -= 1
            # print temp[rpointer]
            rpointer += 1

        Time_Result = [TimeUnit(t, self) for t in temp]
