import sys
n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().rstrip().split()))
x = int(sys.stdin.readline().rstrip())
result = []
a.sort()

for j in range(1, len(a)):
    if a[j] >= x:
        break
    if a[j] < (x//2)+1:
        continue
    for i in range(j):
        if a[i]+a[j] == x:
            result.append([i,j])
        if a[i]+a[j] > x:
            break

print(len(result))


# 1 2 3 5 7 9 10 11 12
# 13