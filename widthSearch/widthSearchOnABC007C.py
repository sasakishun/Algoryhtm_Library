import queue

R, C = [int(i) for i in input().split()]
sy, sx = [int(i)-1 for i in input().split()]
gy, gx = [int(i)-1 for i in input().split()]

c = [[0 for i in range(C)] for i in range(R)]
for i in range(R):
    c[i] = input()

queue = queue.Queue()
queue.put([sy, sx])
visited = [[-1 for i in range(C)] for i in range(R)]
count = 0


def search(sy, sx, queue, visited):
    if c[sy][sx] != "#" and visited[sy][sx] == -1:
        queue.put([sy, sx])
        visited[sy][sx] = 1
    return


while 1:
    size = queue.qsize()
    for i in range(size):
        [sy, sx] = queue.get()
        visited[sy][sx] = count
        if sy == gy and sx == gx:
            print(count)
            exit()
        search(sy+1, sx, queue, visited)
        search(sy-1, sx, queue, visited)
        search(sy, sx+1, queue, visited)
        search(sy, sx-1, queue, visited)
    count += 1