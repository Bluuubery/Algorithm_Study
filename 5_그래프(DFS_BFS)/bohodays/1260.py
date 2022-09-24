# 1260 DFS와 BFS

from collections import deque

def DFS(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            # visited[i] = True
            DFS(graph, i, visited)

def BFS(graph, v, visited):
    queue = deque()
    queue.append(v)
    visited[v] = True

    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for i in graph[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


# 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V
N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    graph[i].sort()

visited = [False] * (N+1)
DFS(graph, V, visited)
print()
visited = [False] * (N+1)
BFS(graph, V, visited)
