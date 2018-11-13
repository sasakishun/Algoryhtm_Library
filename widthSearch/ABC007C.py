R, C = [int(i) for i in input().split()]
sy, sx = [int(i) for i in input().split()]
gy, gx = [int(i) for i in input().split()]

c = [[0 for i in range(C)] for i in range(R)]
for i in range(R):
    c[i] = input()


def search(start, goal, counter, visitedCopy):
    visited = visitedCopy[:]
    visited[start[0]][start[1]] = counter
    if start[0] == goal[0] and start[1] == goal[1]:
        print("goal:{} counter:{}".format(start, counter))
        return counter

    start[0] += 1
    tmpCounter = 10000
    if 0 <= start[0] < R and 0 <= start[1] < C \
            and visited[start[0]][start[1]] == 0\
            and c[start[0]][start[1]] != "#":
        counter += 1
        tmpCounter = min(tmpCounter, search(start, goal, counter, visitedCopy=visited))
    start[0] -= 1

    start[0] -= 1
    if 0 <= start[0] < R and 0 <= start[1]< C \
            and visited[start[0]][start[1]] == 0\
            and c[start[0]][start[1]] != "#":
        counter += 1
        tmpCounter = min(tmpCounter, search(start, goal, counter, visitedCopy=visited))
    start[0] += 1

    start[1] += 1
    if 0 <= start[0] < R and 0 <= start[1]< C \
            and visited[start[0]][start[1]] == 0\
            and c[start[0]][start[1]] != "#":
        counter += 1
        tmpCounter = min(tmpCounter, search(start, goal, counter, visitedCopy=visited))
    start[1] -= 1

    start[1] -= 1
    if 0 <= start[0] < R and 0 <= start[1]< C \
            and visited[start[0]][start[1]] == 0\
            and c[start[0]][start[1]] != "#":
        counter += 1
        tmpCounter = min(tmpCounter, search(start, goal, counter, visitedCopy=visited))
    start[1] += 1
    return counter + tmpCounter

visited = [[0 for i in range(C)] for i in range(R)]
print(search(start=[sy-1, sx-1], goal=[gy-1, gx-1], counter=0, visitedCopy=visited))
"""
for i in range(R):
    print(visited[i])
for i in range(R):
    print(c[i])
"""