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
    X,A は 0 以上 9 以下の整数です。X が A 未満の時 0、A 以上の時 10 を出力してください。
    制約
    0≤X,A≤9入力は全て整数である
    入力
    入力は以下の形式で標準入力から与えられる。
    X A
    """

    data = ["7", "6"]

    # data.extend(list(map(int, input().split(" "))))

    if data[0] < data[1]:
        print(0)
    else:
        print(10)


if __name__ == "__main__":
    # execute only if run as a script
    main()
