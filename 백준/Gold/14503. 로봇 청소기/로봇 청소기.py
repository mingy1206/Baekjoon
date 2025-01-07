import sys

N, M = map(int, sys.stdin.readline().strip().split())
r, c, d = map(int, sys.stdin.readline().strip().split())
room = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

directions =[(0, -1), (1, 0), (0, 1), (-1, 0)] # 순서대로 북, 동, 남, 서 => +90 degree
clean_box = 0

while(True):
    directions_count = 0

    if room[r][c] == 0:
        clean_box += 1
        room[r][c] = 2

    for dc, dr in directions:
        nr, nc = r + dr, c + dc
        if room[nr][nc] == 0:
            directions_count += 1

    if directions_count == 0:
        dc, dr = directions[d]

        # 후진이 벽이거나 범위를 벗어날 경우
        if room[r - dr][c- dc] == 1 \
                or 0 > r - dr or r - dr >= N \
                or 0 > c - dc or c - dc >= M:
            break
        else:
            r, c = r - dr, c - dc
    elif directions_count != 0:
        # 반시계 방향 회전
        d = d - 1
        if d < 0:
            d = 3

        dc, dr = directions[d]
        nr, nc = r + dr, c + dc

        if room[nr][nc] == 0:
            r = nr
            c = nc

print(clean_box)


"""
1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
2. 현재 칸의 주변 $4$칸 중 청소되지 않은 빈 칸이 없는 경우,
    2A. 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
    2B. 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
3. 현재 칸의 주변 $4$칸 중 청소되지 않은 빈 칸이 있는 경우,
    3A. 반시계 방향으로 $90^\circ$ 회전한다.
    3B. 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
    3C. 1번으로 돌아간다.
"""