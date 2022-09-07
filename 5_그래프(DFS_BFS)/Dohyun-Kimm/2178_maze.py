# 백준_2178_미로탐색
# 2022-08-25

# 배열 크기 N M
# 1이동가능 0 벽
# 도착 위치로 이동할수 있는 경우만입력으로 주어짐
# 이동하는 칸의 수를 최소로 가지는 경우.........턴 하는 경우 빼줘야됨

def path_finder(G, v):
    visited = [[0] * M for _ in range(N)]
    queue = list()

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue.append(v)
    # G[v[0]][v[1]] += 1
    while queue:
        w =queue.pop(0)
        if not visited[w[0]][w[1]]:     # 방문한적이 없다면
            visited[w[0]][w[1]] = 1     # 방문 했다는 표시

            for d in range(4):          # 다음 이동할 곳 찾기
                x = w[0] + dx[d]
                y = w[1] + dy[d]
                if -1 < x < N and -1< y < M:     # 인덱스 오류 안나게
                    if G[x][y] == 1 and not visited[x][y]:            # 1이라면 이동 가능하니까 인큐
                        queue.append([x, y])
                        G[x][y] = G[w[0]][w[1]] + 1

                    else:                        
                        continue
    return G[N-1][M-1]


N, M = map(int, input().split())
maze = [[0] * M for _ in range(N)]
for i in range(N):
    line = input()
    for j in range(M):
        maze[i][j] = int(line[j])

print(path_finder(maze, [0, 0]))