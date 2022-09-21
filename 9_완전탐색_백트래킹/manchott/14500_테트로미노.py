import sys
input = sys.stdin.readline

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(x, y, count, temp_sum):
    global max_sum
    # 만약 남은 칸 수 * 가장 큰 수를 더해도 현재의 최대값보다 작으면 끝낸다
    if temp_sum + max_num * (3 - count) <= max_sum:
        return
    # 4칸을 다 채웠다면 현재의 최대값과 계산한 값 중 더 큰 것을 답으로 저장
    if count == 3:
        max_sum = max(max_sum, temp_sum)
        return
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        # dfs 진행
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            # 만약 두칸까지 진행했다면 ㅗ모양을 고려하기 위해 
            # 한 칸 다음까지 갔다고 가정하고 현재 칸 부터 dfs 진행
            if count == 1:
                visited[nx][ny] = 1
                # 현재 칸이니까 x, y
                print(x, y, temp_sum)
                # temp_sum + grid[nx][ny]를 넘겨주는 이유: 
                # nx, ny는 갔다 치고(3칸 모양 됨) dfs 할 것이기 때문
                dfs(x, y, count + 1, temp_sum + grid[nx][ny])
                visited[nx][ny] =0
            visited[nx][ny] = 1
            dfs(nx, ny, count + 1, temp_sum + grid[nx][ny])
            visited[nx][ny] = 0


N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
max_num = max(map(max, grid))
max_sum = 0
for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(i, j, 0, grid[i][j])
        visited[i][j] = 0
print(max_sum)