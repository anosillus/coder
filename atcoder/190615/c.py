# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# File name: c.py
# First Edit: 2019-06-15
# Last Change:  15-Jun-2019.
from __future__ import print_function

# data = []
# N = int(input())
# data.extend([list(map(int, input().split(' ')))])

data = ("1 -1 2").split(" ")
data = map(int, data)

if 4 % 2 == 0:
    print("g")
else:
    print("k")


def make_minus(l):
    min_n = l.min() - l.max()


def make_big(l):
    max_n = l.max() - l.min()
