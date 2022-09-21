# 14891 톱니바퀴

# 재귀적으로 자석들을 회전시키는 함수
def rotation(n, d):
    global visited
    # 방문한 자석 기록
    visited[n] = True
    if n < 3:
        # 오른쪽 자석 확인
        # 자성이 다르고 오른쪽 자석을 방문하지 않았다면 재귀적으로 방문
        if magnetic[n][2] != magnetic[n+1][6] and not visited[n+1]:
            rotation(n+1, -d)
    if n > 0:
        # 왼쪽 자석 확인
        # 자성이 다르고 왼쪽 자석을 방문하지 않았다면 재귀적으로 방문
        if magnetic[n][6] != magnetic[n-1][2] and not visited[n-1]:
            rotation(n-1, -d)
    # 자석을 시계방향으로 회전
    if d == 1:
        tmp = magnetic[n].pop()
        magnetic[n].insert(0, tmp)
    # 자석을 반시계방향으로 회전
    elif d == -1:
        tmp = magnetic[n][0]
        del magnetic[n][0]
        magnetic[n].append(tmp)


# 자석 정보 저장
magnetic = []
for _ in range(4):
    magnetic.append(list(map(int, input())))

K = int(input())

# 회전 정보 저장
rotation_info = []
for _ in range(K):
    rotation_info.append(list(map(int,input().split())))

for i in rotation_info:    
    visited = [False] * 4
    rotation(i[0]-1, i[1])

ans = 0
for idx, i in enumerate(magnetic):
    if i[0] == 1:
        ans += 2**idx


print(ans)
