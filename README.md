﻿# 競技プログラミング用のアルゴリズムのライブラリ化
2018/08/01

- 実装済み
	- UnionFind木
	- 重み付きUnionFind木(WeightedUnionFind.py)2018/11/11
	- IMOS法(imos.py)2018/11/12
		- 表と領域（左下と右上により一意で定められるやつなど）が出てきたらこれを考える
		- 区間[a,b]の要素和はimos[b]-imos[a-1]であることに注意
	- 幅優先探索(widthSearchABC007.py)2018/11/13
 	- 深さ優先探索(depthSearchATC001A.py)2018/11/13
	- ダイクストラ法(dijkstra.py)2018/11/14 O(E*LogV)
		- 非負の辺にのみ対応（負対応はワーシャルフロイドとベルマンフォード）
	- bit全探索(bitSearch.py)2018/11/20
	- 経路総数(dijkstra/routeCountingABC021C.py)2018/12/01
		- dijkstra -> トポロジカルソート -> 経路総数DP
	- 二分探索(binarySearch.py)2018/12/03
		- 発見できなかった場合の不等号処理も記述
	- ワーシャル・フロイドO(V^3) (warshallFloyd.py)
- 実装予定
	- ミニマックス法
		- 自分の番:評価値を最大化
		- 相手の番:評価値を最小化
		- 自分が有利→正の評価値
		- 相手が有利→負の評価値
			- 要するに相手の番では```DP[l][r] = min(DP[l+1][r], DP[l][r+1])```
			のようにすればよいというだけのこと
	- アルファベータ法
	- データ構造（ビットセット、セグメント木(ARC045B)、BIT）
	- グラフ（木の直径、木の重心、クラスカル、LCA）
	- ベルマン・フォードO(VE)
		- 負の閉路がなければ、最短経路長の更新は有限回で終わることによる
	- 平面幾何（凸包、線分の交差）
	- その他（座標圧縮、素数modの階乗・逆元・二項係数、ナップサック問題、部分和問題、LIS）
	- 尺取り法(ARC022B)で対処可能な問題
		- 「条件」を満たす区間 (連続する部分列) の長さの最小と最大
		- 「条件」を満たす区間 (連続する部分列) の数え上げ
			- 尺取り法で得られた区間において、その部分列も「条件」を満たすので,単純にその区間の
			部分列の選び方が,条件を満たす場合の数になる。
	- 全域木アルゴリズム (プリム、クラスカル)
	- 動的計画法'(漸化式を設定、シード値を決定、ループを回す)
	- ゲーム系 (2 人で行うゲームであって、メモ化が可能・もしくは小さいケースを試すと定数時間に帰着できるものが多い)
- 便利ライブラリ
	- 約数列挙```divisorEnumulation.py```2018/11/24
	- 素数判定```is_prime()```
	- 素因数分解```factorization.py```
	- 「リスト<-->文字列」変換```convertListToString.py```
	- 組み合わせ数は```math.factorial(n) // (math.factorial(n - r) * math.factorial(r))```
- 目標
	- ABCをCまで(Cの残り1門が計算量的に難しいかもしれない 2018/12/31)->ABC完了(2019/01/11)、ARCをBまで全部解く、その後ABCのDを全部解く
		- 400点問題を優先して解く
		- 700点問題でも解ける場合ありAGC031B（模範解答より簡単な解き方を使用）
	- マイページ(https://atcoder.jp/users/shunsasa)
- 注意事項
	- 深いコピーは```copy.deepcopy(配列)```
	- ```リスト[a, b]+リスト[c, d, e]```で```[a, b, c, d, e]```となる
	- modの性質
		- ab = (Ap+x)(Bp+y) = ABp² + (Ay+Bx)p + xy ≡ xy (mod p)と出来ることから、最終的に10^9+7で割った余りを出力しろという場合では、途中積の各項を10^9+7で割った余りに置き換えてもよい
	- 1,2...nの部分和(1+3+...+n-1など)で1からn(n+1)/2のすべての整数を生成できる。
	- 文字列を数式として評価したい場合はeval()を使用　eval("2*3")->6
	- 多次元リストのソートでは、配列.sort(key=itemgetter(0))のように、ラムダ式を引数に入れることで、任意の要素、条件でソート可能。
	- 除算結果をint()でキャストするより、切り捨て除算演算子```//```を使った方が丸め誤差が少ない。最大公約数の計算などでは必ずこれを使うべき。
	- 値が大きすぎるとmath.ceilでミスが発生する。代わりに```a // b + (a % b == 0 ? 0: 1)```の意味の式を使用する。
	- 逆元:素数で割った余りを求めるとき、元の式の割り算は掛け算に変換可能
		- ```(x // a) % m -> (x * (a)^(m-2)) % m```　となる。
		- フェルマーの小定理```a^(p-1)≡1 mod(p) ただしpは素数```により簡単に証明可能
	- ```pow(a, b, c)=(a\*\*b)%c```
	- ウィルソンの定理（素数modの階乗）:pが素数であることと```(p − 1)! ≡ −1 (mod p)```は必要十分条件
	- リストの初期化は、リスト内包表記よりも```array = [0]*10```とした方が高速？->原因を調べるべき(18/12/21)
		- ただし多次元でこれを使うとミス発生(```[[[0]*10]*10]*10```だと同じリスト```[0]*10```を参照することになるから)
	- mメモ化の際に、```memo=dict()```とし文字列をkeyとして格納することで、```memo[1 << n - 1]=k```などとするより理解しやすくなる。(ABC025C)
	- 斜めimos法(ABC018)
		- 菱形を1マスずつ動かすような場合は,斜め方向に累積和を取ることで,上端から右端までの和をO(1)で算出できるので計算量を減らせる
	- pythonで何度も```n**3```のような累乗を繰り返すと計算量増加(累乗した分だけ掛け算を実行するため毎回n回積を取るとオーダーがn倍になる)
	- pythonは関数化すると高速になる？、ワーシャルフロイドを関数呼び出しにするとatcoderのTLEを解決ABC073D
	- 深さ優先探索は再帰関数ではなく、stackを使うべき(depthエラーになるから)
	- 各試行にO(logn)しかかからない(2分探索など)なら、10^5程度の種類を全部試せる
	- リスト内包表記でのif文は```[0 if i % 2 == 0 else 1 for i in range(10)]```
	- pythonではO(10^6)は無理(AGC033A)
		- C++をやるべき
