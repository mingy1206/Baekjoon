import sys
from collections import deque
N,K = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(100001)]
queue = deque()
queue.append(N)
distance = [0]*100001

for i in range(100000):
    graph[i].append(i+1)
    graph[i+1].append(i)
    if i*2<=100000:
        graph[i].append(i*2)


def bfs():
    while queue:
        node = queue.popleft()
        if node == K:
            return distance[node]

        for i in graph[node]:
            if distance[i] == 0:
                queue.append(i)
                distance[i] = distance[node] + 1

print(bfs())