# 격자 생성
# 드래곤 커브 모듈 구현
# -> 이전 시나리오를 저장하면서 각 세대마다 각 시나리오의 방향을 + 반시계방향 90도(문제에서 DC는 시계지만 구현의 편의성을 위해서 방향은 반시계)로 변경
# 1x1 정사각형 count 함수 구현
# 정사각형 구하기 -> x,y / x+1,y / x,y+1 / x+1,y+1이 드래곤 커브인 경우의 개수 구현
# 탐색할 때는 미리 구한 값들을 탐색하면서 인접한지 판단

import sys
from collections import deque
N = int(sys.stdin.readline().rstrip())

arr = [[0]*N for _ in range(N)]
dc = []
directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
result = 0

for i in range(N):
    x,y,d,G = map(int, sys.stdin.readline().rstrip().split())
    S = []
    # 0세대
    S.append([x, y, d, 0])
    dc.append((x,y))
    if G == 0:
        dx, dy = directions[d]
        nx = x + dx
        ny = y + dy
        dc.append((nx, ny))
    # 1~G세대
    for j in range(0, G):
        temp = []
        for k in range(0, (2 ** j)):
            x, y, d, g = S[-(k + 1)]
            dx, dy = directions[d]
            if k == 0:
                nx = x + dx
                ny = y + dy
            elif k > 0:
                tempd = temp[k - 1][2]
                tdx, tdy = directions[tempd]
                nx = temp[k - 1][0] + tdx
                ny = temp[k - 1][1] + tdy
            dc.append((nx, ny))

            temp.append([nx, ny,(d+1) % 4,j+1])

        for t in range(len(temp)):
            S.append(temp[t])
            if t == len(temp)-1 and j == G-1:
                x,y,d,g = temp[t]
                dx, dy = directions[d]
                S.append([x+dx, y+dy, S[0][2]+1, G])
                dc.append((x+dx, y+dy))
dc = set(dc)
for x,y in dc:

    if (x+1,y) in dc and (x,y+1) in dc and (x+1,y+1) in dc:
        result += 1

print(result)



