#! /usr/local/bin/python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# File name: test.py
# First Edit: 2019-06-15
# Last Change:  16-Jun-2019.
from __future__ import print_function

from collections import Counter, deque

data = [[1, 1], [1, 2], [2, 1], [2, 2]]
x = []

for e_set in data:
    for sub_set in data:
        x.append((e_set[0] - sub_set[0], e_set[1] - sub_set[1]))

x.remove((0, 0))
val = Counter(x)
# uniqueList = list(set(x))
# uniqueList.remove((0, 0))
# print(val)
commons = val.most_common()[0][1]
ans = len(data) - commons
print(ans)
