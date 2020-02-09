#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# File name: tetst.py
# First Edit: 2020-02-09
# Last Change: 09-Feb-2020.
"""
This scrip is for test

"""

l3 = [0]


def count_0(range_value, zero_count):
    l = []

    for i in range(range_value):
        if str(i).count("0") == zero_count:
            l.append(i)

    return l


k = count_0(500, 2)
print(k)
