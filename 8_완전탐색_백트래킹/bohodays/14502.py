# 14502 연구소

from collections import deque
from copy import deepcopy
import sys

# BFS
def bfs():
    global ans
    queue = deque(two_list)

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < N) and (0 <= ny < M):
                if tmp_arr[nx][ny] == 0:
                    tmp_arr[nx][ny] =2
                    queue.append((nx,ny))

    # 최대값 갱신
    tmp_ans = 0
    for i in tmp_arr:
        tmp_ans += i.count(0)

    ans = max(ans, tmp_ans)
    

# 조합
def my_combination(arr, n):
    result = []

    if n == 0:
        return [[]]

    for i in range(len(arr)):
        elem = arr[i]
        for j in my_combination(arr[i + 1:], n - 1):
            result.append([elem] + j)

    return result

# 입력받기
N, M = map(int, sys.stdin.readline().split())

arr = []
for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))


# arr에서 0인 좌표와 2인 좌표를 각각 리스트에 할당
com_list = []
two_list = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            com_list.append([i,j])
        elif arr[i][j] == 2:
            two_list.append([i,j])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

ans = 0
tmp_arr = deepcopy(arr)
# arr에서 0인 좌표 3개씩 1로 만들고, bfs 수행
for i in my_combination(com_list, 3):
    for j in i:
        tmp_arr[j[0]][j[1]] = 1
    bfs()
    tmp_arr = deepcopy(arr)

print(ans)

