def move_west():
    dice[1], dice[2], dice[3], dice[5] = dice[5], dice[1], dice[2], dice[3]
def move_east():
    dice[1], dice[2], dice[3], dice[5] = dice[2], dice[3], dice[5], dice[1]
def move_north():
    dice[0], dice[2], dice[4], dice[5] = dice[2], dice[4], dice[5], dice[0]
def move_south():
    dice[0], dice[2], dice[4], dice[5] = dice[5], dice[0], dice[2], dice[4]

n, m, y, x, k = map(int, input().split(' '))
paper = [list(map(int, input().split(' '))) for _ in range(n)]
move = list(map(int, input().split(' ')))

dice = [0,0,0,0,0,0]

directions = [(1,0), (-1,0), (0,1), (0,-1)]
for i in move:
    instruction = i - 1
    dx, dy = directions[instruction]

    nx = x + dx
    ny = y - dy # 북쪽의 y좌표가 0

    if nx < 0 or nx >= m or ny < 0 or ny >= n:
        continue

    if instruction == 0:
        move_east()
    elif instruction == 1:
        move_west()
    elif instruction == 2:
        move_north()
    elif instruction == 3:
        move_south()

    if paper[ny][nx] == 0:
        paper[ny][nx] = dice[5]
    else:
        dice[5] = paper[ny][nx]
        paper[ny][nx] = 0

    x = nx
    y = ny
    print(dice[2])
