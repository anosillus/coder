# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# File name: paiza_b.py
# First Edit: 2019-06-15
# Last Change: 15-Jun-2019.

"""
問題文
2 次元平面上に N 個のボールがあり、i 番目のボールは (xi,yi) にあります。まず、p≠0 または q≠0 を満たす 2 つの整数 p,q を決め、その後以下の操作を繰り返してボールを全て回収します。
残っているボールを 1 つ選んで回収する。このボールの座標を (a,b) とする。この時、直前に選んだボールの座標が (a−p,b−q) である時コスト 0 、そうでない時コスト 1 かかる。ただし、1 つ目に選んだボールについては必ずコスト 1 かかる。p,q を最適に選んだ場合にボールを全て回収するのにかかるコストの和の最小値を計算してください。
制約
1≤N≤50|xi|,|yi|≤109xi≠xj または yi≠yj(i≠j)
入力は全て整数である入力入力は以下の形式で標準入力から与えられる。
N
x1 y1
.
.
.
xN yN
出力ボールを全て回収するのにかかるコストの和の最小値を出力せよ。"""


from collections import Counter

# data = [[1, 1], [1, 2], [2, 1], [2, 2]]
# N = len(data)

data = []
N = int(input())

for i in range(N):
    data.extend([list(map(int, input().split(" ")))])
x = []

for e_set in data:
    for sub_set in data:
        x.append((e_set[0] - sub_set[0], e_set[1] - sub_set[1]))
a = (0, 0)

while a in x:
    x.remove(a)
val = Counter(x)

common_times = val.most_common()[0][1]
ans = N - common_times

print(ans)
