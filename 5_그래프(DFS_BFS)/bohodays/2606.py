# 2606 바이러스

def DFS(graph, v, visited):
    global cnt
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            cnt += 1
            DFS(graph, i, visited)


# 정점의 수
N = int(input())
# 간선의 수
M = int(input())

# 그래프 생성
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)

cnt = 0
DFS(graph, 1, visited)

print(cnt)