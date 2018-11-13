# 幅優先探索
	- queueの中身全てをgetし、探索可能地点を得る。これを現地点とする。
	- 各現地点から探索可能な地点をQueueにputする。
	- putする際に探索済リスト(visited[])にチェックする(こうしないと```探索可能地点数×Queueのサイズ```)
	- countを1インクリメント
	- これを繰り返す
		- pythonのリスト、配列は参照渡し(Cと同じ)
# Queueの使い方(python3)
	- import queue
	- インスタンス化 ```queue.Queue()```
	- ポップ```queue.put(variable)```
	- プッシュ```queue.get()```
	- サイズ取得```queue.qsize()```
