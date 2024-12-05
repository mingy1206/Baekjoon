from collections import deque

size = int(input())
apple_num = int(input())
board = [[False]*(size+2) for _ in range(size+2)]

wall = [[False]*(size+2) for _ in range(size+2)]
for i in range(1, size+1):
    for j in range(1, size+1):
        wall[i][j] = True


for _ in range(apple_num):
    n, m = map(int, input().split())
    board[n][m] = True

direction_num = int(input())
directions = ['']
for i in range(direction_num):
    n, m = map(str, input().split())
    num = len(directions)-1
    for j in range(int(n) - num):
        if j == int(n)-num-1:
            directions.append(m)
        else:
            directions.append('')

cnt = 0
dx = 1
dy = 0
queue = deque()
queue.append((1,1))
while True:
    cnt += 1
    x, y = queue[-1]
    nx = x+dx
    ny = y-dy

    if wall[ny][nx] is False:
        break

    if (nx,ny) in queue:
        break

    if board[ny][nx] is True:
        board[ny][nx] = False
    else:
        queue.popleft()

    queue.append((nx,ny))


    if cnt <= len(directions)-1:
        if directions[cnt] == 'D':
            temp = dx
            dx = dy
            dy = -temp
        elif directions[cnt] == 'L':
            temp = dy
            dy = dx
            dx = -temp

print(cnt)