# CCTV의 위치를 저장
# 재귀를 통해서 각 CCTV의 감시 가능한 경우의 수를 구현하기
# 이때, copy.deepcopy() 이용해서 시뮬레이션 구현
import sys
import copy

def simulation(cnt, room):
    global result
    # cctv 방향 세팅
    for rotation in range(4):
        # room 깊은 복사
        copy_room = copy.deepcopy(room)

        x, y = cctv[cnt]
        cctv_kind = copy_room[y][x] - 1
        uy = direction[cctv_kind][rotation % 4]
        rx = direction[cctv_kind][(rotation + 1) % 4]
        dy = direction[cctv_kind][(rotation + 2) % 4] * -1
        lx = direction[cctv_kind][(rotation + 3) % 4] * -1
        arr = [uy, rx, dy, lx]

        for i in range(4):
            nx, ny = x, y
            nxy = arr[i]
            if nxy == 0:
                    continue

            while(True):
                if i%2==0:
                    if ny+nxy < 0 or ny+nxy >= N or copy_room[ny+nxy][x] == 6:
                        break
                    elif copy_room[ny+nxy][x] == 0:
                        copy_room[ny+nxy][x] = -1
                        ny += nxy
                    else:
                        ny += nxy
                        continue
                elif i%2==1:
                    if nx+nxy < 0 or nx+nxy >= M or copy_room[y][nx+nxy] == 6:
                        break
                    elif copy_room[y][nx+nxy] == 0:
                        copy_room[y][nx+nxy] = -1
                        nx += nxy
                    else:
                        nx += nxy
                        continue

        # 마지막 cctv 방향 세팅시 구현한 시뮬레이션 탐색
        if cnt >= len(cctv) - 1:
            temp = count(copy_room)
            if temp < result:
                result = temp
        else:
            simulation(cnt+1, copy_room)

def count(copy_room):
    cnt = 0
    for y in range(N):
        for x in range(M):
            if copy_room[y][x] == 0:
                cnt += 1
    return cnt

N,M = map(int, sys.stdin.readline().rstrip().split())
room = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
cctv = []
result = N*M
direction = [(0,1,0,0), (0,1,0,1), (1,1,0,0), (1,1,1,0), (1,1,1,1)]

for y in range(N):
    for x in range(M):
        if room[y][x] != 0 and room[y][x] != 6:
            cctv.append([x,y])

# 시뮬레이션 구현
if len(cctv) > 0:
    simulation(0, room)
    print(result)
else:
    #cctv가 없는 경우
    print(count(room))

