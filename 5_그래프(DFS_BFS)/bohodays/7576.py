# 7576 토마토

from collections import deque
import sys

# bfs 함수 생성
def bfs():
    # 큐를 구현하고 토마토의 좌표 추가
    queue = deque()
    for i, j in tomato:
        queue.append((i, j))
    
    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                # 토마토가 안 익었으면(0이면) 이전 값에서 +1 해준다.
                if box[nx][ny] == 0:
                    box[nx][ny] = box[x][y] + 1
                    # 새로운 좌표를 큐에 추가
                    queue.append((nx, ny))
        for k in box:
            print(k)
        print()

M, N = map(int, input().split())

# 토마토 정보 추가
box = []
for _ in range(N):
    box.append(list(map(int, sys.stdin.readline().split())))

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 토마토 좌표 찾기
tomato = []
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            tomato.append((i,j))

# 함수 호출
bfs()

maxV = 0
flag = False
for i in range(N):
    for j in range(M):
        # 안 익은 토마토가 있으면 flag를 True로 설정
        if box[i][j] == 0:
            flag = True
        # 안 익은 토마토가 없다면 최대값 구하기
        else:
            if box[i][j] > maxV:
                maxV = box[i][j]

if flag:
    print(-1)
else:
    print(maxV-1)
    