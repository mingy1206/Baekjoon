import copy
from collections import deque

# 유튜브 참고 버전
# https://www.youtube.com/watch?v=1Ab5s8HV1ww
def bfs(tlst):
    # 3개 좌표를 1로 저장 => 벽 막기
    for i,j in tlst:
        arr[i][j]=1
    queue = deque()
    w = [[0]*M for _ in range(N)]
    cnt = CNT-3
    for ti,tj in virus:
        queue.append((ti, tj))
        w[ti][tj]=1

    while queue:
        ci, cj = queue.popleft()
        for di,dj in((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and w[ni][nj]==0 and arr[ni][nj]==0:
                queue.append((ni,nj))
                w[ni][nj]=1
                cnt-=1


    for i,j in tlst:
        arr[i][j]=0

    return cnt



"""def dfs(n, tlst):
    global ans
    if n==3:
        ans = max(ans, bfs(tlst))
        return
    for j in range(CNT):
        if v[j]==0:
            v[j]=1
            dfs(n+1, tlst+[lst[j]])
            v[j] = 0"""

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

lst = []
virus = []

# 빈칸 위치, 바이러스 위치 저장
for i in range(N):
    for j in range(M):
        if arr[i][j]==0:
            lst.append((i,j))
        elif arr[i][j]==2:
            virus.append((i,j))

CNT = len(lst)
v = [0]*CNT
ans = 0

for i in range(CNT-2):
    for j in range(i+1, CNT-1):
        for k in range(j+1, CNT):
            ans = max(ans, bfs((lst[i], lst[j], lst[k])))

print(ans)



"""
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
        for line in temp:
            print(line)

        print("------------")





n, m = map(int, input().split(' '))
graph = [list(map(int, input().split(' '))) for _ in range(n)]

max_cnt = 0

wall(0)
print(max_cnt)

"""


