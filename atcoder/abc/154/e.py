#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# File name: e.py
# First Edit: 2020-02-09
# Last Change: 09-Feb-2020.
"""

問題文
1以上N以下の整数であって、10進法で表したときに、0でない数字がちょうどK個あるようなものの個数を求めてください。

N
K
"""
# from scipy.misc import comb
import math

import numpy as np


N = int(input())
K = int(input())


def count_0(range_value, zero_count):
    k = 0

    for i in range(range_value):
        if str(i).count("0") == zero_count:
            k += 1

    return k


print(count_0(N, K))
