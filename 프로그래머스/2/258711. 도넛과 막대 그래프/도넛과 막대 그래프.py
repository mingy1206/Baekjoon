# 생성한 정점 찾는 법 -> 다른 정점으로 가는 간선은 2개 이상 존재하지만, 오는 간선은 없을 때
# 도넛 모양 특징 -> n개의 정점과 n개의 간선
# 막대 모양 특징 -> n개의 정점과 n-1개의 간선
# 8자 모양 특징 -> 2n+1개의 정점과 2n+2개
# 1. 생성된 정점 구하기
# 2. 생성된 점점에서 DFS하면서 정점이랑 간선 개수 세기
import sys
sys.setrecursionlimit(10**7)

def solution(edges):
    graph = [[] for _ in range(1000001)]
    in_degree = [0]*(1000001)
    visited = [False]*(1000001)

    for a,b in edges:
        graph[a].append(b)
        in_degree[b] += 1
        
    new_node = 0
    num = len(graph)
    
    
    for i in range(1, num+1):
        if len(graph[i]) >= 2 and in_degree[i] == 0:
            new_node = i
            break
    
    answer = [new_node, 0, 0, 0]
    # 도넛 모양 특징 -> n개의 정점과 n개의 간선
    # 막대 모양 특징 -> n개의 정점과 n-1개의 간선
    # 8자 모양 특징 -> 2n+1개의 정점과 2n+2개의 간선
    for node in graph[new_node]:
        node_num, edge_num = dfs(graph, node, visited, 1, 0)
        for n in range(1, 1000001):
            if n == node_num and n == edge_num:
                answer[1] += 1
                break
            elif n == node_num and n-1 == edge_num:
                answer[2] += 1
                break
            elif (2*n)+1 == node_num and (2*n)+2 == edge_num:
                answer[3] += 1
                break
            
    
    return answer

def dfs(graph, node, visited, node_num, edge_num):
    visited[node] = True
    edge_num += len(graph[node])

    for v in graph[node]:
        if visited[v] is False:
            node_num, edge_num = dfs(graph, v, visited, node_num+1, edge_num)
            
    return [node_num, edge_num]