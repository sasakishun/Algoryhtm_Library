﻿# 競技プログラミング用のアルゴリズムのライブラリ化
2018/08/01

- 実装済み
	- UnionFind木
	- 重み付きUnionFind木(WeightedUnionFind.py)2018/11/11
	- IMOS法(imos.py)2018/11/12
	- 幅優先探索(widthSearchABC007.py)2018/11/13
 	- 深さ優先探索(depthSearchATC001A.py)20218/11/13
- 実装予定
	- ダイクストラ法（ライブラリ化）
	- 二分探索木（ライブラリ化）、発見できなかった場合の不等号処理も記述
	- bit全探索
	- ミニマックス法
		- 自分の番:評価値を最大化
		- 相手の番:評価値を最小化
		- 自分が有利→正の評価値
		- 相手が有利→負の評価値
			- 要するに相手の番では```DP[l][r] = min(DP[l+1][r], DP[l][r+1])```
			のようにすればよいというだけのこと
	- アルファベータ法
	- データ構造（ビットセット、union-find、セグメント木、BIT）
	- グラフ（ベルマン・フォード、ワーシャル・フロイド、木の直径、木の重心、クラスカル、LCA）
	- 平面幾何（凸包、線分の交差）
	- その他（座標圧縮、素数modの階乗・逆元・二項係数、ナップサック問題、部分和問題、LIS）
	- しゃくとり法
- 便利ライブラリ
	- 約数列挙```$$O(\sqrt{n})$$```
	- 素数判定```is_prime()```
