import math


# 条件式「condition」を満たす引数tの中で
# 最小となるtを出力
class binarySearch:
    # 添え字「t」によってソート済みリストを二分探索
    def __init__(self, limit):
        self.limit = limit  # 上限
        self.t = 0

    # 問題によってここを書き換える
    def condition(self, h, a, b):
        if self.t < 0:
            return False
        count = 0
        for i in range(len(h)):
            if h[i] > b * self.t:
                count += math.ceil((h[i] - b * self.t) / (a - b))
        if count > self.t:
            return False
        else:
            return True

    def search(self, h, a, b):
        low = 0
        high = self.limit
        self.t = int((low + high) / 2)
        while high >= low:
            out = self.condition(h, a, b)
            if not out:
                low = self.t + 1
            else:
                high = self.t - 1
            self.t = int((low + high) / 2)
        return self.t + 1


# ABC063D
n, a, b = [int(i) for i in input().split()]
h = [0 for _ in range(n)]
for i in range(n):
    h[i] = int(input())
binary = binarySearch(limit=math.ceil(max(h) / 1))
print(binary.search(h, a, b))
