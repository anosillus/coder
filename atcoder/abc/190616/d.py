#! /usr/local/bin/python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# File name: a.py
# First Edit: 2019-06-16
# Last Change:  16-Jun-2019.
from __future__ import print_function


def value_check(value, current_i, end_i):
    now = value - arrays[current_i]
    # print(f"{arrays[current_i]} {current_i} is current,  {end_i} is end_i")
    # print(f"{now} is now")

    if now <= 0:
        return end_i - current_i + 1

    if end_i == current_i:
        return 0
    else:
        return value_check(now, current_i + 1, end_i)


data = list(map(int, input().split()))
arrays = list(map(int, input().split()))
# data = [4, 10]
# arrays = [6, 1, 2, 7]

# print(data)
width = data[0]
value = data[1]
ans = 0

for i in range(width):
    ans += value_check(value, current_i=i, end_i=width - 1)
print(ans)
