from collections import deque

def dfs(x):
    global visited_d
    visited_d[x] = 1
    print(x, end=' ')
    for i in graph[x]:
        if not visited_d[i]:
            dfs(i)


def bfs(x):
    queue = deque([x])
    visited_b[x] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited_b[i]:
                queue.append(i)
                visited_b[i] = True


N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited_d = [0] * (N + 1)
visited_b = [0] * (N + 1)
for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
for i in graph:
    i.sort()

dfs(V)
print()
bfs(V)
