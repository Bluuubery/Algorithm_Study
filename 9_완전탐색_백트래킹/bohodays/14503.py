# 14503 로봇 청소기

from collections import deque
import sys

# bfs 구현
def bfs(x, y, d):
    global cnt
    queue = deque()
    # 시작 위치 방문 처리
    queue.append((x, y, d))
    table[x][y] = 2
    cnt += 1

    while queue:
        x, y, d = queue.popleft()
        # 종료상태 확인을 위해 d값 복사
        tmp_d = d
        # 회전 횟수
        turn = 0

        for _ in range(4):
            nd = (tmp_d + 3) % 4
            nx = x + dx[nd]
            ny = y + dy[nd]
            # 회전한 방향으로 다시 설정
            tmp_d = nd

            if 0 <= nx < n and 0 <= ny < m:
                # 청소하지 않은 곳이라면
                if table[nx][ny] == 0:
                    queue.append((nx, ny, nd))
                    # 방문 처리
                    table[nx][ny] = 2
                    cnt += 1
                    # 이동한 칸에서 다시 검사
                    break
                # 벽이라면 회전
                else:
                    turn += 1

        # 4방향 모두 청소했는지 확인
        if turn == 4:
            # 뒤쪽 확인 (북: 0, 동: 1, 남: 2, 서: 3) -> (남: 2, 서: 3, 북: 0, 동: 1)
            nx = x + dx[(d + 2) % 4]
            ny = y + dy[(d + 2) % 4]
            # 뒤쪽 방향이 벽이라서 후진할 수 없는 경우
            if table[nx][ny] == 1:
                return cnt
            # 뒤쪽 방향이 벽이 아니라면 바라보는 방향을 유치한 채로 한 칸 후진
            queue.append((nx, ny, d))

n,m = map(int, sys.stdin.readline().split())
r,c,d = map(int,sys.stdin.readline().split())

# 북쪽을 기준으로 시계방향 (문제 제시)
dx = [-1,0,1,0]
dy = [0,1,0,-1]

table = []
for _ in range(n):
    table.append(list(map(int,sys.stdin.readline().split())))

# 청소 횟수
cnt = 0
print(bfs(r, c, d))
