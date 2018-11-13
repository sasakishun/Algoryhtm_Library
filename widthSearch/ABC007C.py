R, C = [int(i) for i in input().split()]
sy, sx = [int(i) for i in input().split()]
gy, gx = [int(i) for i in input().split()]

c = [[0 for i in range(C)] for i in range(R)]
for i in range(R):
    c[i] = input()


def search(start, goal, counter, visited):
    print(start)
    visited[start[0]][start[1]] = counter
    if start[0] == goal[0] and start[1] == goal[1]:
        print("goal:{}".format(start))
        return counter

    start[0] += 1
    tmpCounter = 10000
    if 0 <= start[0] < R and 0 <= start[1]< C \
            and visited[start[0]][start[1]] == 0\
            and c[start[0]][start[1]] != "#":
        counter += 1
        tmpCounter = min(tmpCounter, search(start, goal, counter, visited=visited))
    start[0] -= 1

    start[0] -= 1
    if 0 <= start[0] < R and 0 <= start[1]< C \
            and visited[start[0]][start[1]] == 0\
            and c[start[0]][start[1]] != "#":
        counter += 1
        tmpCounter = min(tmpCounter, search(start, goal, counter, visited=visited))
    start[0] += 1

    start[1] += 1
    if 0 <= start[0] < R and 0 <= start[1]< C \
            and visited[start[0]][start[1]] == 0\
            and c[start[0]][start[1]] != "#":
        counter += 1
        tmpCounter = min(tmpCounter, search(start, goal, counter, visited=visited))
    start[1] -= 1

    start[1] -= 1
    if 0 <= start[0] < R and 0 <= start[1]< C \
            and visited[start[0]][start[1]] == 0\
            and c[start[0]][start[1]] != "#":
        counter += 1
        tmpCounter = min(tmpCounter, search(start, goal, counter, visited=visited))
    start[0] += 1
    return counter + tmpCounter

visited = [[0 for i in range(C)] for i in range(R)]
print(search(start=[sy-1, sx-1], goal=[gy-1, gx-1], counter=0, visited=visited))
#visited[gy-1][gx-1] = 2
for i in range(R):
    print(visited[i])
for i in range(R):
    print(c[i])