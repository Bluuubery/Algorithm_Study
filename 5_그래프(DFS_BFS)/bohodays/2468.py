# 2468 안전 영역

import sys
sys.setrecursionlimit(10**6)

import copy

def DFS(x, y, key, tmp_arr):
    tmp_arr[x][y] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if tmp_arr[nx][ny] > key:
                DFS(nx, ny, key, tmp_arr)
        


N = int(input())

maxV = 0
arr = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    if maxV < max(tmp):
        maxV = max(tmp)
    arr.append(tmp)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


ans = 0
for key in range(maxV):
    cnt = 0
    tmp_arr = copy.deepcopy(arr)
    for i in range(N):
        for j in range(N):
            if tmp_arr[i][j] and tmp_arr[i][j] > key:
                cnt += 1
                DFS(i, j, key, tmp_arr)

    if cnt > ans:
        ans = cnt

print(ans)

