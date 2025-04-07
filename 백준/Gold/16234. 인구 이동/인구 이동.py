# N×N크기의 땅, 각각의 1x1 땅에는 나라가 하나씩 존재하며, r행 c열에 있는 나라에는 A[r][c]명이 살고 있다
# 국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하라면, 두 나라가 공유하는 국경선을 오늘 하루 동안 연다
# (연합의 인구수) / (연합을 이루고 있는 칸의 개수)가 된다. 편의상 소수점은 버린다.
# 각 나라의 인구수가 주어졌을 때, 인구 이동이 며칠 동안 발생하는지 구하는 프로그램을 작성하시오. (인구 이동이 발생하는 일수가 2,000번 보다 작거나 같은 입력만 주어진다.)

# 연합은 상황에 따라서 여러 그룹이 나올 수 있음
# visited 만들고 for문에 좌표마다 bfs로 탐색, 이때 조건문으로 visited 상황을 고려해서 bfs 여부 판단
# 리스트를 복사해서 bfs에 전달
# bfs 탐색하면서 연합 조건에 맞으면, 값을 더하며 좌표를 리스트에 저장 마지막에 값/country 하고
# 다음 탐색 전에
'''
대충 이런 느낌으로 탐색
while True:
    arr_copy = copy.deepcopy(arr)
    federation = 0
    for
        for
            populatuon, target = bfs(arr_copy)
            if len(target)>=2:
                arr 반영
                federation += 1
    if federation == 0:
        break
'''
import copy
import sys
import math
from collections import deque
def main():
    N, L, R = map(int, sys.stdin.readline().split())
    A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    count = 0
    while True:
        A_copy = copy.deepcopy(A)
        federation = 0
        flag = 1
        sub_population = 0
        target = []
        visited = [[False] * N for _ in range(N)]
        for x in range(N):
            for y in range(N):
                if visited[y][x] is False:
                    sub_population, target = bfs(visited, A_copy, x, y, N, L, R)
                    federation = len(target)
                    flag *= federation
                    if federation >= 2:
                        for cx, cy in target:
                            A[cy][cx] = sub_population

        if flag >= 2:
            count += 1
        if flag <2:
            break


    print(count)

def bfs(visited, A, fx, fy, N, L, R):
    queue = deque()
    queue.append((fx,fy))
    visited[fy][fx] = True
    directions = [(1,0),(0,1),(-1,0),(0,-1)]
    population = A[fy][fx]
    target = [(fx,fy)]
    while queue:
        x,y = queue.popleft()

        for dx,dy in directions:
            nx = x + dx
            ny = y + dy

            if 0 <= nx <N and 0 <= ny < N and visited[ny][nx] is False:
                if L <= abs(A[y][x] - A[ny][nx]) <= R:
                    queue.append((nx,ny))
                    visited[ny][nx] = True
                    target.append((nx,ny))
                    population += A[ny][nx]
    return math.floor(population/len(target)), target


if __name__ == "__main__":
    main()
    
