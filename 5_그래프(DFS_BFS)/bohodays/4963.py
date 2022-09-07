# 4963 섬의 개수

from collections import deque

def bfs(x, y):
    global w, h, cnt
    # 큐를 생성하고 시작지점 추가
    queue = deque()
    queue.append((x, y))
    # 땅(1)의 좌표만 검사할 것이므로 cnt에 1 더해주기
    cnt += 1
    # 중복을 방지하기 위해 추가한 땅은 -1로 바꿔준다.
    map_list[x][y] = -1

    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 8가지 방향으로 땅(1) 탐색
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            # 영역을 벗어난 경우 무시
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            # 바다(0)인 경우 무시
            elif map_list[nx][ny] == 0:
                continue
            # 땅(1)인 경우, -1로 바꿔주고 좌표를 큐에 추가
            elif map_list[nx][ny] == 1:
                map_list[nx][ny] = -1
                queue.append((nx, ny))


while True:
    w, h = map(int, input().split())

    # 문제의 종료 조건
    if w == 0 and h == 0:
        break

    map_list = []
    for _ in range(h):
        map_list.append(list(map(int, input().split())))

    # 땅(1)이 있는 좌표 찾기
    ground = []
    for i in range(h):
        for j in range(w):
            if map_list[i][j] == 1:
                ground.append((i, j))

    # 상하좌우 대각선 확인
    dx = [-1, 1, 0, 0, -1, 1, 1, -1]
    dy = [0, 0, -1, 1, 1, 1, -1, -1]

    # 섬의 개수 카운팅
    cnt = 0

    for i in ground:
        if map_list[i[0]][i[1]] == 1:
            bfs(i[0], i[1])

    print(cnt)