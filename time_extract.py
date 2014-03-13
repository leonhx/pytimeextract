#!/usr/bin/env python
# coding:utf-8

from time_expr import normalizer, unit

def time_expr_extract(time_expr):
    norm = normalizer.TimeNormalizer()
    norm.parse(time_expr)
    unit = norm.getTimeUnit()
    return unit

if __name__ == '__main__':
    import sys
    assert len(sys.argv) == 2
    for s in time_expr_extract(sys.argv[1]):
        print(s)
