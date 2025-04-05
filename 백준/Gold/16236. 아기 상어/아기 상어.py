# NxN, 아기 상어 초기 크기 2
# 아기 상어 이동은 상하좌우 1칸에 1초, 먹는 시간 0
# 아기 상어보다 크기가 크면 갈 수 없다, 크기가 같으면 지나갈 수는 있다, 크기가 작으면 먹을 수 있다.
# 자기 크기의 수만큼 먹으면 사이즈 +1 ex) 크기가 2인 아기상어는, 물고기 2마리를 먹으면 크기가 3이 된다.
# 아기 상어보다 크기가 작은 물고기 중에서, 최단 거리 순서로 가장 가까운 물고기를 먹으러 간다.
# 이때, 거리가 같으면 1. 더 위쪽 -> 2. 더 왼쪽에 있는 물고기 먼저 먹는다. -> xy 기준 y를 먼저
# 먹을 수 있는 물고기가 없으면, 엄마 상어를 부른다. -> 종료

# BFS 사용해서 해당 칸의 물고기와 아기상어의 현재 크기를 비교

import sys
from collections import deque
def main():
    N = int(sys.stdin.readline())
    sea = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    x = -1
    y = -1
    eat_fish = 0
    shark_size = 2
    time = 0
    for i in range(N):
        for j in range(N):
            if sea[i][j] == 9:
                x = j
                y = i
    while True:
        distance, x, y = bfs(N, sea, shark_size, x, y)
        if distance == -1 and x == -1 and y ==-1:
            break
        time += distance - 1
        eat_fish += 1
        if eat_fish == shark_size:
            shark_size += 1
            eat_fish = 0


    print(time)
def bfs(N, sea, shark_size, start_x, start_y):
    queue = deque()
    queue.append((start_x,start_y))
    directions = [(1,0), (0,1), (-1,0), (0,-1)]
    visited = [[0]*N for _ in range(N)]
    visited[start_y][start_x] = 1
    result = []
    x = -1
    y = -1
    while queue:
        x,y = queue.popleft()
        for dx,dy in directions:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if visited[ny][nx] == 0 and sea[ny][nx] <= shark_size:
                    queue.append((nx,ny))
                    visited[ny][nx] = visited[y][x] + 1
        if sea[y][x] != 9 and sea[y][x] > 0 and sea[y][x] < shark_size:
            distance = visited[y][x]
            result.append((x,y,distance))
            while queue:
                x,y = queue.popleft()
                if sea[y][x] != 9 and sea[y][x] > 0 and sea[y][x] < shark_size and visited[y][x] <= distance:
                    result.append((x,y,visited[y][x]))
            break

    if result:
        best_x = result[0][0]
        best_y = result[0][1]
        best_distance =result[0][2]
        for x,y,distance in result:
            if  best_distance > distance:
                best_x = x
                best_y = y
                best_distance = distance

            elif best_distance == distance:
                if best_y > y:
                    best_x = x
                    best_y = y
                    best_distance = distance

                elif best_y == y:
                    if best_x > x:
                        best_x = x
                        best_y = y
                        best_distance = distance
        sea[start_y][start_x] = 0
        sea[best_y][best_x] = 9
        return (best_distance,best_x,best_y)
    elif not result:
        return (-1,-1,-1)




main()
