from collections import deque
def bfs():
    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]
    global day

    while queue:
        z,y,x = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if nx < 0 or ny < 0 or nz < 0:
                continue
            if nx >= m or ny >= n or nz >= h:
                continue
            if graph[nz][ny][nx] != 0:
                continue

            if graph[nz][ny][nx] == 0:
                queue.append([nz, ny, nx])
                day = graph[z][y][x] + 1
                graph[nz][ny][nx] = day


m, n, h = map(int, input().split(' '))
graph = [[list(map(int, input().split(' '))) for i in range(n)]
         for j in range(h)]

check = 0
day = 1

queue = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 0:
                check = 1
            if graph[i][j][k] == day:
                queue.append([i,j,k])


if check == 0:
    print(0)
else:
    check = 0
    bfs()
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if graph[i][j][k] == 0:
                    check = 1
    if check == 1:
        print(-1)
    else:
        print(day -1)