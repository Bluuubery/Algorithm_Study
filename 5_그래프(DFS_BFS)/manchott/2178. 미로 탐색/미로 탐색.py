from collections import deque

N, M = map(int, input().split())
maze = [list(input()) for _ in range(N)]
# 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
x, y = 0, 0
queue = deque()
queue.append((x, y))
graph = [[0] * M for _ in range(N)]
while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 미로 찾기 공간을 벗어난 경우 무시
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        # 이동할 수 없는 경우 무시
        if maze[nx][ny] == '0':
            continue
        # 한번도 방문하지 않은 경우 최소 경로 입력
        if graph[nx][ny] == 0:
            graph[nx][ny] = graph[x][y] + 1
            queue.append((nx, ny))
print(graph[N - 1][M - 1] + 1)
