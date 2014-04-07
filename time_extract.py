#!/usr/bin/env python
# coding:utf-8

import sys, os
sys.path.append(os.path.abspath('./time_expr'))

import normalizer, unit

def time_expr_extract(time_expr):
    norm = normalizer.TimeNormalizer()
    return norm.parse(time_expr)

if __name__ == '__main__':
    time_exps = time_expr_extract(sys.argv[1].decode('gbk'))
    if time_exps:
        print(time_exps[0])
