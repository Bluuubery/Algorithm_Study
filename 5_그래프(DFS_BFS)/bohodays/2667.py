# 2667 단지번호붙이기

def DFS(x, y):
    global arr, cnt
    arr[x][y] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if arr[nx][ny] == 1:
                cnt += 1
                DFS(nx, ny)

N = int(input())

arr = []
for _ in range(N):
    arr.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

total = 0
result = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            total += 1
            cnt = 1
            DFS(i, j)
            result.append(cnt)

print(total)
result.sort()
for i in result:
    print(i)