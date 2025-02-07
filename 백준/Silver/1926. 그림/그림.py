import sys
sys.setrecursionlimit(10**6)

def dfs(x,y):
    global current_width
    current_width += 1
    for i in range(4):
        dx,dy = directions[i]
        nx = x+dx
        ny = y+dy
        if 0<=nx<m and 0<=ny<n and li[ny][nx] == 1 and visited[ny][nx] == False:
            visited[ny][nx] = True
            dfs(nx,ny)

n,m = map(int, sys.stdin.readline().rstrip().split())
li = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
cnt = 0
max_width = 0


for y in range(n):
    for x in range(m):
        if li[y][x] == 1 and visited[y][x] == False:
            current_width = 0
            visited[y][x] = True
            dfs(x,y)
            max_width = max(max_width,current_width)
            cnt += 1


print(cnt)
print(max_width)



