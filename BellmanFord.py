# 入力「edges:隣接行列」「num_v:頂点数」「start:始点」
def shortest_path(edge, num_v, start):
    inf = float("inf")
    d = [inf for f in range(num_v)]
    d[start] = 0;
    while True:
        update = False
        for e in edge:
            if d[e[0]] != inf and d[e[1]] > d[e[0]] + e[2]:
                d[e[1]] = d[e[0]] + e[2]
                update = True
        if not update:
            break
    return d
edge = [[0,1,2],[0,2,5],[1,2,4],[1,3,6],[1,4,10],[2,3,2],[3,5,1],[4,5,3],[4,6,5],[5,6,9],
       [1,0,2],[2,0,5],[2,1,4],[3,1,6],[4,1,10],[3,2,2],[5,3,1],[5,4,3],[6,4,5],[6,5,9]]
print(shortest_path(edge,7,0))