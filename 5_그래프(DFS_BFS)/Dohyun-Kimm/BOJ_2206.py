# 벽 부수고 이동하기
# 2022-08-27

# 미로를 빠져나가는 최소 경로 구하기
# + 벽을 한칸만 부시고 길을 만들 수 있음
# 부수고 이동하는 조건을 구현하기
# 0= 이동가능, 1 = 벽
# 1< N,M< 1000,
# 벽 부수기 구현만 하면됨
def maze_break_wall(G,n,m):   # G: mat, v: start node
    queue = list()
    visited = [[0] * m for _ in range(n)]
    dx = [1, -1, 0, 0]      # 방향키 좌 우
    dy = [0, 0, 1, -1]      # 방향키 하 상
    # 벽 부수기 카운트 용 스택 1일때 인접 노드가 1이면 인큐 못하게
    # 스택 0 일때 인접 노드가 1이면 인큐
    stack = 0
    v = [0, 0]
    queue.append(v)
    while queue:
        t = queue.pop(0)     # queue 의 맨 앞 값 팝해주기

        if not visited[t[0]][t[1]]:
            visited[t[0]][t[1]] = 1
            if G[t[0][t[1]]] == 1:
                stack = 1
        for d in range(4):      # 인접 노드 델타 탐색
            x = t[0] + dx[d]    # 4 방향 인접 노트 탐색
            y = t[1] + dy[d]
            if -1 < x < N and -1 < y < M:   # 맵 안에 있다면 이동 가능
                if stack == 0:              # 벽 부수기를 하지 않았다면 0 ,1 둘다 가능
                    w = [x, y]
                    queue.append(w)
                    G[w[0]][w[1]] = G[t[0]][t[1]] + 1
                elif stack == 1:                       # 벽부수기를 한 상태면 0만 가능
                    if G[x][y] == 0:
                        w = [x, y]
                        queue.append(w)
                        G[w[0]][w[1]] = G[t[0]][t[1]] + 1
                        # stack = 0           # 0으로 이동하면  스택 초기화
                    else:
                        continue
    for f in range(N):
        print(visited[f])
    # print(G)
    return G[N-1][M-1]


N, M = map(int, input().split())        # N = 행, M = 열
mat = [[0] * M for _ in range(N)]
for p in range(N):
    line = input()         # 맵 입력받기
    for q in range(M):
        mat[p][q] = int(line[q])


print(maze_break_wall(mat, N, M))
for e in range(N):
    print(mat[e])
