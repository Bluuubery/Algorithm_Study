# 11724 연결 요소의 개수

import sys
sys.setrecursionlimit(5000)

def DFS(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            DFS(graph, i, visited)


# N은 정점의 개수, M은 간선의 개수
N, M = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)
cnt = 0

for i in range(1, N+1):
    # 방문하지 않았다면
    if not visited[i]:
        # 정점이 1개인 요소를 확인
        if not graph[i]:
            cnt += 1
            visited[i] = True
        # 연결되어 있다면 DFS 수행
        else:
            DFS(graph, i, visited)
            cnt += 1

print(cnt)