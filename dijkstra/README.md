# ダイクストラ法
    - 幅優先探索では、経路の重みを非考慮(単純に移動回数を最小化)
    - 幅優先探索のキューを、プライオリティキューに変更するだけ
    - ```O(n^2)```

#プライオリティキュー(heapq)の使い方
    - import heapq
    - heapq.heappush(list, (variable, label)):variableが昇順になるようにlistがソートされる