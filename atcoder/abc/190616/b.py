#! /usr/local/bin/python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# File name: a.py
# First Edit: 2019-06-16
# Last Change:  16-Jun-2019.
from __future__ import print_function


def main():
    """
    問題文
    数直線上を N+1 回跳ねるボールがあり、1 回目は 座標 D1 = 0, i 回目は 座標 Di = Di−1+Li−1(2≤i≤N+1) で跳ねます。
    数直線の座標が X 以下の領域でボールが跳ねる回数は何回でしょうか。
    制約
    1≤N≤100
    1≤Li≤100
    1≤X≤10000
    入力は全て整数である入力入力は以下の形式で標準入力から与えられる。
    N XL1 L2 ... LN−1 LN
    出力
    数直線の座標が X 以下の領域でボールが跳ねる回数を出力せよ。
    """

def count_times(x, value, bounds, i):
    value += bounds[i]

    if x < value:
        print(i + 1)
    else:
        count_times(x, value, bounds, i + 1)

data = [[3, 6], [3, 4, 5]]
print(data)

x = data[0][1]
bounds = data[1]
count_times(x, 0, bounds, 0)


if __name__ == "__main__":
    # execute only if run as a script
    main()
