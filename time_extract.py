#!/usr/bin/env python
# coding:utf-8

import sys, os
sys.path.append(os.path.abspath('./time_expr'))

import normalizer, unit

def win32_unicode_argv():
    """Uses shell32.GetCommandLineArgvW to get sys.argv as a list of Unicode
    strings.

    Versions 2.x of Python don't support Unicode in sys.argv on
    Windows, with the underlying Windows API instead replacing multi-byte
    characters with '?'.
    """

    from ctypes import POINTER, byref, cdll, c_int, windll
    from ctypes.wintypes import LPCWSTR, LPWSTR

    GetCommandLineW = cdll.kernel32.GetCommandLineW
    GetCommandLineW.argtypes = []
    GetCommandLineW.restype = LPCWSTR

    CommandLineToArgvW = windll.shell32.CommandLineToArgvW
    CommandLineToArgvW.argtypes = [LPCWSTR, POINTER(c_int)]
    CommandLineToArgvW.restype = POINTER(LPWSTR)

    cmd = GetCommandLineW()
    argc = c_int(0)
    argv = CommandLineToArgvW(cmd, byref(argc))
    if argc.value > 0:
        start = argc.value - len(sys.argv)
        return [argv[i] for i in xrange(start, argc.value)]

sys.argv = win32_unicode_argv()

def time_expr_extract(time_expr):
    norm = normalizer.TimeNormalizer()
    return norm.parse(time_expr)

if __name__ == '__main__':
    assert len(sys.argv) == 2
    for s in time_expr_extract(sys.argv[1]):
        print(s.__str__().encode(sys.stdout.encoding))
