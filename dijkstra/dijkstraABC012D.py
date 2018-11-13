import heapq


class dijkstra:
    def __init__(self, adj):
        self.adj = adj
        self.visited = [-1 for i in range(len(adj))]
        self.heap = []

    def allSearch(self, _start):
        # スタート地点を設定
        heapq.heappush(self.heap, [0, _start])
        # ダイクストラ法でスタート地点からの距離を算出
        while 1:
            if len(self.heap) == 0:
                break
            start = heapq.heappop(self.heap)
            # 同じノードへ複数候補がある場合がある、一度訪れたノードへの候補は削除する
            if self.visited[start[1]] != -1:
                continue
            # 確定した距離をvisitテーブルに保持
            self.visited[start[1]] = start[0]
            for i in range(len(self.adj)):
                if self.visited[i] == -1 and self.adj[start[1]][i] != 0:
                    heapq.heappush(self.heap, [self.adj[start[1]][i] + self.visited[start[1]], i])
        # print("start:{} score:{}".format(_start, max(self.visited)))
        return self.visited


n, m = [int(i) for i in input().split()]
adj = [[0 for i in range(n)] for j in range(n)]
for i in range(m):
    a, b, c = [int(i) for i in input().split()]
    adj[a - 1][b - 1] = c
    adj[b - 1][a - 1] = c
minDist = 100000
for i in range(len(adj)):
    dij = dijkstra(adj=adj)
    minDist = min(minDist, max(dij.allSearch(i)))
print(minDist)
