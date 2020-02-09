#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# File name: a.py
# First Edit: 2020-02-09
# Last Change: 09-Feb-2020.
"""
A-REmaining Balls
文字列 Sの書かれたボールが A個、文字列 Tの書かれたボールが B個あります。高橋君は、文字列 Uの書かれたボールを 1個選んで捨てました。
文字列 S , Tの書かれたボールがそれぞれ何個残っているか求めてください。

S T
A B
U

red blue
3 4
red

> 2 4
"""


S, T = input().split()
s_i, t_i = map(int, input().split())
U = input()

if U == S:
    print(str(s_i - 1) + " " + str(t_i))
else:
    print(str(s_i) + " " + str(t_i - 1))
