import sys

N,M,H = map(int, sys.stdin.readline().rstrip().split())
li = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(M)]
grph = [[0]*(N+2) for _ in range(H+2)]
result = -1
add = []
def dfs(n,p):
    global result
    if n == cnt:
        if search() is True:
            result = n
        return

    for i in range(p,len(add)):
        ny,nx = add[i]
        if grph[ny][nx-1] == 0 and grph[ny][nx+1] == 0:
            grph[ny][nx] = 1
            dfs(n+1, i+1)
            grph[ny][nx] = 0
        if result != -1:
            return True

def search():
    for k in range(1,N+1):
        point = k
        for h in range(1,H+1):
            if grph[h][point-1] == 1:
                point -= 1
            elif grph[h][point] == 1:
                point += 1
        if point != k:
            return False
    return True

for y,x in li:
    grph[y][x] = 1

for y in range(1,H+1):
    for x in range(1, N+1):
        if grph[y][x] == 0:
            add.append([y,x])
for cnt in range(4):
    if dfs(0,0) is True:
        break


print(result)

