from collections import deque

n, m = map(int, input().split())
# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

visited = [[0] * m for _ in range(n)]
visited[0][0] = 1

# 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 벽을 부술 수 있는 기회 표시
chance = True

# BFS 소스코드 구현
def bfs(x, y):
    global chance
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복하기
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if 0 <= nx < n and 0 <= ny < m:
                # 벽인 경우
                if graph[nx][ny] == 1:
                    if visited[nx][ny] == 0 and chance == True:
                        chance = False
                        visited[nx][ny] = visited[x][y] + 1
                        queue.append((nx, ny))
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
                else:
                    if visited[nx][ny] == 0:
                        visited[nx][ny] = visited[x][y] + 1
                        queue.append((nx, ny))

            for i in visited:
                print(i)
            print()
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n - 1][m - 1]


# BFS를 수행한 결과 출력
print(bfs(0,0))

