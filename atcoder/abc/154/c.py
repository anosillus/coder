#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# File name: c.py
# First Edit: 2020-02-09
# Last Change: 09-Feb-2020.
"""
問題文
整数列 A 1 , A 2 , .  .  .  , A Nが与えられます。
この整数列のどの 2つの要素も互いに異なるならば YES を、そうでないなら NO を出力してください。

N
A 1 .  .  .  A N
"""


N = int(input())
len_a = len(set(input().split()))

if N == len_a:
    print("YES")
else:
    print("NO")
