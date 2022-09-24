# 11725 트리의 부모 찾기

import sys
sys.setrecursionlimit(10**6)

def DFS(graph, v, visited):
    global p
    # 방문 처리
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            p[i] = v
            DFS(graph, i, visited)

N = int(sys.stdin.readline())

graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N + 1)
p = [0] * (N + 1)

DFS(graph, 1, visited)
for i in p[2:]:
    print(i)