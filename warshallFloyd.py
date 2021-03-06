# 入力 : 隣接行列
# 出力 : 各ノード間の距離行列
def war(dis):
    size = len(dis)
    # 非接続要素が「float("inf")」なら省略可
    for i in range(size):
        for j in range(size):
            if i != j and dis[i][j] == 0:
                dis[i][j] = float("inf")
    for k in range(size):
        for i in range(size):
            for j in range(size):
                if dis[i][j] > dis[i][k] + dis[k][j]:
                    dis[i][j] = dis[i][k] + dis[k][j]
    return dis


"""
高速化したいなら
下のようにライブラリを使うこと
import scipy.sparse.csgraph as ssc
距離行列dis = ssc.floyd_warshall(隣接行列adj)
"""
"""
import copy


# 入力:隣接行列　出力:各頂点間の最短距離
class warshallFloyd:
    def __init__(self, adj):
        # math.infはpython3.5以降のみ使用可能
        self.inf = 10 ** 9
        self.dis = copy.deepcopy(adj)
        for i in range(len(adj)):
            for j in range(len(adj)):
                if i != j and adj[i][j] == 0:
                    self.dis[i][j] = self.inf

    # 全ての頂点間の最短距離を算出、
    def search(self):
        for k in range(len(self.dis)):
            for i in range(len(self.dis)):
                for j in range(len(self.dis)):
                    if self.dis[i][j] > self.dis[i][k] + self.dis[k][j]:
                        self.dis[i][j] = self.dis[i][k] + self.dis[k][j]
        return self.dis


n, m = [int(i) for i in input().split()]
adj = [[0 for _ in range(n)] for j in range(n)]
for i in range(m):
    a, b, t = [int(i) for i in input().split()]
    adj[a - 1][b - 1] = t
    adj[b - 1][a - 1] = t

# 各頂点において、最大の最短経路が最も小さくなる場合の
# 頂点における最大の最小経路長を算出
warshal = warshallFloyd(adj)
dis = warshal.search()

minDis = warshal.inf
for i in range(n):
    # print(dis[i])
    minDis = min(minDis, max(dis[i]))
print(minDis)
"""
