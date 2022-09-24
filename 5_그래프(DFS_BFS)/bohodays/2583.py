# 2583 영역 구하기

import sys
sys.setrecursionlimit(10**6)

def DFS(x, y):
    global cnt
    cnt += 1
    area[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N:
            if area[nx][ny] == 0:
                DFS(nx, ny)

M, N, K = map(int, sys.stdin.readline().split())

rectangle = []
for _ in range(K):
    rectangle.append(list(map(int, sys.stdin.readline().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

area = [[0] * N for _ in range(M)]

for tmp in rectangle:
    for i in range(M-tmp[3], M-tmp[1]):
        for j in range(tmp[0], tmp[2]):
            area[i][j] = 1

ans = 0
result = []
for i in range(M):
    for j in range(N):
        if area[i][j] == 0:
            ans += 1
            cnt = 0
            DFS(i, j)
            result.append(cnt)

print(ans)
result.sort()
print(*result)
