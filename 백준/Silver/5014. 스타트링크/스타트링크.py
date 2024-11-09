from collections import deque

f, s, g, u, d = map(int, input().split())

graph = [[] for _ in range(f+1)]

for i in range(len(graph)):
    if i == 0:
        continue
    if i + u <= f:
        graph[i].append(i+u)
    if i - d >= 1:
        graph[i].append(i-d)

queue = deque()
queue.append(s)

pushing = [-1] * (f+1)
pushing[s] = 0

check = 0
push = "use the stairs"
if s == g:
    print(0)
else:
    while queue:
        now = queue.popleft()
        for i in graph[now]:

            if pushing[i] == -1:
                queue.append(i)
                pushing[i] = pushing[now] + 1
                if i == g:
                    check = 1
                    push = pushing[i]
                    break
        if check == 1:
            break
    print(push)

