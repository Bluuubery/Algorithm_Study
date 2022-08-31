N = int(input())
grid = [list(map(int, input())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(x, y):
    global count
    visited[x][y] = 1
    if grid[x][y]:
        count += 1
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if not visited[nx][ny] and grid[nx][ny]:
                dfs(nx, ny)


count = 0
result = []
for i in range(N):
    for j in range(N):
        if grid[i][j] and not visited[i][j]:
            dfs(i, j)
            result.append(count)
            count = 0

result.sort()
print(len(result))
for house in result:
    print(house)