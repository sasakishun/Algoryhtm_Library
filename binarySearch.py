class binarySearch():
    # 入力tableはソートされていることが前提
    def __init__(self, table):
        self.table = table

    # min(table) <= target <= max(table)が前提
    def search(self, target):
        low = 0
        high = len(self.table)
        # t は中央番目の数
        t = int((low + high) / 2)

        # 探索の下限のlowが上限のhighになるまで探索
        # lowがhighに達すると数は見つからなかったということ
        while high >= low:
            if target == self.table[t]:
                break
            elif target > self.table[t]:
                low = t + 1
            elif target < self.table[t]:
                high = t - 1
            t = int((low + high) / 2)
        if target == self.table[t]:
            print(str(t) + "番目にあります")
        else:
            print("x[high:{}]:{} < i:{} < x[low:{}]:{} \nありません".format(high, self.table[high], target, low, self.table[low]))

x = [1, 8, 14, 23, 44, 55, 67, 88, 103, 146]
binary = binarySearch(x)
for i in range(min(x), max(x) + 1):
    binary.search(i)
    print()