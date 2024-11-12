from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]


year = 0

while True:
    visited = [[False] * m for _ in range(n)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    cnt = 0
    for y in range(n):
        for x in range(m):
            if graph[y][x] != 0 and visited[y][x] == False:

                cnt += 1
                queue = deque()
                queue.append([x, y])
                visited[y][x] = True
                while queue:

                    a, b = queue.popleft()
                    for i in range(4):
                        nx = a + dx[i]
                        ny = b + dy[i]
                        if nx >= m or ny >= n or nx < 0 or ny < 0:
                            continue
                        if graph[ny][nx] == 0 and graph[b][a] > 0 and visited[ny][nx] == False:
                            graph[b][a] -= 1
                            if graph[b][a] == 0:
                                visited[b][a] = True
                        if graph[ny][nx] != 0 and visited[ny][nx] == False:
                            queue.append([nx, ny])
                            visited[ny][nx] = True



    if cnt == 0:
        print(0)
        break
    elif cnt >= 2:
        print(year)
        break
    year += 1