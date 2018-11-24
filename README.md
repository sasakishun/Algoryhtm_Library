﻿# 競技プログラミング用のアルゴリズムのライブラリ化
2018/08/01

- 実装済み
	- UnionFind木
	- 重み付きUnionFind木(WeightedUnionFind.py)2018/11/11
	- IMOS法(imos.py)2018/11/12
		- 表と領域（左下と右上により一意で定められるやつなど）が出てきたらこれを考える
	- 幅優先探索(widthSearchABC007.py)2018/11/13
 	- 深さ優先探索(depthSearchATC001A.py)2018/11/13
	- bit全探索(bitSearch.py)2018/11/20
- 実装予定
	- ダイクストラ法（ライブラリ化）
	- 二分探索木（ライブラリ化）、発見できなかった場合の不等号処理も記述
	- ミニマックス法
		- 自分の番:評価値を最大化
		- 相手の番:評価値を最小化
		- 自分が有利→正の評価値
		- 相手が有利→負の評価値
			- 要するに相手の番では```DP[l][r] = min(DP[l+1][r], DP[l][r+1])```
			のようにすればよいというだけのこと
	- アルファベータ法
	- データ構造（ビットセット、セグメント木、BIT）
	- グラフ（ベルマン・フォード、ワーシャル・フロイド、木の直径、木の重心、クラスカル、LCA）
	- 平面幾何（凸包、線分の交差）
	- その他（座標圧縮、素数modの階乗・逆元・二項係数、ナップサック問題、部分和問題、LIS）
	- 二分探索、尺取り法
	- 全域木アルゴリズム (プリム、クラスカル)
	- 動的計画法
	- ゲーム系 (2 人で行うゲームであって、メモ化が可能・もしくは小さいケースを試すと定数時間に帰着できるものが多い)
- 便利ライブラリ
	- 約数列挙```divisorEnumulation.py```2018/11/24
	- 素数判定```is_prime()```
	- 素因数分解```factorization.py```
	- 「リスト<-->文字列」変換```convertListToString.py```
- 目標
	ABCをCまで、ARCをBまで全部解く 
- 注意事項
	- 深いコピーは```copy.deepcopy(配列)```
	- ```リスト[a, b]+リスト[c, d, e]```で```[a, b, c, d, e]```となる
	- modの性質
		- ab = (Ap+x)(Bp+y) = ABp² + (Ay+Bx)p + xy ≡ xy (mod p)と出来ることから、最終的に10^9+7で割った余りを出力しろという場合では、途中積の各項を10^9+7で割った余りに置き換えてもよい
	- 1,2...nの部分和(1+3+...+n-1など)で1からn(n+1)/2のすべての整数を生成できる。
