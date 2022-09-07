# BOJ_1206
# 2022-08-29


# DFS_BFS
# BFS
# 첫 정점 큐에 추가
# 큐에서 팝으로 받아오고
# 방문안한 정점이면 방문하기
# 방문한 노드의 인접한 노드들중, 방문한적이 없는 노드들만 큐에 추가
# 큐가 빌때까지 반복

def bfs(g,vv):
    bfs_visited = [0] *(N+1)
    queue = list()
    queue.append(vv)
    while queue:
        # 큐에 있는 노드 팝해서 방문하기 맨 앞에 있는것 팝
        t = queue.pop(0)        # 1- 2,3,4/ 2-4
        if not bfs_visited[t]:
            bfs_visited[t] = 1
            print(t,end=' ')
            for n in g[t]:          # t와 인접한 노드들
                if not bfs_visited[n]:
                    queue.append(n)



# N 정점수, M 간선수, v 시작 노드
N, M, v = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

print(graph)

# for문으로 DFS 구현하기
# 노드 1에서 시작해서 깊이우선 탐색을하며, 방문한 곳은 프리트하기
stack = list() # 방문 노드를 기록하는 곳
visited = [0] * (N +1) # 1대1 매칭을 위해 N+1개 만들고 인덱스 0 사용 안하기
flag = 0
dfs_v = v
stack.append(dfs_v)
visited[dfs_v]= 1
print(dfs_v, end=' ')
while stack:
    for node in graph[dfs_v]:   # 2 3 4 / 2
        if not visited[node]:
            stack.append(dfs_v)  # 시작 노드를 스택에 푸시
            dfs_v = node
            visited[dfs_v] = 1
            print(dfs_v, end=' ')
            break
    else:
        if stack:
            dfs_v = stack.pop()
        else:
            break

print()
# BFS
bfs(graph,v)


