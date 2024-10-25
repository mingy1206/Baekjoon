from collections import deque

def bfs():
    visited[1] = True
    queue = deque([1])
    cnt = 0
    while queue:
        worm = queue.popleft()
        for i in graph[worm]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                cnt += 1

    return cnt

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for i in range(m):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

for i in range(len(graph)):
    graph[i].sort()

visited = [False]*(n+1)
print(bfs())




"""
7
6
1 2
2 3
1 5
5 2
5 6
4 7
"""