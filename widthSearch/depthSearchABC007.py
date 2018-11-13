h, w = [int(i) + 2 for i in input().split()]
c = [["#" for i in range(w)] for j in range(h)]

sy, sx, gy, gx = 0, 0, 0, 0
for i in range(1, h - 1):
    c[i][1:-2] = input()
    for j in range(1, w - 1):
        if c[i][j] == "s":
            sy, sx = i, j
        elif c[i][j] == "g":
            gy, gx = i, j


def search(sy, sx, stack, visited, count):
    if c[sy][sx] != "#" and visited[sy][sx] == -1:
        stack.append([sy, sx])
        # print("visit to {}".format([sy, sx]))
        visited[sy][sx] = count + 1
    return


stack = [[sy, sx]]
visited = [[-1 for i in range(w)] for i in range(h)]
visited[sy][sx] = 0
count = 0
while 1:
    size = len(stack)
    # print("stack {}".format(stack))
    if size == 0:
        print("No")
        break
    [sy, sx] = stack.pop()
    count = visited[sy][sx]
    if sy == gy and sx == gx:
        print("Yes")
        # print(count)
        # for i in range(len(c)):
        # print(visited[i])
        exit()
    search(sy + 1, sx, stack, visited, count)
    search(sy - 1, sx, stack, visited, count)
    search(sy, sx + 1, stack, visited, count)
    search(sy, sx - 1, stack, visited, count)
