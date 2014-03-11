#!/usr/bin/env python
# coding:utf-8

import datetime

import prehandler

class ReadModelError(Exception):
    def __init__(self, path):
        self.__path__ = path
    def __str__(self):
        return 'cannot read model from `%s`' % path

class TimeNormalizer:
    def __init__(self, filename):
        if self.__patterns__ = null:
            try:
                self.__patterns__ = self.__readModel__(filename)
            except Exception:
                raise ReadModelError(filename)
    def __read_model__(self, file):
        pass # read a Pattern
    def parse(self, target, time_base=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')):
        self.__target__ = target
        self.__time_base__ = time_base
        self.__old_time_base__ = time_base
        self.__pre_handling__()
        return self.__time_ex__(self.__target__, time_base)
    def __pre_handling__(self):
        self.__target__ = prehandler.del_keyword(target, "\\s+")
        self.__target__ = prehandler.del_keyword(target, "[的]+")
        self.__target__ = prehandler.number_translator(target)
    def __time_ex__(self, tar, timebase)
