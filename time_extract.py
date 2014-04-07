#!/usr/bin/env python
# coding:utf-8

import sys, os
sys.path.append(os.path.abspath('./time_expr'))

import normalizer, unit

def time_expr_extract(time_expr):
    norm = normalizer.TimeNormalizer()
    return norm.parse(time_expr)

if __name__ == '__main__':
    req = u'明天下午三点过来一下，后天上午10点我有点事情'
    time_exps = time_expr_extract(req)
    if time_exps:
        print(time_exps[0])
