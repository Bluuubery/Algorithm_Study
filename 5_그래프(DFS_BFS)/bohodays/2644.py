# 2644 촌수계산

def DFS(v, target, cnt):
    cnt += 1
    # 방문처리
    visited[v] = True

    if v == target:
        ans.append(cnt-1)
        
    for i in graph[v]:
        # 방문하지 않았다면
        if not visited[i]:
            DFS(i, target, cnt)

#노드 수
n = int(input())

a, b = map(int, input().split())

# 간선 수
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    tmp1, tmp2 = map(int, input().split())
    graph[tmp1].append(tmp2)
    graph[tmp2].append(tmp1)

visited = [False] * (n+1)
ans = [-1]

DFS(a, b, 0)
print(ans[-1])
