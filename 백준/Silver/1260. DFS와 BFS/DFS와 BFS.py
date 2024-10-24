from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i] == True:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    visited[v] =True
    queue = deque([v])

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i] == True:
                visited[i] = True
                queue.append(i)

n, m, v = map(int, input().split())
graph = [[]for i in range(n+1)]
visited = [False]*(n+1)

for i in range(m):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

for i in range(len(graph)):
    graph[i].sort()

visited = [False]*(n+1)
dfs(graph, v, visited)

print()

visited = [False]*(n+1)
bfs(graph, v, visited)

