def dfs(n, m, cnt):

    visited[n] = True
    cnt += 1
    for i in family[n]:
        if not visited[i] == True:
            if i == m:
                stack.append(cnt)
            else:
                dfs(i, m, cnt)




total = int(input())
p1, p2 = map(int, input().split())
num = int(input())

family = [[] for _ in range(total+1)]

for i in range(num):
    node1, node2 = map(int, input().split())
    family[node1].append(node2)
    family[node2].append(node1)

stack = []
visited = [False] * (total + 1)
cnt = 0
dfs(p1, p2, cnt)

if len(stack) == 0:
    print(-1)
else:
    print(stack[0])


