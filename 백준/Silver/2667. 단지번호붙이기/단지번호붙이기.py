from collections import deque
def dfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    if y < 0 or x < 0 or y >= n or x >= n:
        return False
    if graph[y][x] == 0:
        return False
    if graph[y][x] == 1:
        graph[y][x] = 0
        global num
        num += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            dfs(nx, ny)
        return True

    return False

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]

cnt = 0
num = 0
li = []
for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            li.append(num)
            num = 0
            cnt += 1
print(cnt)
li.sort(reverse=True)
for i in range(len(li)):
    print(li.pop())










"""
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
"""