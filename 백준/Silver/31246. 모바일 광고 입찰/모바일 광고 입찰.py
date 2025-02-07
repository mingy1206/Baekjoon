import sys
N,K = map(int, sys.stdin.readline().rstrip().split())
li = [0]*N
X = 0
result = 0
for i in range(N):
    a,b = map(int, sys.stdin.readline().rstrip().split())
    li[i] = a-b

li.sort(reverse=True)
if li[K-1] >= 0:
    print(0)
else:
    print(abs(li[K-1]))

