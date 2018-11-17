# 入力 : 自然数     ex) 12
# 出力 : 約数リスト ex) [2, 2, 3]
def factorization(n):
    R = int(n)
    s = 0
    L = []
    div = 2
    while s == 0:
        for i in range(div, R + 1):
            if n % i == 0:
                n = n / i
                div = i
                if n == 1:
                    s = 1
                L.append(i)
                break
    return L
