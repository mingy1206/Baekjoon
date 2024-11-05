from collections import deque

def bfs(y, x):
    global cnt
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    if x >= size or y >= size or x < 0 or y < 0:
        return False
    if graph[y][x] == 0:
        return False
    if graph[y][x] == 1 and visited[y][x] == False:
        visited [y][x] = True
        graph[y][x] = total + 1 ## 리스트도 추가적으로 바꿔보기
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            bfs(ny, nx)
        return True
    return False

size = int(input())
graph =[list(map(int, input())) for _ in range(size)]
visited = [[False]*size for _ in range(size)]
result = []
total = 0

for i in range(size):
    for j in range(size):
        cnt = 0
        if bfs(i, j) is not False:
            total += 1
            result.append(cnt)

result.sort()

print(total)
for i in range(len(result)):
    print(result[i])

