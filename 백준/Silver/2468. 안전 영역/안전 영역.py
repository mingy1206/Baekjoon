from collections import deque
size = int(input())

graph = [list(map(int, input().split())) for i in range(size)]

max = max(max(x) for x in graph)

safe = 0

for k in range(max):
    visited = [[False] * size for _ in range(size)]
    cnt = 0
    if k == 0:
        safe = 1

    for i in range(size):
        for j in range(size):
            if graph[i][j] <= k:
                visited[i][j] = True

    for i in range(size):
        for j in range(size):
            if visited[i][j] == False:
                queue = deque()
                queue.append([i, j])
                cnt += 1
                visited[i][j] = True

                dx = [1, -1, 0, 0]
                dy = [0, 0, 1, -1]

                while queue:
                    y, x = queue.popleft()

                    for z in range(4):
                        nx = x + dx[z]
                        ny = y + dy[z]
                        if ny >= size or ny < 0:
                            continue
                        if nx >= size or nx < 0:
                            continue
                        if visited[ny][nx] == False:
                            queue.append([ny, nx])
                            visited[ny][nx] = True

    if cnt > safe:
        safe = cnt

print(safe)

