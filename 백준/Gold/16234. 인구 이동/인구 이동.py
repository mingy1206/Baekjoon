from collections import deque
import sys
input = sys.stdin.readline

def main():
    n,l,r = map(int,input().split())
    board = [list(map(int,input().split())) for _ in range(n)]
    visited = [[-1]*n for _ in range(n)]
    cnt = 0
    move = [(1,0),(-1,0),(0,1),(0,-1)]
    # 격자 모양으로 탐색
    cand = deque([(i,j) for i in range(n) for j in range(i%2,n,2)])
    
    while True:
        q = deque()
        for _ in range(len(cand)):
            i,j = cand.popleft()
            if visited[i][j] == cnt:
                continue
            visited[i][j] = cnt
            area = set([(i,j)])
            popul = board[i][j]
            q.append((i,j))
            
            # BFS
            while q:
                x,y = q.popleft()
                for a,b in move:
                    dx=x+a; dy=y+b
                    if dx>=n or dx<0 or dy>=n or dy<0 or visited[dx][dy] == cnt:
                        continue

                    if l<=abs(board[x][y]-board[dx][dy])<=r:
                        visited[dx][dy] = cnt
                        area.add((dx,dy))
                        popul += board[dx][dy]
                        q.append((dx,dy))
            
            # 국경선이 열린 경우
            if len(area) > 1:
                avg_popul = popul//len(area)
                for x,y in area:
                    board[x][y] = avg_popul
                    cand.append((x,y))
        if cand:
            cnt += 1
        else:
            break
    print(cnt)
main()