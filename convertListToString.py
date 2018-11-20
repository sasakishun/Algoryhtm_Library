def listToString(_list, split=""):
    maped_list = map(str, _list)  # mapで要素すべてを文字列に
    mojiretu = split.join(maped_list)
    return mojiretu


def stringToList(_string, split=" "):
    str_list = []
    temp = ''
    for x in _string:
        if x == split:  # 区切り文字
            str_list.append(temp)
            temp = ''
        else:
            temp += x
    if temp != '':  # 最後に残った文字列を末尾要素としてリストに追加
        str_list.append(temp)
    return str_list


print(listToString([0 for i in range(5)]))  # -> 00000
print(stringToList("0 0 0 0 0"))  # ->['0', '0', '0', '0', '0']
