import sys

N,L = map(int, sys.stdin.readline().rstrip().split())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
ans = 0
def check(lst, v):
    cnt = 1
    for j in range(N-1):
        # 높이 차이 2이상
        if lst[j]+1 < lst[j+1]:
            return False
        # 내리막
        elif lst[j] > lst[j+1]:
            cnt = 1
        # 경사로 설치 가능
        elif lst[j]+1 == lst[j+1] and v[j+1-L:j+1] == [0]*L and cnt >= L:
            v[j+1-L:j+1] = [1]*L
            cnt = 1
        # 평지
        elif lst[j] == lst[j+1]:
            cnt += 1
        else:
            return False
    return True


for i in range(2):
    for lst in arr:
        v = [0]*N
        # 정방향 and 역방향
        if check(lst, v) and check(lst[::-1], v[::-1]):
            ans += 1
    # 전치행렬
    arr = list(map(list, zip(*arr)))

print(ans)