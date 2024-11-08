from collections import deque

def bfs(n, k):
    distance = [0] * 100002
    queue = deque()
    queue.append(n)

    distance[n] = 0
    visited[n] = True

    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if visited[i] is not True:
                queue.append(i)
                visited[i] = True
                distance[i] = distance[node] + 1
                if i == k:
                    return  distance[i]




n, k = map(int, input().split())
visited = [False]*100002
graph = [[] for _ in range(100002)]

for i in range(len(graph)):
    if i+1 <= 100000:
        graph[i].append(i+1)
        graph[i+1].append(i)
    if i*2 <= 100000:
        graph[i].append(i*2)
        
if n == k:
    print(0)
else:
    print(bfs(n,k))
