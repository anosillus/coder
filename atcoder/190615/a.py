#! /usr/local/bin/python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# File name: a.py
# First Edit: 2019-06-15
# Last Change:  16-Jun-2019.
from __future__ import print_function


def main():
    """
    N(ボール)  K(人数)
ボールの個数の差としてあり得る最大値を出力せよ。
"""
    data = []

    data.extend(list(map(int, input().split(" "))))
    n = data[0]
    k = data[1]

    if n == 1:
        print(0)
    else:
        print(n - k)
