#!/usr/bin/python
# coding: UTF-8

# import
import random  # 入力整数列Aの生成に使用


class Node:
    def __init__(self, data):  # コンストラクタ
        self.data = data  # ノードがもつ数値
        self.left = None  # 左エッジ
        self.right = None  # 右エッジ


class BST:
    def __init__(self, number_list):  # コンストラクタ
        self.root = None  # ルートノード初期化
        for node in number_list:  # 数値を持つ配列から二分木を生成
            self.insert(node)  # 挿入メソッドを使ってノードを挿入する

    # 挿入
    def insert(self, data):
        n = self.root
        if n == None:
            self.root = Node(data)
            return
        else:
            while True:
                entry = n.data
                if data < entry:
                    if n.left is None:
                        n.left = Node(data)
                        return
                    n = n.left
                elif data > entry:
                    if n.right is None:
                        n.right = Node(data)
                        return
                    n = n.right
                else:
                    n.data = data
                    return

    # 検索機能(インターフェース)
    def search(self, search):
        searcher = self._search_bool(search)
        if searcher is None:
            print("Search target is not found.")
        elif searcher == True:
            print(str(search) + " is found!")
        elif searcher == False:
            print(str(search) + " is not found.")

    # 検索機能本体(出力:boolean),深さ優先探索
    # nodeのvisitedはpopで代用
    def _search_bool(self, search):
        n = self.root
        if n is None:
            return None
        else:
            lst = []
            lst.append(n)
            while len(lst) > 0:
                node = lst.pop()
                if node.data == search:
                    return True
                if node.right is not None:
                    lst.append(node.right)
                if node.left is not None:
                    lst.append(node.left)
            return False

    def inorder(self, node):  # 中順探索 l->r->p^n
        if node is not None:
            self.inorder(node.left)
            print(node.data)
            self.inorder(node.right)


# 整数列Aの生成---------------------------------------------
# ランダム整数列Aの生成
iarray_A = list(range(50))
random.shuffle(iarray_A)
print(iarray_A)
# ---------------------------------------------------------


# テスト----------------------------------------------------
tree = BST(iarray_A)  # 配列から二分探索木生成し、treeに代入
tree.search(10)  # １０がtreeに存在するか検索
tree.inorder(tree.root)  # 中順走査、１～順にソート
# ---------------------------------------------------------
