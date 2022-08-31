import sys
sys.setrecursionlimit(10 ** 9)

# x : 시작 노드 번호, y : 시작 노드의 가중치
# 1의 가중치 0으로 설정
def dfs(graph, x, y, visited):
    # ex) [[(2, 3), (3, 2)]]
    for i in graph[x]:
        # 방문하지 않은 노드라면 탐색
        if visited[i[0]] == -1:
            # ex) visited의 2번 인덱스에 가중치 저장
            visited[i[0]] = i[1] + y
            dfs(graph, i[0],  i[1] + y, visited)
            

# 노드의 개수
n = int(input())

# 인접리스트 생성
graph = [[] for _ in range(n+1)]
for i in range(n-1):
    a, b, c = map(int, sys.stdin.readline().split())
    # 인접 번호와 가중치를 튜플로 저장
    graph[a].append((b, c))
    graph[b].append((a, c))

# 방문 확인 리스트 -1로 초기화
visited = [-1] * (n+1)
# 시작 노드 번호의 가중치 0으로 설정
visited[1] = 0

# 첫 번째 노드 (1)에서 탐색 시작
dfs(graph, 1, 0, visited)
# 가중치의 합이 가장 큰 노드의 인덱스 저장
idx = visited.index(max(visited))

# 위에서 구한 인덱스에서 탐색을 시작하여 가중치의 합이 가장 큰 노드 찾기
visited = [-1] * (n+1)
visited[idx] = 0
dfs(graph, idx, 0, visited)

# 가장 큰 값 출력
print(max(visited))

