import copy
from collections import deque

def virus(temp):
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    queue = deque()

    for y in range(n):
        for x in range(m):
            if temp[y][x] == 2:
                queue.append((x, y))
    while(queue):
        x, y = queue.popleft()
        for dx,dy in directions:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < m and 0 <= ny < n and temp[ny][nx] == 0:
                temp[ny][nx] = 2
                queue.append((nx, ny))


def wall(cnt):
    for i in range(n):
        for j in range(m):
            if cnt == 3:
                temp = copy.deepcopy(graph)
                virus(temp)
                count(temp)
                return
            if graph[i][j] == 0:
                graph[i][j] = 1
                wall(cnt+1)
                graph[i][j] = 0

def count(temp):
    cnt = 0
    global max_cnt
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
              cnt += 1

    if cnt > max_cnt:
        max_cnt = cnt
        """for line in temp:
            print(line)

        print("------------")"""





n, m = map(int, input().split(' '))
graph = [list(map(int, input().split(' '))) for _ in range(n)]

max_cnt = 0

wall(0)
print(max_cnt)




