# -*- coding: utf-8 -*-

"""
ダイクストラ、最短経路DAG、トポロジカルソート、経路DP
"""

from scipy.sparse.csgraph import dijkstra

N = int(input())
a, b = [int(i) - 1 for i in input().split()]
M = int(input())
xM, yM = [0] * M, [0] * M
for i in range(M):
    x, y = [int(i) - 1 for i in input().split()]
    xM[i] = x
    yM[i] = y

# 始点aから全頂点への最短経路を探す(今回はダイクストラした)
dk = [[float('inf')] * N for i in range(N)]
for i in range(M):
    dk[xM[i]][yM[i]] = 1
    dk[yM[i]][xM[i]] = 1
dist = dijkstra(dk, directed=False, indices=a)
print("dist:{}".format(dist))  # 各ノードへの距離を出力[ノード0への距離,ノード1への距離,...]

# 最短経路DAGの作成
# "ある家への最短 + コスト = 次の家への最短"
# が成り立つ道のみで構成する
dag = []
for i in range(M):
    # ここではコスト = 1
    if dist[xM[i]] + 1 == dist[yM[i]]:
        dag.append((xM[i], yM[i]))
    elif dist[yM[i]] + 1 == dist[xM[i]]:
        dag.append((yM[i], xM[i]))
print("dag:{}".format(dag))
# dag:[(0, 1), (0, 2),..(出発地,目的地)]

# ここからトポロジカルソート準備
incnts = [0] * N  # 自身へ流入するノードの数
outnodes = [[] for i in range(N)]  # 自身から流出するノードのリスト
for i in range(len(dag)):
    # 流入するノード数
    incnts[dag[i][1]] += 1
    # 流出先ノードのリスト
    outnodes[dag[i][0]].append(dag[i][1])
print("incnts:{}".format(incnts))
print("outnodes:{}".format(outnodes))
# 流入ノード数が0であるノードのセットS
S = set()
for i in range(N):
    if incnts[i] == 0:
        S.add(i)
print("S:{}".format(S)) # スタートノードなどがSに追加される
# 暫定ソート結果を保持する空リストL
L = []

# ここからトポロジカルソート
# 暫定セットが空になるまでループ
# 暫定セットにあるのは自身への流入が0のもののみ
# そして暫定セットからポップしたノードの流出ノードへの流入を
# デクリメントすると、暫定セットに入っていたノードのみからしか
# 流入がないノードの流入ノード数=0となり、このノードが暫定セットへ追加される。
# このようにして暫定セットに入った順番を見ると、
# 自身への流入ノードは、自身より前に暫定セットに入っていた頂点に限られる
# よってトポロジカルソート後の頂点集合で、頭から経路数を足していけば
# DPによって経路数を算出できる
while S:
    # 暫定セットから結果リストへ1つ入れる
    L.append(S.pop())
    # 確定させたノードから流出するノードでループ
    for node in outnodes[L[-1]]:
        # 流入ノード数を1減らす
        incnts[node] -= 1
        # 流入ノードが0なら暫定セットへ
        if incnts[node] == 0:
            S.add(node)
# Sは空になっている
print("L:{}".format(L))
# 経路DP
dp = [0] * N
# 開始位置は0じゃなくてa-1,問題文でスタートが可変にされたため
dp[a] = 1
# ソート済のノードリストLでループ
for i in range(1, N):
    for j in range(len(dag)):
        # ノードL[i]が到着点となる経路があれば
        if dag[j][1] == L[i]:
            # その経路の出発点に記載された経路数を到着点に足す
            dp[dag[j][1]] += dp[dag[j][0]]
# 最終的な目的地の場所(b-1)で出力
print(dp[b] % (10 ** 9 + 7))
