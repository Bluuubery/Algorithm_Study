# 유기농 배추

import sys
sys.setrecursionlimit(10000)

def DFS(x, y):
    global graph
    graph[x][y] = 0
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if not visited[nx][ny] and graph[nx][ny] == 1:
                DFS(nx, ny)

T = int(input())

for _ in range(T):
    # 배추를 심은 배추밭의 가로길이 M(1 ≤ M ≤ 50)과 세로길이 N(1 ≤ N ≤ 50), 그리고 배추가 심어져 있는 위치의 개수 K(1 ≤ K ≤ 2500)
    M, N, K = map(int, input().split())

    # 그래프 생성
    graph = [[0]*M for _ in range(N)]

    # 방문 확인 리스트 생성
    visited = [[False] * M for _ in range(N)]

    # 배추 위치 표시
    for _ in range(K):
        a, b = map(int, input().split())
        graph[b][a] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    ans = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                ans += 1
                DFS(i, j)
    
    print(ans)