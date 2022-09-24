# 10026 적록색약

import copy
import sys
sys.setrecursionlimit(10**6)

def DFS(x, y, target1, target2, arr):
    arr[x][y] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if arr[nx][ny] == target1 or arr[nx][ny] == target2:
                DFS(nx, ny, target1, target2, arr)

N = int(sys.stdin.readline())

arr = []
for _ in range(N):
    arr.append(list(sys.stdin.readline()))
tmp_arr = copy.deepcopy(arr)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 정상인 경우
cnt1 = 0
for i in range(N):
    for j in range(N):
        if arr[i][j]:
            cnt1 += 1
            if arr[i][j] == 'R':
                DFS(i, j, 'R', '', arr)
            elif arr[i][j] == 'G':
                DFS(i, j, 'G', '', arr)
            elif arr[i][j] == 'B':
                DFS(i, j, 'B', '', arr)

# 적록색약인 경우
cnt2 = 0
for i in range(N):
    for j in range(N):
        if tmp_arr[i][j]:
            cnt2 += 1
            if tmp_arr[i][j] == 'R' or tmp_arr[i][j] == 'G':
                DFS(i, j, 'R','G', tmp_arr)
            elif tmp_arr[i][j] == 'B':
                DFS(i, j, 'B', '', tmp_arr)

print(cnt1, cnt2)
            
