#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# File name: d.py
# First Edit: 2020-02-09
# Last Change: 09-Feb-2020.
"""
問題文
N個のサイコロが左から右に一列に並べてあります。左から i番目のサイコロは 1から p iまでの p i種類の目がそれぞれ等確率で出ます。
隣接する K個のサイコロを選んでそれぞれ独立に振ったとき、出る目の合計の期待値の最大値を求めてください。


N K
p 1 .  .  .  p N
"""
import numpy as np

N, K = map(int, input().split())
p = list(map(int, input().split()))

last_value = 0
l = [0]

for head, tail in zip(p, p[K:]):
    now = tail - head + last_value
    l.append(now)
    last_value = now
max_index = np.argmax(l)
max_sum = sum(p[max_index : max_index + K])
print((K + max_sum) / 2)
