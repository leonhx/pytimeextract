#!/usr/bin/env python
# coding: utf-8

import re

def rm(target, pattern):
    pattern = re.compile(pattern)
    return re.sub(pattern, '', target)

def number_translator(target):
    def num_han(base):
        def get_num(s):
            num = 0
            if len(s) == 2:
                num += __word2num__(s[0])*10*base + __word2num__(s[1])*base
            return num
        return get_num

    target = __num__(target, u'[一二两三四五六七八九123456789]万[一二两三四五六七八九123456789](?!(千|百|十))', u'万', num_han(1000))
    target = __num__(target, u'[一二两三四五六七八九123456789]千[一二两三四五六七八九123456789](?!(百|十))', u'千', num_han(100))
    target = __num__(target, u'[一二两三四五六七八九123456789]百[一二两三四五六七八九123456789](?!十)', u'百', num_han(10))
    target = __num0__(target, u'[零一二两三四五六七八九]')
    target = __num0__(target, u'(?<=周)[天日]|(?<=星期)[天日]')

    def num_digit(base):
        def get_num(s):
            num = 0
            if len(s) == 0:
                num += base
            elif len(s) == 1:
                coef = int(s[0])
                if coef == 0:
                    num += base
                else:
                    num += coef * base
            elif len(s) == 2:
                if s[0] == '':
                    num += base
                else:
                    coef = int(s[0])
                    if coef == 0:
                        num += base
                    else:
                        num += coef * base
                if s[1] != '':
                    num += int(s[1])
            return num
        return get_num

    target = __num__(target, u'(?<!周)0?[0-9]?十[0-9]?|(?<!星期)0?[0-9]?十[0-9]?', u'十', num_digit(10))
    target = __num__(target, u'0?[1-9]百[0-9]?[0-9]?', u'百', num_digit(100))
    target = __num__(target, u'0?[1-9]千[0-9]?[0-9]?[0-9]?', u'千', num_digit(1000))
    target = __num__(target, u'[0-9]+万[0-9]?[0-9]?[0-9]?[0-9]?', u'万', num_digit(10000))

    return target

def __num__(target, regex, unit, get_num):
    pattern = re.compile(regex)
    res = u''
    m = pattern.search(target)
    while m:
        group = m.group()
        s = group.split(unit)
        res += target[:m.start()] + str(get_num(s))
        target = target[m.end():]
        m = pattern.search(target)
    res += target
    return res

def __num0__(target, regex):
    pattern = re.compile(regex)
    res = u''
    m = pattern.search(target)
    while m:
        res += target[:m.start()] + str(__word2num__(m.group()))
        target = target[m.end():]
        m = pattern.search(target)
    res += target
    return res

def __word2num__(s):
    word_num_dict = {
        u'零': 0, '0': 0, '': 0,
        u'一': 1, '1': 1,
        u'二': 2, u'两': 2, '2': 2,
        u'三': 3, '3': 3,
        u'四': 4, '4': 4,
        u'五': 5, '5': 5,
        u'六': 6, '6': 6,
        u'七': 7, u'天': 7, u'日': 7, '7': 7,
        u'八': 8, '8': 8,
        u'九': 9, '9': 9,
    }
    return word_num_dict.get(s, -1)

if __name__ == '__main__':
    t1 = u'一千三百五十二年以前'
    t2 = u'两千零二年'
    print number_translator(t1)
    print number_translator(t2)
