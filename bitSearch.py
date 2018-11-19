N = [i for i in range(10)]  # N = bit探索する桁数
# Nの要素の全組み合わせが出力
for i in range(1, 1 << len(N)):
    output = []
    for j in range(len(N)):
        if ((i >> j) & 1) == 1:
            output.append(j)  # このjが今回探索するindexの1つ
    print(output)
